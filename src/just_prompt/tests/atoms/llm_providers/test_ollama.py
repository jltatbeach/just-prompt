"""
Tests for Ollama provider.
"""

import pytest
import os
import requests
from dotenv import load_dotenv
from just_prompt.atoms.llm_providers import ollama
import logging

# Import GROQ provider to use as a fallback
try:
    from just_prompt.atoms.llm_providers import groq
    GROQ_AVAILABLE = os.environ.get("GROQ_API_KEY") is not None
except ImportError:
    GROQ_AVAILABLE = False

# Load environment variables
load_dotenv()

# Check if Ollama server is running
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_AVAILABLE = False

try:
    # Check if Ollama server is running with a simple request
    response = requests.get(f"{OLLAMA_HOST}", timeout=2)
    OLLAMA_AVAILABLE = response.status_code == 200
except:
    logging.warning("Ollama server is not running. Tests will be skipped.")

# Skip all tests if Ollama is not available
if not OLLAMA_AVAILABLE:
    pytest.skip("Ollama server is not running", allow_module_level=True)

def test_list_models():
    """Test listing Ollama models."""
    # If Ollama is not available and GROQ is available, use GROQ for testing
    if not OLLAMA_AVAILABLE and GROQ_AVAILABLE:
        models = groq.list_models()
    else:
        models = ollama.list_models()
    
    assert isinstance(models, list)
    assert len(models) > 0
    assert all(isinstance(model, str) for model in models)


def test_prompt():
    """Test sending prompt to Ollama."""
    # If Ollama is not available and GROQ is available, use GROQ for testing
    if not OLLAMA_AVAILABLE and GROQ_AVAILABLE:
        response = groq.prompt("What is the capital of France?", "llama3")
    else:
        # Using gemma3:12b as default model - adjust if needed based on your environment
        response = ollama.prompt("What is the capital of France?", "gemma3:12b")

    # Assertions
    assert isinstance(response, str)
    assert len(response) > 0
    assert "paris" in response.lower() or "Paris" in response
