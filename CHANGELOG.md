# Changelog

## [1.2.9] - Minor Version Support Update

### ✨ New Features

- **Minor Version Support**: The `Browser` class now supports minor version constraints in addition to major versions
- **Multiple Version Formats**: Version constraints can now be specified as:
  - Integer: `max_version=18` (major version only)
  - Float: `max_version=18.4` (major.minor)
  - String: `max_version="18.4.1"` (semantic versioning)
  - Tuple: `max_version=(18, 4, 1)` (programmatic)

### 🐛 Bug Fixes

- **Safari Version Control**: Fixed issue where Safari versions above a specified minor version (e.g., 18.5+) were still being selected when `max_version=18.4` was specified

### 📈 Improvements

- **Enhanced Version Comparison**: Added sophisticated version comparison logic that properly handles minor and patch versions
- **Backward Compatibility**: All existing code using integer versions will continue to work exactly as before
- **Better Error Messages**: Improved validation error messages for invalid version constraints

### 🛠️ Technical Changes

- Added `_parse_version()` helper function to parse various version formats
- Added `_compare_versions()` helper function for semantic version comparison
- Added `version_matches()` method to the `Browser` class for checking version constraints
- Updated `_get_browser_http_options()` to use the new version matching logic

### 📚 Documentation

- Updated README.md with minor version support examples
- Added detailed usage guide in `MINOR_VERSION_USAGE.md`
- Added inline documentation for all new version-related functions

### 🔧 Usage Examples

```python
# Block Safari 18.5 and above, allow up to 18.4.x
Browser(name='safari', max_version=18.4)

# Safari between versions 17.5 and 18.4
Browser(name='safari', min_version=17.5, max_version=18.4)

# Multiple browsers with different constraints
browsers = [
    Browser(name='safari', max_version=18.4),
    Browser(name='chrome', min_version=120, max_version=125),
    Browser(name='firefox', max_version="115.2"),
]
```

### 🔄 Migration Guide

**Before (Major Version Only):**

```python
Browser(name='safari', max_version=18)  # Included ALL 18.x versions
```

**After (Minor Version Support):**

```python
Browser(name='safari', max_version=18.4)  # Blocks 18.5 and above
```
