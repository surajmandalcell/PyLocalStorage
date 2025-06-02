<div align="center">

# localStoragePro

**A familiar localStorage API from the Web, adapted for Python applications**

*Simple, fast, and reliable local data storage with multiple backend options*

<br />

![PyPI](https://img.shields.io/pypi/v/localStoragePro.svg)
![License](https://img.shields.io/pypi/l/localStoragePro.svg)
![Downloads](https://img.shields.io/pypi/dm/localStoragePro.svg)
![Python](https://img.shields.io/pypi/pyversions/localStoragePro.svg)

</div>

---

## Features

- **Familiar API** - Web localStorage-like interface for Python
- **Multiple Backends** - Choose between SQLite, JSON, or Text storage
- **Bulk Operations** - Efficient `getAll()`, `getMany()`, and `removeAll()` methods
- **Async Support** - Both synchronous and asynchronous APIs available
- **Type Safe** - Full type annotations for better IDE support
- **Well Tested** - Comprehensive test coverage across all backends
- **Zero Dependencies** - Uses only Python standard library
- **Easy Setup** - Simple namespace-based storage organization

---

## Quick Start

### Installation

```bash
pip install localStoragePro
```

### Synchronous Usage

```python
from localStoragePro import lsp, localStoragePro

# Option 1: Using the convenient singleton instance
lsp('com.myapp.data').setItem('user_id', '12345')
user_id = lsp.getItem('user_id')  # Returns: '12345'

# Option 2: Creating your own instance
storage = localStoragePro('com.myapp.data')

# Store data (any serializable type)
storage.setItem('theme', 'dark')
storage.setItem('settings', '{"notifications": true}')

# Retrieve data
theme = storage.getItem('theme')      # Returns: 'dark'

# Remove items
storage.removeItem('theme')
print(storage.getItem('theme'))       # Returns: None

# Clear all data
storage.clear()
```

### Asynchronous Usage

```python
import asyncio
from localStoragePro import async_lsp, AsyncLocalStoragePro

async def main():
    # Option 1: Using the convenient singleton instance
    await async_lsp('com.myapp.data').setItem('user_id', '12345')
    user_id = await async_lsp.getItem('user_id')  # Returns: '12345'
    
    # Option 2: Creating your own instance
    storage = AsyncLocalStoragePro('com.myapp.data')
    
    # Store data asynchronously
    await storage.setItem('theme', 'dark')
    await storage.setItem('settings', '{"notifications": true}')
    
    # Retrieve data
    theme = await storage.getItem('theme')  # Returns: 'dark'
    
    # Remove items
    await storage.removeItem('theme')
    
    # Concurrent operations
    tasks = [
        storage.setItem('key1', 'value1'),
        storage.setItem('key2', 'value2'),
        storage.setItem('key3', 'value3')
    ]
    await asyncio.gather(*tasks)
    
    # Bulk retrieval
    all_data = await storage.getAll()
    
    # Clear all data
    await storage.clear()

# Run the async example
asyncio.run(main())
```

---

## Storage Backends

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

## Requirements

- Python 3.9 or higher (for `asyncio.to_thread()` support)
- No external dependencies

---

## Bulk Operations

Efficiently work with multiple keys at once:

<details>
<summary><strong>Click to see bulk operations examples</strong></summary>

```python
from localStoragePro import lsp

# Set up some data
lsp('bulk_demo').setItem('name', 'Suraj Mandal')
lsp.setItem('email', 'localstoragepro.oss@mandalsuraj.com')
lsp.setItem('role', 'Developer')
lsp.setItem('location', 'India')

# Get all stored data
all_data = lsp.getAll()
print(all_data)
# {'name': 'Suraj Mandal', 'email': 'localstoragepro.oss@mandalsuraj.com', 'role': 'Developer', 'location': 'India'}

# Get specific keys only
user_info = lsp.getMany(['name', 'email'])
print(user_info)
# {'name': 'Suraj Mandal', 'email': 'localstoragepro.oss@mandalsuraj.com'}

# Remove all data at once
lsp.removeAll()
print(len(lsp.getAll()))  # 0
```

</details>

---

## API Reference

<details>
<summary><strong>Click to see all available methods</strong></summary>

### Synchronous API

| Method | Description | Returns |
|--------|-------------|---------|
| `setItem(key, value)` | Store a value with the given key | `None` |
| `getItem(key)` | Retrieve value by key | `str \| None` |
| `removeItem(key)` | Remove item by key | `None` |
| `getAll()` | Get all key-value pairs | `Dict[str, str]` |
| `getMany(keys)` | Get multiple values by keys | `Dict[str, str]` |
| `removeAll()` | Remove all items | `None` |
| `clear()` | Clear all stored data (alias for removeAll) | `None` |

### Asynchronous API

| Method | Description | Returns |
|--------|-------------|---------|
| `async setItem(key, value)` | Store a value with the given key | `None` |
| `async getItem(key)` | Retrieve value by key | `str \| None` |
| `async removeItem(key)` | Remove item by key | `None` |
| `async getAll()` | Get all key-value pairs | `Dict[str, str]` |
| `async getMany(keys)` | Get multiple values by keys | `Dict[str, str]` |
| `async removeAll()` | Remove all items | `None` |
| `async clear()` | Clear all stored data (alias for removeAll) | `None` |

### Type Signatures

```python
# Synchronous API
from typing import Dict, List, Optional, Any

def setItem(self, key: str, value: Any) -> None: ...
def getItem(self, key: str) -> Optional[str]: ...
def removeItem(self, key: str) -> None: ...
def getAll(self) -> Dict[str, str]: ...
def getMany(self, keys: List[str]) -> Dict[str, str]: ...
def removeAll(self) -> None: ...
def clear(self) -> None: ...

# Asynchronous API
async def setItem(self, key: str, value: Any) -> None: ...
async def getItem(self, key: str) -> Optional[str]: ...
async def removeItem(self, key: str) -> None: ...
async def getAll(self) -> Dict[str, str]: ...
async def getMany(self, keys: List[str]) -> Dict[str, str]: ...
async def removeAll(self) -> None: ...
async def clear(self) -> None: ...
```

</details>

---

## Examples

### Working with JSON Data

```python
import json
from localStoragePro import lsp

# Store complex data as JSON
user_profile = {
    "name": "Suraj Mandal",
    "preferences": {"theme": "dark", "language": "en"},
    "projects": ["localStoragePro", "Other Projects"]
}

lsp('json_example').setItem('profile', json.dumps(user_profile))

# Retrieve and parse JSON
profile_data = json.loads(lsp.getItem('profile'))
print(profile_data['name'])  # "Suraj Mandal"
```

### Asynchronous Operations

```python
import asyncio
import json
from localStoragePro import async_lsp

async def main():
    # Store multiple items concurrently
    tasks = [
        async_lsp('async_example').setItem('key1', 'value1'),
        async_lsp.setItem('key2', 'value2'),
        async_lsp.setItem('key3', 'value3')
    ]
    await asyncio.gather(*tasks)
    
    # Retrieve all data
    data = await async_lsp.getAll()
    print(f"Stored {len(data)} items")
    
    # Bulk retrieval is more efficient
    subset = await async_lsp.getMany(['key1', 'key3'])
    print(subset)  # {'key1': 'value1', 'key3': 'value3'}

asyncio.run(main())
```

### Configuration Management

```python
from localStoragePro import lsp

lsp('myapp.config').setItem('db_host', 'localhost')
lsp.setItem('db_port', '5432')
lsp.setItem('debug_mode', 'true')
lsp.setItem('log_level', 'INFO')

# Load all config at startup
app_config = lsp.getAll()
print(f"Connecting to {app_config['db_host']}:{app_config['db_port']}")
```

---

## Error Handling

localStoragePro gracefully handles common error scenarios:

```python
from localStoragePro import lsp

# Getting non-existent keys returns None
result = lsp('error_handling_demo').getItem('does_not_exist')
print(result)  # None

# Getting many with mixed existing/non-existing keys
result = lsp.getMany(['exists', 'does_not_exist', 'also_exists'])
print(result)  # Only returns existing keys

# Removing non-existent keys doesn't raise errors
lsp.removeItem('does_not_exist')  # Safe operation

# Multiple removeAll() calls are safe
lsp.removeAll()
lsp.removeAll()  # No error
```

---

## Contributing

We welcome contributions! Here's how you can help:

1. **Report Bugs** - [Open an issue](https://github.com/surajmandalcell/localStoragePro/issues)
2. **Suggest Features** - [Start a discussion](https://github.com/surajmandalcell/localStoragePro/discussions)
3. **Submit PRs** - Fork, code, test, and submit!

### Development Setup

```bash
# Clone the repository
git clone https://github.com/surajmandalcell/localStoragePro.git
cd localStoragePro

# Install development dependencies
make install-dev

# Run tests
make test

# Build package
make build

# Run examples
python examples/example.py
python examples/async_example.py  # Requires Python 3.9+
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Forked from [localStoragePy](https://github.com/sunsetsonwheels/localStoragePy) by [sunsetsonwheels](https://github.com/sunsetsonwheels)
- Maintained by [Suraj Mandal](https://github.com/surajmandalcell)
- Built for the Python community

---
<br>
<div align="center">
  
**[Star this repo](https://github.com/surajmandalcell/localStoragePro)** if you find it useful!

Shamelessly VibeCoded by [Suraj Mandal](https://github.com/surajmandalcell)

</div>
