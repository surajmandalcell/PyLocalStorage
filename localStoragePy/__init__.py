__author__ = 'Suraj Mandal'
__copyright__ = 'Copyright (C) 2021-present Suraj Mandal'
__license__ = 'MIT License'
__version__ = '0.3.0'

from typing import Any
from .storage_backends import BasicStorageBackend, TextStorageBackend, SQLiteStorageBackend, JSONStorageBackend

__all__ = ['localStoragePy']

class localStoragePy:
    """
    A familiar API from the Web, adapted to storing data locally with Python.
    
    This class provides a localStorage-like interface for persisting key-value data
    using various storage backends (SQLite, JSON, or text files).
    
    Args:
        app_namespace (str): A unique identifier for your application (e.g., 'com.mycompany.myapp').
                           Must not contain path separators.
        storage_backend (str): Storage backend to use. Options: 'sqlite' (default), 'json', 'text'.
    
    Examples:
        Basic usage:
        >>> localStorage = localStoragePy('com.example.myapp')
        >>> localStorage.setItem('username', 'john_doe')
        >>> localStorage.getItem('username')
        'john_doe'
        
        Using different backend:
        >>> localStorage = localStoragePy('com.example.myapp', 'json')
        
        Bulk operations:
        >>> localStorage.setItem('name', 'John')
        >>> localStorage.setItem('email', 'john@example.com')
        >>> localStorage.getAll()
        {'name': 'John', 'email': 'john@example.com'}
        >>> localStorage.getMany(['name', 'email'])
        {'name': 'John', 'email': 'john@example.com'}
    """
    
    def __init__(self, app_namespace: str, storage_backend: str = "sqlite") -> None:
        """
        Initialize localStoragePy with the specified namespace and backend.
        
        Args:
            app_namespace (str): Unique namespace for your application
            storage_backend (str): Backend type ('sqlite', 'json', or 'text')
        """
        self.storage_backend_instance = BasicStorageBackend(app_namespace)
        if storage_backend == "text":
            self.storage_backend_instance = TextStorageBackend(app_namespace)
        elif storage_backend == "sqlite":
            self.storage_backend_instance = SQLiteStorageBackend(app_namespace)
        elif storage_backend == "json":
            self.storage_backend_instance = JSONStorageBackend(app_namespace)
        else:
            self.storage_backend_instance = SQLiteStorageBackend(app_namespace)

    def getItem(self, item: str) -> Any:
        """
        Retrieve a value by its key.
        
        Args:
            item (str): The key to retrieve.
            
        Returns:
            str | None: The stored value as a string, or None if the key doesn't exist.
        """
        return self.storage_backend_instance.get_item(item)

    def setItem(self, item: str, value: Any) -> None:
        """
        Store a value with the given key.
        
        Args:
            item (str): The key to store the value under.
            value (Any): The value to store (will be converted to string).
        """
        self.storage_backend_instance.set_item(item, value)

    def removeItem(self, item: str) -> None:
        """
        Remove a key-value pair.
        
        Args:
            item (str): The key to remove.
        """
        self.storage_backend_instance.remove_item(item)

    def getAll(self) -> dict:
        """
        Retrieve all stored key-value pairs.
        
        Returns:
            dict: A dictionary containing all stored key-value pairs.
        """
        return self.storage_backend_instance.get_all()

    def getMany(self, items: list) -> dict:
        """
        Retrieve multiple values by their keys.
        
        Args:
            items (list): A list of keys to retrieve.
            
        Returns:
            dict: A dictionary containing only the keys that exist in storage.
        """
        return self.storage_backend_instance.get_many(items)

    def removeAll(self) -> None:
        """
        Remove all stored key-value pairs.
        
        This method clears all data from storage.
        """
        self.storage_backend_instance.remove_all()

    def clear(self) -> None:
        """
        Clear all stored data (equivalent to removeAll).
        
        This method provides the familiar web localStorage.clear() API.
        """
        self.storage_backend_instance.clear()

