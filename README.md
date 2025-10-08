# Test #2 - Get Nested Value

Python solution for retrieving nested values from JSON-like dictionaries using a slash-separated key path

## How to run

```bash
python get_nested_value_challenge.py
```

This will execute the builtin test suite with detailed output for verification

## What's inside

* `get_nested_value(obj, key_path, default=None)`: main function to extract nested values from dictionaries using a `'/'` separated key path
* small test suite with console output for debugging

## Behavior

* `key_path` is a `'/'` separated string
* leading, trailing, and repeated slashes are ignored (e.g. `"a//b///c"` is treated the same as `"a/b/c"`)
* returns the original `obj` if `key_path` is empty (`""`)
* returns `default` if any key in the path is missing or if a non-dict is encountered
* supports custom default values

## Usage

```python
from get_nested_value_challenge import get_nested_value

# Basic usage
obj = {"a": {"b": {"c": "d"}}}
result = get_nested_value(obj, "a/b/c")  # Returns "d"

# With custom default
result = get_nested_value(obj, "missing/path", "NOT_FOUND")  # Returns "NOT_FOUND"
```

## Limitations

* list indices are not supported
* indistinguishable real value `None` from a missing path for default (`default=None`)
