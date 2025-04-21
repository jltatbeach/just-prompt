# just-prompt

## Commands
- DO NOT ever `git add` or `git commit` code. Allow the Claude user to always manually review changes.
- DO NOT ever remove tests from pytest

## Code Style
- **Error Handling**: Log errors with proper context 
- Follow existing component patterns with clear interfaces.
- Follow existing error handling patterns with optional chaining and fallbacks.
- When adding source code or new files, enhance, update, and provide new unit tests using the existing Vitest patterns.

## Common Tasks
- If connected to a `mcp-shell-server` also known as just a "shell", run all shell commands through that mcp server. This approach will automatically restrict which commands can be run and properly configure the shell environment. 

## Project Specifics
- DO NOT change language or narratives when synthesizing code. Ask if you feel changes are necessary.
