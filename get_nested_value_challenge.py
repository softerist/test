def get_nested_value(obj, key_path, default=None):
    """    
    Parameters:
        obj: any
            The root object expected to be a dict, nested dictionaries are traversed
        key_path: str
            Slash separated path, e.g. "a/b/c", also leading/trailing/repeated slashes are ignored
        default: any, optional
            Value to return when the path does not exist or cannot be traversed, defaults to None
            
    Returns:
        any
            The value at the path if it exists (including None if the final value is None), otherwise default
    """
    
    # ensure that key_path is a string
    if not isinstance(key_path, str):
        raise TypeError("key_path must be a string")
    
    # normalize path by removing empty segments
    parts = [p for p in key_path.split('/') if p != '']
    if not parts:
        return obj
    
    current = obj
    for segment in parts:
        if not isinstance(current, dict) or segment not in current:
            return default
        current = current[segment]
    return current

def run_tests():
    """Tests suite"""
    # not choosing 'assert' as a way to do these tests, because I believe this way I can better see detailed logs about why the tests might be failing
    tests = [
        # (obj, path, default, expected, description)
        ({"a": {"b": {"c": "d"}}}, "a/b/c", None, "d", "challenge example #1"),
        ({"x": {"y": {"z": "a"}}}, "x/y/z", None, "a", "challenge example #2"),
        ({"a": {"b": {"c": "d"}}}, "a/x/y", None, None, "non-existent key returns default"),
        ({}, "a/b/c", None, None, "epty object"),
        ({"a": {"b": {"c": "d"}}}, "a/b", None, {"c": "d"}, "partial path returns nested dict"),
        ({"a": {"b": {"c": "d"}}}, "a/x", "NOT FOUND", "NOT FOUND", "custom default value"),
        ({"a": {"b": "c"}}, "/a/b/", None, "c", "leading/trailing slashes ignored"),
        ({"a": 1}, "a/b", None, None, "non-dict intermediate returns default"),
        ({"a": {"b": {"c": "d"}}}, "a//b///c", None, "d", "repeated slashes are ignored"),
        ({"a": {"b": {"c": "d"}}}, "", None, {"a": {"b": {"c": "d"}}}, "empty path returns original object"),
    ]
    
    passed = 0
    failed = 0
    for i, (obj, path, default, expected, desc) in enumerate(tests, 1):
        try:
            result = get_nested_value(obj, path, default=default)
            ok = (result == expected)
        except Exception as exc:
            result = f"<exception: {type(exc).__name__}>"
            ok = False
        status = "PASSED" if ok else "FAILED"
        if ok:
            passed += 1
        else:
            failed += 1
        
        print(f"Test {i}: {desc}")
        print(f"  Input: {obj}, path='{path}', default={default}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        print(f"  Status: {status}")
        print("-" * 40)
    
    print(f"Results: {passed}/{passed + failed} tests passed")
    if failed > 0:
        print(f"[FAILED] - {failed} test(s) failed")
    else:
        print("[SUCCESS] - all tests passed")
        
if __name__ == '__main__':
    run_tests()
  
