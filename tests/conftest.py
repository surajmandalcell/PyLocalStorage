"""
Pytest configuration for  tests.
"""

import sys
import os
from pathlib import Path

# Add src directory to Python path
root_dir = Path(__file__).parent.parent
src_dir = root_dir / "src"
sys.path.insert(0, str(src_dir))

import pytest


@pytest.fixture(scope="session")
def test_namespace():
    """Provide a unique namespace for tests."""
    return "test..pytest"


@pytest.fixture(autouse=True)
def cleanup_test_storage():
    """Clean up test storage after each test."""
    yield
    # Cleanup logic could go here if needed
