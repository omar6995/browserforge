# Minor Version Support for Browsers

This update adds support for minor version constraints in browser specifications. Previously, the library only supported major version constraints (e.g., `max_version=18`), but now you can specify minor versions like `max_version=18.4`.

## Usage Examples

### Safari with Maximum Version 18.4

To ensure Safari versions don't exceed 18.4 (blocking 18.5 and above):

```python
from omar6995_browserforge.headers import Browser, HeaderGenerator

# Create a Safari browser constraint with max version 18.4
safari_browser = Browser(name='safari', max_version=18.4)

# Use with HeaderGenerator
headers = HeaderGenerator(browser=[safari_browser])
```

### Supported Version Formats

The `min_version` and `max_version` parameters now accept multiple formats:

```python
# Integer (major version only)
Browser(name='safari', max_version=18)  # 18.x.x

# Float (major.minor)
Browser(name='safari', max_version=18.4)  # Up to 18.4.x

# String (semantic versioning)
Browser(name='safari', max_version="18.4.1")  # Up to 18.4.1

# Tuple (programmatic)
Browser(name='safari', max_version=(18, 4, 1))  # Up to 18.4.1
```

### Version Range Examples

```python
# Safari between 17.5 and 18.4
Browser(name='safari', min_version=17.5, max_version=18.4)

# Chrome 120 or higher
Browser(name='chrome', min_version=120)

# Firefox up to 115.2
Browser(name='firefox', max_version="115.2")

# Edge exactly in the 110.x range
Browser(name='edge', min_version=110, max_version=110.99)
```

### Multiple Browsers with Different Constraints

```python
browsers = [
    Browser(name='safari', max_version=18.4),
    Browser(name='chrome', min_version=120, max_version=125),
    Browser(name='firefox', max_version=115),
]

headers = HeaderGenerator(browser=browsers)
```

## Version Comparison Logic

The version comparison follows semantic versioning principles:

- `18.4` includes `18.4.0`, `18.4.1`, etc.
- `18.4.1` is greater than `18.4.0`
- `18.5` is greater than `18.4.9`
- `19.0` is greater than `18.99.99`

## Migration from Previous Version

### Before (Major Version Only)

```python
# This would include ALL 18.x versions including 18.5, 18.6, etc.
Browser(name='safari', max_version=18)
```

### After (Minor Version Support)

```python
# This blocks 18.5 and above, allowing only up to 18.4.x
Browser(name='safari', max_version=18.4)
```

## Error Handling

The library validates version constraints:

```python
# This will raise a ValueError
Browser(name='safari', min_version=18.5, max_version=18.4)
# Error: Browser min version constraint (18.5) cannot exceed max version (18.4)
```

## Backward Compatibility

This update is fully backward compatible. Existing code using integer versions will continue to work exactly as before:

```python
# This still works and behaves the same as before
Browser(name='chrome', min_version=100, max_version=120)
```
