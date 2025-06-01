# Changelog

All notable changes to LocalStoragePro will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2025-06-01

### Added
- **New bulk operations for improved performance:**
  - `getAll()` - Retrieve all stored key-value pairs at once
  - `getMany(keys)` - Efficiently retrieve multiple values in a single call
  - `removeAll()` - Remove all stored data across all backends
- **Enhanced type annotations** throughout the codebase for better IDE support
- **Comprehensive documentation** with complete code examples in README.md
- **Example scripts** demonstrating new functionality:
  - `example_demo.py` - Interactive demo of all new features
  - `test_complete.py` - Comprehensive test suite for all backends
  - `test_simple.py` - Quick functionality verification
- **Performance optimizations** for bulk operations, especially in SQLite backend

### Changed
- **Project ownership transferred to Suraj Mandal**
  - Updated GitHub repository URL to: https://github.com/surajmandalcell/LocalStoragePro
  - Changed author information in setup.py and documentation
  - Updated contact information and contributing guidelines
- **Improved storage backend consistency** across all implementations
- **Enhanced error handling** for edge cases and invalid operations
- **Better parameter naming consistency** across all methods

### Enhanced
- **README.md completely rewritten** with:
  - Multiple practical usage examples
  - Detailed method documentation with type signatures
  - Storage backend comparison and recommendations
  - Error handling best practices
  - Contributing guidelines with new maintainer details
- **Type annotations** added throughout codebase:
  - All method signatures include proper typing
  - Import statements updated with necessary type imports
  - Return types and parameter types clearly specified
- **Documentation strings** enhanced for all public methods

### Technical Improvements
- **Storage backend implementations** unified and optimized
- **Import structure** cleaned up with proper `__all__` exports
- **Error handling** improved across all storage operations
- **Code consistency** improved across all backend implementations

### Backward Compatibility
- All existing methods remain unchanged and fully compatible
- No breaking changes to the public API
- Existing code will continue to work without modifications

### Testing
- **Comprehensive test suite** covering all new functionality
- **Performance benchmarking** for bulk vs individual operations
- **Cross-backend compatibility** testing
- **Error handling** validation
- **JSON data storage** testing with complex objects

---

## [0.2.x] - Previous Versions

Previous versions were maintained by the original author. This changelog starts from version 0.3.0 under new maintenance by Suraj Mandal.

---

### Notes for Developers

**Migration from 0.2.x to 0.3.0:**
- No code changes required for existing functionality
- Consider using new bulk operations (`getAll()`, `getMany()`, `removeAll()`) for better performance
- Update imports if using internal storage backend classes directly

**New in this version:**
- Bulk operations are significantly faster for multiple data operations
- Enhanced type support makes the library more IDE-friendly
- Comprehensive documentation makes integration easier

**Maintainer Information:**
- **New Maintainer:** Suraj Mandal
- **GitHub:** [@surajmandalcell](https://github.com/surajmandalcell)
- **Repository:** [LocalStoragePro](https://github.com/surajmandalcell/LocalStoragePro)
