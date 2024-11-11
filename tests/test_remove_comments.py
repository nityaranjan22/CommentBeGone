import textwrap
from commentbegone.remove_comments import remove_comments_from_text

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