#!/usr/bin/env python3
"""
localStoragePro Quick Start Example

A simple example showing the most common use cases of localStoragePro.

Author: Suraj Mandal
GitHub: https://github.com/surajmandalcell/localStoragePro
"""

import json
from localStoragePro import localStoragePro


def main():
    print("🗄️ localStoragePro Quick Start Example")
    print("=" * 45)
    
    # Initialize storage (SQLite backend by default)
    print("1. Initializing storage...")
    storage = localStoragePro('quickstart.example')
    
    # Clear any existing data for clean demo
    storage.clear()
    print("   ✓ Storage initialized and cleared")
    
    # Basic operations
    print("\n2. Basic operations:")
    storage.setItem('app_name', 'My Awesome App')
    storage.setItem('version', '1.0.0')
    storage.setItem('debug_mode', 'true')
    
    app_name = storage.getItem('app_name')
    version = storage.getItem('version')
    print(f"   App: {app_name} v{version}")
    
    # JSON data storage
    print("\n3. Storing complex data as JSON:")
    user_config = {
        'username': 'surajmandal',
        'preferences': {
            'theme': 'dark',
            'language': 'en',
            'notifications': True
        },
        'recent_files': [
            'project1.py',
            'script.py',
            'data.json'
        ]
    }
    
    storage.setItem('user_config', json.dumps(user_config))
    
    # Retrieve and use JSON data
    retrieved_config = json.loads(storage.getItem('user_config'))
    print(f"   User: {retrieved_config['username']}")
    print(f"   Theme: {retrieved_config['preferences']['theme']}")
    print(f"   Recent files: {len(retrieved_config['recent_files'])} files")
    
    # Bulk operations
    print("\n4. Bulk operations:")
    
    # Add more sample data
    storage.setItem('last_login', '2025-06-01T10:30:00Z')
    storage.setItem('session_count', '42')
    storage.setItem('feature_flags', '{"new_ui": true, "beta_features": false}')
    
    # Get all data
    all_data = storage.getAll()
    print(f"   Total stored items: {len(all_data)}")
    
    # Get specific items efficiently
    app_info = storage.getMany(['app_name', 'version', 'debug_mode'])
    print(f"   App info: {app_info}")
    
    # Configuration management example
    print("\n5. Configuration management pattern:")
    
    class AppConfig:
        def __init__(self, storage_namespace='myapp.config'):
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
    config.set_setting('window_width', '1200')
    config.set_setting('window_height', '800')
    config.set_setting('auto_save', 'true')
    
    print(f"   Window size: {config.get_setting('window_width')}x{config.get_setting('window_height')}")
    print(f"   Auto-save: {config.get_setting('auto_save')}")
    print(f"   Unknown setting: {config.get_setting('unknown', 'default_value')}")
    
    # Data persistence verification
    print("\n6. Data persistence verification:")
    
    # Create new storage instance with same namespace
    storage2 = localStoragePro('quickstart.example')
    persisted_app_name = storage2.getItem('app_name')
    print(f"   Data persisted across instances: {persisted_app_name}")
    
    # Cleanup
    print("\n7. Cleanup:")
    storage.removeAll()
    print(f"   Items after cleanup: {len(storage.getAll())}")
    
    print("\n" + "=" * 45)
    print("✅ Quick start example completed!")
    print("\nKey takeaways:")
    print("  • Use setItem()/getItem() for basic storage")
    print("  • Store complex data as JSON strings")
    print("  • Use bulk operations for efficiency")
    print("  • Data persists across application restarts")
    print("  • Choose appropriate storage backend for your needs")
    print("\nNext steps:")
    print("  • Check out the comprehensive demo: python examples/example_demo.py")
    print("  • Read the full documentation: https://github.com/surajmandalcell/localStoragePro")


if __name__ == "__main__":
    main()
