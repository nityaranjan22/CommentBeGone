# tests/test_remove_comments.py

from commentbegone.remove_comments import remove_comments_from_text
import textwrap

def test_remove_python_comments():
    code_with_comments = textwrap.dedent('''
        def add(a, b):
            # This function adds two numbers
            return a + b  # Return the sum
    ''').strip()

    expected_code = textwrap.dedent('''
        def add(a, b):
            return a + b
    ''').strip()

    assert remove_comments_from_text(code_with_comments) == expected_code

def test_remove_yaml_comments():
    yaml_with_comments = textwrap.dedent('''
        key1: value1  # Inline comment
        # Full line comment
        key2: value2
        nested:
          # Nested comment
          key3: value3  # Another inline comment
    ''').strip()

    expected_yaml = textwrap.dedent('''
        key1: value1
        key2: value2
        nested:
          key3: value3
    ''').strip()

    assert remove_comments_from_text(yaml_with_comments) == expected_yaml

def test_mixed_content_with_comments():
    mixed_content = textwrap.dedent('''
        # This is a YAML-like structure with Python code
        key1: value1  # Inline comment
        def func():
            return "Hello"  # Return a greeting
        # End of example
    ''').strip()

    expected_output = textwrap.dedent('''
        key1: value1
        def func():
            return "Hello"
    ''').strip()

    assert remove_comments_from_text(mixed_content) == expected_output

def test_escaped_hash():
    content_with_escaped_hash = textwrap.dedent('''
        key: value_with_escaped\\#hash  # Real comment
        # Full comment line
        def func(): return "String with # inside"  # Inline comment
    ''').strip()

    expected_output = textwrap.dedent('''
        key: value_with_escaped\\#hash
        def func(): return "String with # inside"
    ''').strip()

    assert remove_comments_from_text(content_with_escaped_hash) == expected_output
