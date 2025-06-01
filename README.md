# LocalStoragePro
![PyPI](https://img.shields.io/pypi/v/localStoragePy.svg?style=flat-square) ![GitHub issues](https://img.shields.io/github/issues-raw/surajmandalcell/LocalStoragePro.svg?style=flat-square) ![PyPI - License](https://img.shields.io/pypi/l/localStoragePy.svg?style=flat-square)

A familiar API from the Web, adapted to storing data locally with Python. Enhanced with additional functionality for working with multiple keys and values.

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

# Retrieve a value
username = localStorage.getItem('username')  # Returns 'surajmandal'

# Remove a value
localStorage.removeItem('theme')

# Clear all stored data
localStorage.clear()
```

### Advanced Operations

```python
from localStoragePy import localStoragePy

localStorage = localStoragePy('com.surajmandal.myapp')

# Store multiple values
localStorage.setItem('user_id', '12345')
localStorage.setItem('email', 'contact@surajmandal.com')
localStorage.setItem('preferences', '{"notifications": true, "darkMode": true}')

# Get all stored key-value pairs
all_data = localStorage.getAll()  # Returns dict with all key-value pairs

# Get multiple specific values
user_data = localStorage.getMany(['user_id', 'email'])  # Returns dict with specified keys

# Remove all stored data (alternative to clear)
localStorage.removeAll()
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
    'notifications': True
}
localStorage.setItem('settings', json.dumps(user_settings))

# Retrieve and parse JSON data
settings_json = localStorage.getItem('settings')
settings = json.loads(settings_json)
print(f"Theme: {settings['theme']}")
```

## Available Methods

- `getItem(key)`: Retrieve a single value by key
- `setItem(key, value)`: Store a value with the given key
- `removeItem(key)`: Remove a single key-value pair
- `getAll()`: Retrieve all stored key-value pairs as a dictionary
- `getMany(keys)`: Retrieve multiple values by providing a list of keys
- `removeAll()`: Remove all stored data (similar to clear)
- `clear()`: Clear all stored data

## When is this useful?

- When you want to store configuration for your app
- When you need a simple key-value store without setting up a database
- For storing user preferences and settings
- As a lightweight data persistence solution for small applications

## Contributing

Feel free to open issues or submit pull requests on GitHub: https://github.com/surajmandalcell/LocalStoragePro

## License

MIT License
