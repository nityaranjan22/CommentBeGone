import re

def remove_comments_from_python(content: str) -> str:
    """
    Removes comments from Python content, excluding those inside strings.

    Args:
        content (str): The content of the file as a string.

    Returns:
        str: The content with comments removed.
    """
    # Match Python comments only if they are outside of string literals.
    pattern = re.compile(r'(?<!\\)(#)(?!.*[\'\"].*).*$', re.MULTILINE)
    
    # Function to remove matches that are actual comments and not within strings.
    cleaned_content = pattern.sub('', content)
    
    # Clean up any trailing spaces left by removed comments.
    return '\n'.join(line.rstrip() for line in cleaned_content.splitlines() if line.strip())


def remove_comments_from_yaml(content: str) -> str:
    """
    Removes comments from YAML content.

    Args:
        content (str): The content of the file as a string.

    Returns:
        str: The content with comments removed.
    """
    pattern = re.compile(r"(?<!\\)#.*$", re.MULTILINE)
    cleaned_content = re.sub(pattern, '', content)
    return '\n'.join([line.rstrip() for line in cleaned_content.splitlines() if line.strip()])

def remove_comments_from_text(content: str, file_type: str = 'python') -> str:
    """
    Removes comments from content based on file type.

    Args:
        content (str): The content of the file as a string.
        file_type (str): The file type to specify comment syntax, e.g., 'python' or 'yaml'.

    Returns:
        str: The content with comments removed.
    """
    if file_type == 'python':
        return remove_comments_from_python(content)
    elif file_type == 'yaml':
        return remove_comments_from_yaml(content)
    else:
        raise ValueError("Unsupported file type. Please use 'python' or 'yaml'.")
