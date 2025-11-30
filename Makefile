.PHONY: install dev lint format test clean

# Install dependencies
install:
	pip install -e ".[dev]"

# Run development server
dev:
	uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

# Run linter (check only)
lint:
	ruff check src tests

# Format code
format:
	ruff check src tests --fix
	ruff format src tests

# Run tests
test:
	pytest tests -v

# Clean cache files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	