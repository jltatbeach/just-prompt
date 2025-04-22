"""
Tests for DeepSeek provider.
"""

import pytest
import os
from dotenv import load_dotenv
from just_prompt.atoms.llm_providers import deepseek

# Load environment variables
load_dotenv()

# Skip tests if API key not available
if not os.environ.get("DEEPSEEK_API_KEY"):
    pytest.skip("DeepSeek API key not available", allow_module_level=True)


def test_list_models():
    """Test listing DeepSeek models."""
    models = deepseek.list_models()
    assert isinstance(models, list)
    assert len(models) > 0
    assert all(isinstance(model, str) for model in models)


def test_prompt():
    """Test sending prompt to DeepSeek."""
    try:
        # First check if the DeepSeek key is valid by attempting to list models
        models = deepseek.list_models()
        if not models or len(models) == 0:
            pytest.skip("DeepSeek API key appears to be invalid or DeepSeek API is not responding")
            
        # Try sending a prompt
        response = deepseek.prompt("What is the capital of France?", "deepseek-coder")
        assert isinstance(response, str)
        assert len(response) > 0
        assert "paris" in response.lower() or "Paris" in response
    except Exception as e:
        # If we get an authentication error, skip the test
        if "authentication" in str(e).lower() or "api key" in str(e).lower() or "401" in str(e):
            pytest.skip(f"DeepSeek API key appears to be invalid: {str(e)}")
        else:
            # If it's not an authentication error, re-raise it
            raise
