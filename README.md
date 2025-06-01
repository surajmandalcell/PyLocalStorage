# 🗄️ localStoragePro

<div align="center">

![PyPI](https://img.shields.io/pypi/v/localStoragePro.svg?style=for-the-badge&logo=pypi&logoColor=white)
![Python](https://img.shields.io/pypi/pyversions/localStoragePro.svg?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/pypi/l/localStoragePro.svg?style=for-the-badge)
![Downloads](https://img.shields.io/pypi/dm/localStoragePro.svg?style=for-the-badge&logo=python&logoColor=white)

**A familiar localStorage API from the Web, adapted for Python applications** 🐍

*Simple, fast, and reliable local data storage with multiple backend options*

</div>

---

## ✨ Features

- 🌐 **Familiar API** - Web localStorage-like interface for Python
- 🚀 **Multiple Backends** - Choose between SQLite, JSON, or Text storage
- ⚡ **Bulk Operations** - Efficient `getAll()`, `getMany()`, and `removeAll()` methods
- 🔒 **Type Safe** - Full type annotations for better IDE support
- 🧪 **Well Tested** - Comprehensive test coverage across all backends
- 📦 **Zero Dependencies** - Uses only Python standard library
- 🔧 **Easy Setup** - Simple namespace-based storage organization

---

## 🚀 Quick Start

### Installation

```bash
pip install localStoragePro
```

### Basic Usage

```python
from localStoragePro import localStoragePro

# Initialize with your app namespace
storage = localStoragePro('com.myapp.data')

# Store data (any serializable type)
storage.setItem('user_id', '12345')
storage.setItem('theme', 'dark')
storage.setItem('settings', '{"notifications": true}')

# Retrieve data
user_id = storage.getItem('user_id')  # Returns: '12345'
theme = storage.getItem('theme')      # Returns: 'dark'

# Remove items
storage.removeItem('theme')
print(storage.getItem('theme'))       # Returns: None

# Clear all data
storage.clear()
```

---

## 🎯 Storage Backends

Choose the backend that fits your needs:

| Backend | Best For | Pros | Cons |
|---------|----------|------|------|
| **`sqlite`** *(default)* | Most applications | Fast, ACID compliant, handles large datasets | Single file dependency |
| **`json`** | Simple apps, human-readable data | Readable, easy debugging | Can be slower for large datasets |
| **`text`** | Key-value files | Individual files per key, simple | Many files, slower for bulk operations |

```python
# Choose your backend
storage_sqlite = localStoragePro('myapp', 'sqlite')  # Default
storage_json = localStoragePro('myapp', 'json')      # Human-readable
storage_text = localStoragePro('myapp', 'text')      # Individual files
```

---

## ⚡ Bulk Operations

Efficiently work with multiple keys at once:

<details>
<summary><strong>🔽 Click to see bulk operations examples</strong></summary>

```python
from localStoragePro import localStoragePro

storage = localStoragePro('bulk_demo')

# Set up some data
storage.setItem('name', 'Suraj Mandal')
storage.setItem('email', 'localstoragepro.oss@mandalsuraj.com')
storage.setItem('role', 'Developer')
storage.setItem('location', 'India')

# Get all stored data
all_data = storage.getAll()
print(all_data)
# {'name': 'Suraj Mandal', 'email': 'localstoragepro.oss@mandalsuraj.com', 'role': 'Developer', 'location': 'India'}

# Get specific keys only
user_info = storage.getMany(['name', 'email'])
print(user_info)
# {'name': 'Suraj Mandal', 'email': 'localstoragepro.oss@mandalsuraj.com'}

# Remove all data at once
storage.removeAll()
print(len(storage.getAll()))  # 0
```

</details>

---

## 📖 Complete API Reference

<details>
<summary><strong>🔽 Click to see all available methods</strong></summary>

### Core Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `setItem(key, value)` | Store a value with the given key | `None` |
| `getItem(key)` | Retrieve value by key | `str \| None` |
| `removeItem(key)` | Remove item by key | `None` |
| `clear()` | Remove all stored data | `None` |

### Bulk Methods ⚡

| Method | Description | Returns |
|--------|-------------|---------|
| `getAll()` | Get all key-value pairs | `Dict[str, str]` |
| `getMany(keys)` | Get multiple values by keys | `Dict[str, str]` |
| `removeAll()` | Remove all items (alias for `clear()`) | `None` |

### Type Signatures

```python
from typing import Dict, List, Optional

def setItem(self, key: str, value: Any) -> None: ...
def getItem(self, key: str) -> Optional[str]: ...
def removeItem(self, key: str) -> None: ...
def getAll(self) -> Dict[str, str]: ...
def getMany(self, keys: List[str]) -> Dict[str, str]: ...
def removeAll(self) -> None: ...
def clear(self) -> None: ...
```

</details>

---

## 🧪 Examples

### Working with JSON Data

```python
import json
from localStoragePro import localStoragePro

storage = localStoragePro('json_example')

# Store complex data as JSON
user_profile = {
    "name": "Suraj Mandal",
    "preferences": {"theme": "dark", "language": "en"},
    "projects": ["localStoragePro", "Other Projects"]
}

storage.setItem('profile', json.dumps(user_profile))

# Retrieve and parse JSON
profile_data = json.loads(storage.getItem('profile'))
print(profile_data['name'])  # "Suraj Mandal"
```

### Configuration Management

```python
from localStoragePro import localStoragePro

config = localStoragePro('myapp.config')

# Store app configuration
config.setItem('db_host', 'localhost')
config.setItem('db_port', '5432')
config.setItem('debug_mode', 'true')
config.setItem('log_level', 'INFO')

# Load all config at startup
app_config = config.getAll()
print(f"Connecting to {app_config['db_host']}:{app_config['db_port']}")
```

### Performance Comparison

```python
import time
from localStoragePro import localStoragePro

storage = localStoragePro('performance_test')

# Setup test data
for i in range(100):
    storage.setItem(f'item_{i}', f'value_{i}')

keys_to_fetch = [f'item_{i}' for i in range(0, 100, 10)]

# Individual fetches
start = time.time()
individual_results = {key: storage.getItem(key) for key in keys_to_fetch}
individual_time = time.time() - start

# Bulk fetch
start = time.time() 
bulk_results = storage.getMany(keys_to_fetch)
bulk_time = time.time() - start

print(f"Individual: {individual_time:.4f}s")
print(f"Bulk: {bulk_time:.4f}s")
print(f"Speedup: {individual_time/bulk_time:.1f}x faster")
```

---

## 🛡️ Error Handling

localStoragePro gracefully handles common error scenarios:

```python
from localStoragePro import localStoragePro

storage = localStoragePro('error_handling_demo')

# Getting non-existent keys returns None
result = storage.getItem('does_not_exist')
print(result)  # None

# Getting many with mixed existing/non-existing keys
result = storage.getMany(['exists', 'does_not_exist', 'also_exists'])
print(result)  # Only returns existing keys

# Removing non-existent keys doesn't raise errors
storage.removeItem('does_not_exist')  # Safe operation

# Multiple removeAll() calls are safe
storage.removeAll()
storage.removeAll()  # No error
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **🐛 Report Bugs** - [Open an issue](https://github.com/surajmandalcell/localStoragePro/issues)
2. **💡 Suggest Features** - [Start a discussion](https://github.com/surajmandalcell/localStoragePro/discussions)
3. **🔧 Submit PRs** - Fork, code, test, and submit!

### Development Setup

```bash
# Clone the repository
git clone https://github.com/surajmandalcell/localStoragePro.git
cd localStoragePro

# Run tests
python -m pytest tests/

# Run examples
python examples/example_demo.py
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Original concept inspired by Web localStorage API
- Maintained by [Suraj Mandal](https://github.com/surajmandalcell)
- Built with ❤️ for the Python community

---

<div align="center">

**[⭐ Star this repo](https://github.com/surajmandalcell/localStoragePro)** if you find it useful!

Made with ❤️ by [Suraj Mandal](https://github.com/surajmandalcell)

</div>
