import textwrap
from commentbegone.remove_comments import remove_comments_from_code

def test_remove_comments():
    code_with_comments = textwrap.dedent('''
        def add(a, b):
            # This function adds two numbers
            return a + b  # Return the sum
            # Another comment
        # Final comment
    ''').strip()
    
    expected_code = textwrap.dedent('''
        def add(a, b):
            return a + b
    ''').strip()
    
    assert remove_comments_from_code(code_with_comments) == expected_code
