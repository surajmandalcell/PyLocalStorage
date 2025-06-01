"""
Pytest configuration for tests.
"""

import pytest


@pytest.fixture(scope="session")
def test_namespace():
    """Provide a unique namespace for tests."""
    return "test.pytest"


@pytest.fixture(autouse=True)
def cleanup_test_storage():
    """Clean up test storage after each test."""
    yield
    # Cleanup logic could go here if needed
