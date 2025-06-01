# LocalStoragePro
![PyPI](https://img.shields.io/pypi/v/localStoragePy.svg?style=flat-square) ![GitHub issues](https://img.shields.io/github/issues-raw/surajmandalcell/LocalStoragePro.svg?style=flat-square) ![PyPI - License](https://img.shields.io/pypi/l/localStoragePy.svg?style=flat-square)

A familiar API from the Web, adapted to storing data locally with Python. Enhanced with additional functionality for working with multiple keys and values.

**Maintained by [Suraj Mandal](https://github.com/surajmandalcell)**

## Get started

1. Install using PyPi: `$ pip3 install localStoragePy`

2. Import into your project: `from localStoragePy import localStoragePy`

3. Setup localStorage: `localStorage = localStoragePy('your-app-namespace', 'your-storage-backend')` 

- `your-app-namespace`: whatever you want (example: `com.surajmandal.myapp`) excluding path separators `/ \` or other disallowed characters in file name for your intended platform

- `your-storage-backend`: your preferred storage backend (`sqlite` by default).
    - Available storage backends:
        - `text`: text files for each storage item.
        - `sqlite`: a single database for all storage items.
        - `json`: a single JSON file for all storage items.

## Usage Examples

### Basic Operations

```python
from localStoragePy import localStoragePy

# Initialize with namespace and backend (sqlite is default)
localStorage = localStoragePy('com.surajmandal.myapp', 'json')

# Store values
localStorage.setItem('username', 'surajmandal')
localStorage.setItem('theme', 'dark')
localStorage.setItem('language', 'en')
localStorage.setItem('version', '1.0.0')

# Retrieve a single value
username = localStorage.getItem('username')  # Returns 'surajmandal'
print(f"Username: {username}")

# Check if item exists (returns None if not found)
nonexistent = localStorage.getItem('nonexistent')  # Returns None
if nonexistent is None:
    print("Item not found")

# Remove a single item
localStorage.removeItem('theme')

# Clear all stored data
localStorage.clear()
```

### Advanced Operations - Working with Multiple Items

```python
from localStoragePy import localStoragePy

localStorage = localStoragePy('com.surajmandal.myapp')

# Store multiple values
localStorage.setItem('user_id', '12345')
localStorage.setItem('email', 'contact@surajmandal.com')
localStorage.setItem('first_name', 'Suraj')
localStorage.setItem('last_name', 'Mandal')
localStorage.setItem('role', 'developer')
localStorage.setItem('preferences', '{"notifications": true, "darkMode": true}')

# Get all stored key-value pairs
all_data = localStorage.getAll()
print("All stored data:")
for key, value in all_data.items():
    print(f"  {key}: {value}")

# Get multiple specific values
user_info = localStorage.getMany(['user_id', 'email', 'first_name', 'last_name'])
print("\nUser information:")
for key, value in user_info.items():
    print(f"  {key}: {value}")

# Get values that may or may not exist
mixed_keys = localStorage.getMany(['user_id', 'nonexistent_key', 'email'])
print(f"\nMixed query result: {mixed_keys}")  # Only existing keys are returned

# Remove all stored data (alternative to clear)
localStorage.removeAll()

# Verify all data is removed
remaining_data = localStorage.getAll()
print(f"Remaining data after removeAll(): {remaining_data}")  # Should be empty dict {}
```

### Working with JSON Data

```python
import json
from localStoragePy import localStoragePy

localStorage = localStoragePy('com.surajmandal.myapp', 'json')

# Store complex data as JSON string
user_settings = {
    'theme': 'dark',
    'fontSize': 14,
    'notifications': True,
    'shortcuts': ['Ctrl+S', 'Ctrl+C', 'Ctrl+V']
}
localStorage.setItem('settings', json.dumps(user_settings))

# Store user profile
user_profile = {
    'name': 'Suraj Mandal',
    'email': 'contact@surajmandal.com',
    'github': 'https://github.com/surajmandalcell',
    'projects': ['LocalStoragePro', 'Other Projects']
}
localStorage.setItem('profile', json.dumps(user_profile))

# Retrieve and parse JSON data
settings_json = localStorage.getItem('settings')
if settings_json:
    settings = json.loads(settings_json)
    print(f"Theme: {settings['theme']}")
    print(f"Font Size: {settings['fontSize']}")
    print(f"Notifications: {settings['notifications']}")

# Get multiple JSON objects at once
json_data = localStorage.getMany(['settings', 'profile'])
for key, value in json_data.items():
    parsed_data = json.loads(value)
    print(f"\n{key.title()}:")
    if isinstance(parsed_data, dict):
        for k, v in parsed_data.items():
            print(f"  {k}: {v}")
```

### Storage Backend Comparison

```python
from localStoragePy import localStoragePy
import time

# Test different backends
backends = ['text', 'sqlite', 'json']

for backend in backends:
    print(f"\n--- Testing {backend.upper()} Backend ---")
    localStorage = localStoragePy(f'test.{backend}', backend)
    
    # Store test data
    localStorage.setItem('name', 'Suraj Mandal')
    localStorage.setItem('project', 'LocalStoragePro')
    localStorage.setItem('language', 'Python')
    
    # Retrieve all data
    all_data = localStorage.getAll()
    print(f"Stored {len(all_data)} items: {list(all_data.keys())}")
    
    # Test getMany
    subset = localStorage.getMany(['name', 'project'])
    print(f"Retrieved subset: {subset}")
    
    # Clean up
    localStorage.removeAll()
    print(f"Cleaned up - remaining items: {len(localStorage.getAll())}")
```

### Error Handling and Best Practices

```python
from localStoragePy import localStoragePy

try:
    # Initialize with a valid namespace
    localStorage = localStoragePy('com.surajmandal.myapp', 'sqlite')
    
    # Store some data
    localStorage.setItem('config', 'some_config_value')
    
    # Always check if data exists before using it
    config = localStorage.getItem('config')
    if config is not None:
        print(f"Config found: {config}")
    else:
        print("No config found, using defaults")
    
    # Use getMany for efficient bulk retrieval
    required_keys = ['api_key', 'user_token', 'refresh_token']
    tokens = localStorage.getMany(required_keys)
    
    missing_keys = set(required_keys) - set(tokens.keys())
    if missing_keys:
        print(f"Missing required keys: {missing_keys}")
    else:
        print("All required tokens found")
        
except Exception as e:
    print(f"Storage error: {e}")
```

## Available Methods

### Core Methods
- `getItem(key)` → `str | None`: Retrieve a single value by key. Returns `None` if key doesn't exist.
- `setItem(key, value)` → `None`: Store a value with the given key. Value is converted to string.
- `removeItem(key)` → `None`: Remove a single key-value pair.
- `clear()` → `None`: Clear all stored data.

### Bulk Operations
- `getAll()` → `dict`: Retrieve all stored key-value pairs as a dictionary.
- `getMany(keys)` → `dict`: Retrieve multiple values by providing a list of keys. Only returns existing keys.
- `removeAll()` → `None`: Remove all stored data (equivalent to `clear()`).

### Method Details

#### `getItem(key: str) -> str | None`
```python
# Returns the value as a string, or None if not found
value = localStorage.getItem('username')
if value is not None:
    print(f"Found: {value}")
```

#### `setItem(key: str, value: any) -> None`
```python
# All values are converted to strings before storage
localStorage.setItem('count', 42)  # Stored as '42'
localStorage.setItem('config', json.dumps({'theme': 'dark'}))  # Store complex data as JSON
```

#### `getAll() -> dict`
```python
# Returns all key-value pairs
all_data = localStorage.getAll()
print(f"Total items: {len(all_data)}")
for key, value in all_data.items():
    print(f"{key}: {value}")
```

#### `getMany(keys: list) -> dict`
```python
# Only returns keys that exist in storage
requested = ['name', 'email', 'nonexistent']
found = localStorage.getMany(requested)
# found will only contain 'name' and 'email' if they exist
```

#### `removeAll()` vs `clear()`
Both methods do the same thing - remove all stored data. Use whichever feels more natural:
```python
localStorage.removeAll()  # More explicit about removing items
localStorage.clear()      # Familiar from web localStorage API
```

## Storage Backends

LocalStoragePro supports multiple storage backends, each with different characteristics:

### SQLite Backend (Default - Recommended)
```python
localStorage = localStoragePy('myapp', 'sqlite')
```
- **File**: Single `.db` file in the storage directory
- **Performance**: Fast for all operations, especially bulk operations
- **Durability**: ACID compliant, handles concurrent access well
- **Use case**: Most applications, especially those requiring reliability

### JSON Backend
```python
localStorage = localStoragePy('myapp', 'json')
```
- **File**: Single `.json` file in the storage directory
- **Performance**: Good for small to medium datasets
- **Durability**: Simple file-based storage, entire file rewritten on each change
- **Use case**: Applications that need human-readable storage files

### Text Backend
```python
localStorage = localStoragePy('myapp', 'text')
```
- **File**: Separate text file for each key
- **Performance**: Slower for bulk operations, good for individual access
- **Durability**: Each key is a separate file
- **Use case**: Simple applications, debugging, or when you need individual file access

### Storage Location
All backends store data in: `~/.config/localStoragePy/<your-app-namespace>/`

## When is this useful?

- **Configuration Management**: Store app settings, user preferences, and configuration data
- **Simple Data Persistence**: Lightweight alternative to setting up a full database
- **Caching**: Store computed results, API responses, or temporary data
- **User Preferences**: Remember user choices, themes, and personalization settings
- **Development**: Quick prototyping without database setup
- **Cross-platform Storage**: Consistent API across Windows, macOS, and Linux

## Contributing

This project is maintained by [Suraj Mandal](https://github.com/surajmandalcell). Contributions are welcome!

### How to Contribute
1. Fork the repository: https://github.com/surajmandalcell/LocalStoragePro
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Submit a pull request

### Development Setup
```bash
git clone https://github.com/surajmandalcell/LocalStoragePro.git
cd LocalStoragePro
pip install -e .
```

### Reporting Issues
Found a bug or have a feature request? Please open an issue on GitHub:
https://github.com/surajmandalcell/LocalStoragePro/issues

## License

MIT License
