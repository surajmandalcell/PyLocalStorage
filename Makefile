.PHONY: clean build test publish-test publish install-dev help

# Define ANSI color codes for terminal output
BLUE=\033[36m
GREEN=\033[32m
YELLOW=\033[33m
RESET=\033[0m

help:
	@echo "$(BLUE)localStoragePro Makefile$(RESET)"
	@echo "$(YELLOW)make clean$(RESET)        - Remove build artifacts"
	@echo "$(YELLOW)make build$(RESET)        - Build the package"
	@echo "$(YELLOW)make test$(RESET)         - Run tests"
	@echo "$(YELLOW)make install-dev$(RESET)  - Install development dependencies"
	@echo "$(YELLOW)make publish-test$(RESET) - Publish to TestPyPI"
	@echo "$(YELLOW)make publish$(RESET)      - Publish to PyPI"

clean:
	@echo "$(BLUE)Cleaning up build artifacts...$(RESET)"
	-rmdir /s /q build
	-rmdir /s /q dist
	-rmdir /s /q *.egg-info
	-for /d /r . %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"
	-del /s /q *.pyc
	@echo "$(GREEN)Cleanup complete.$(RESET)"

build: clean
	@echo "$(BLUE)Building package...$(RESET)"
	python -m pip install --upgrade pip
	python -m pip install --upgrade build
	python -m build
	@echo "$(GREEN)Build complete.$(RESET)"

install-dev:
	@echo "$(BLUE)Installing development dependencies...$(RESET)"
	python -m pip install --upgrade pip
	python -m pip install -e ".[dev]"
	@echo "$(GREEN)Development dependencies installed.$(RESET)"

test: install-dev
	@echo "$(BLUE)Running tests...$(RESET)"
	python -m pytest tests/
	@echo "$(GREEN)Tests complete.$(RESET)"

publish-test: build
	@echo "$(BLUE)Publishing to TestPyPI...$(RESET)"
	python -m pip install --upgrade twine
	python -m twine upload --repository testpypi dist/*
	@echo "$(GREEN)Published to TestPyPI.$(RESET)"

publish: build
	@echo "$(BLUE)Publishing to PyPI...$(RESET)"
	python -m pip install --upgrade twine
	python -m twine upload dist/*
	@echo "$(GREEN)Published to PyPI.$(RESET)"

# Default target
.DEFAULT_GOAL := help 