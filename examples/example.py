#!/usr/bin/env python3
"""A comprehensive example showing the capabilities of localStoragePro."""

import json
import time
from localStoragePro import localStoragePro

def basic_usage():
    """Basic usage example."""
    print("\n=== Basic Usage ===")
    
    # Initialize with SQLite backend (default)
    storage = localStoragePro('example.basic', 'sqlite')
    storage.clear()  # Start fresh
    
    # Store basic data
    storage.setItem('app_name', 'My App')
    storage.setItem('version', '1.0.0')
    storage.setItem('debug_mode', 'true')
    
    # Retrieve data
    app_name = storage.getItem('app_name')
    version = storage.getItem('version')
    print(f"App: {app_name} v{version}")
    
    # Remove data
    storage.removeItem('debug_mode')
    print(f"Debug mode (after removal): {storage.getItem('debug_mode')}")
    
    # Cleanup
    storage.clear()
    print("Basic storage cleared")

def json_data_handling():
    """JSON data handling example."""
    print("\n=== JSON Data Handling ===")
    
    # Initialize with JSON backend for readability
    storage = localStoragePro('example.json_data', 'json')
    storage.clear()
    
    # Create complex data structure
    user_profile = {
        "name": "Suraj Mandal",
        "email": "localstoragepro.oss@mandalsuraj.com",
        "preferences": {
            "theme": "dark",
            "language": "en",
            "notifications": True
        },
        "projects": ["localStoragePro", "Other Projects"],
        "stats": {
            "contributions": 256,
            "stars": 42
        }
    }
    
    # Store as JSON string
    storage.setItem('user_profile', json.dumps(user_profile))
    
    # Retrieve and parse
    retrieved_profile = json.loads(storage.getItem('user_profile'))
    print(f"User: {retrieved_profile['name']}")
    print(f"Email: {retrieved_profile['email']}")
    print(f"Theme: {retrieved_profile['preferences']['theme']}")
    print(f"Projects: {', '.join(retrieved_profile['projects'])}")
    
    # Cleanup
    storage.clear()
    print("JSON storage cleared")

def bulk_operations():
    """Bulk operations example."""
    print("\n=== Bulk Operations ===")
    
    storage = localStoragePro('example.bulk', 'sqlite')
    storage.clear()
    
    # Store multiple items
    test_data = {
        'name': 'Suraj Mandal',
        'email': 'localstoragepro.oss@mandalsuraj.com',
        'role': 'Developer',
        'location': 'India',
        'project': 'localStoragePro'
    }
    
    for key, value in test_data.items():
        storage.setItem(key, value)
    
    print(f"Stored {len(test_data)} items")
    
    # Get all data
    all_data = storage.getAll()
    print(f"Retrieved all data ({len(all_data)} items)")
    
    # Get specific keys
    subset_keys = ['name', 'email', 'project']
    subset_data = storage.getMany(subset_keys)
    print(f"Retrieved subset: {subset_data}")
    
    # Get with missing keys
    mixed_keys = ['name', 'nonexistent', 'project']
    mixed_data = storage.getMany(mixed_keys)
    print(f"Found keys: {list(mixed_data.keys())}")
    print(f"Missing keys: {set(mixed_keys) - set(mixed_data.keys())}")
    
    # Performance comparison
    print("\nPerformance comparison:")
    
    # Individual retrieval
    start_time = time.time()
    individual_results = {}
    for key in subset_keys:
        individual_results[key] = storage.getItem(key)
    individual_time = time.time() - start_time
    
    # Bulk retrieval
    start_time = time.time()
    bulk_results = storage.getMany(subset_keys)
    bulk_time = time.time() - start_time
    
    print(f"Individual getItem() calls: {individual_time*1000:.2f}ms")
    print(f"Single getMany() call: {bulk_time*1000:.2f}ms")
    if bulk_time > 0 and individual_time > 0:
        print(f"Bulk retrieval is {individual_time/bulk_time:.1f}x faster!")
    
    # Cleanup
    storage.removeAll()
    print("Bulk storage cleared")

def configuration_pattern():
    """Configuration pattern example."""
    print("\n=== Configuration Pattern ===")
    
    class AppConfig:
        def __init__(self, storage_namespace='example.config'):
            self.storage = localStoragePro(storage_namespace)
        
        def get_setting(self, key, default=None):
            value = self.storage.getItem(key)
            return value if value is not None else default
        
        def set_setting(self, key, value):
            self.storage.setItem(key, str(value))
        
        def get_all_settings(self):
            return self.storage.getAll()
        
        def reset_settings(self):
            self.storage.removeAll()
    
    # Use the configuration manager
    config = AppConfig()
    config.reset_settings()  # Start fresh
    
    # Set some configuration values
    config.set_setting('window_width', '1200')
    config.set_setting('window_height', '800')
    config.set_setting('auto_save', 'true')
    config.set_setting('theme', 'dark')
    
    # Retrieve settings
    width = config.get_setting('window_width')
    height = config.get_setting('window_height')
    print(f"Window size: {width}x{height}")
    print(f"Auto-save: {config.get_setting('auto_save')}")
    print(f"Theme: {config.get_setting('theme')}")
    
    # Default values for missing settings
    max_recent = config.get_setting('max_recent_files', '10')
    print(f"Max recent files: {max_recent} (default value)")
    
    # Get all settings
    all_settings = config.get_all_settings()
    print(f"Total settings: {len(all_settings)}")
    
    # Cleanup
    config.reset_settings()
    print("Config storage cleared")

def storage_backends_demo():
    """Storage backends demonstration."""
    print("\n=== Storage Backends ===")
    
    # SQLite backend (default)
    sqlite_storage = localStoragePro('example.backends.sqlite', 'sqlite')
    sqlite_storage.clear()
    sqlite_storage.setItem('backend', 'sqlite')
    print(f"SQLite backend: {sqlite_storage.getItem('backend')}")
    
    # JSON backend
    json_storage = localStoragePro('example.backends.json', 'json')
    json_storage.clear()
    json_storage.setItem('backend', 'json')
    print(f"JSON backend: {json_storage.getItem('backend')}")
    
    # Text backend
    text_storage = localStoragePro('example.backends.text', 'text')
    text_storage.clear()
    text_storage.setItem('backend', 'text')
    print(f"Text backend: {text_storage.getItem('backend')}")
    
    # Cleanup
    sqlite_storage.clear()
    json_storage.clear()
    text_storage.clear()
    print("All backend storages cleared")

def main():
    """Run all examples."""
    print("localStoragePro Examples")
    print("=" * 45)
    print("A lightweight, persistent local storage solution for Python")
    print("Maintainer: Suraj Mandal (localstoragepro.oss@mandalsuraj.com)")
    print("GitHub: https://github.com/surajmandalcell/localStoragePro")
    print("=" * 45)
    
    basic_usage()
    json_data_handling()
    bulk_operations()
    configuration_pattern()
    storage_backends_demo()
    
    print("\n" + "=" * 45)
    print("All examples completed successfully!")
    print("\nKey features demonstrated:")
    print("  • Basic storage operations (setItem, getItem, removeItem, clear)")
    print("  • Storing and retrieving complex data as JSON")
    print("  • Bulk operations (getAll, getMany, removeAll)")
    print("  • Application configuration pattern")
    print("  • Different storage backends (SQLite, JSON, Text)")
    print("\nFor more information, see the README.md file.")
    print("GitHub: https://github.com/surajmandalcell/localStoragePro")

if __name__ == "__main__":
    main() 