# Modular Calculator CLI (Python)

A clean, modular Python application that supports both interactive and command-line usage.
Built with professional engineering practices including logging, custom exceptions, and automated tests.

## Features
- Supports +, -, *, /, ** operations
- Works in interactive mode or via CLI arguments
- Custom exception handling for invalid operations and inputs
- Logging for application flow and errors
- Automated unit tests
- Clean modular folder structure

## Run (Interactive Mode)
```bash
python run.py

Run (CLI Mode)
python run.py 10 5 +
python run.py 2 3 **

Run Tests
python -m tests.test_math_ops

Project Structure
app/
  utils/
  config/
  exceptions.py
tests/
run.py
