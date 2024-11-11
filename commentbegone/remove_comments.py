# commentbegone/remove_comments.py

import re
from ruamel.yaml import YAML
from io import StringIO

def remove_comments_from_python(content: str) -> str:
    """
    Removes comments from Python code.

    Args:
        content (str): The Python code as a string.

    Returns:
        str: The code with comments removed.
    """
    # Regular expression pattern to match comments not within quotes
    pattern = re.compile(
        r'''
        (?P<code>[^"'\n]*?)          # Any code before the comment
        (?P<comment>\s*#.*)          # The comment
        (?P<newline>\n|$)            # Newline or end of string
        ''',
        re.VERBOSE
    )

    def replacer(match):
        code = match.group('code').rstrip()
        if code:
            return code + '\n'
        else:
            return ''

    cleaned_content = pattern.sub(replacer, content)
    return cleaned_content.strip()

def remove_comments_from_yaml(content: str) -> str:
    """
    Removes comments from YAML content using ruamel.yaml.

    Args:
        content (str): The YAML content as a string.

    Returns:
        str: The YAML content with comments removed.
    """
    yaml = YAML()
    yaml.preserve_quotes = True
    data = yaml.load(content)
    stream = StringIO()
    yaml.dump(data, stream)
    return stream.getvalue().strip()

def remove_comments_from_text(content: str, file_type: str = 'python') -> str:
    """
    Removes comments from Python or YAML content.

    Args:
        content (str): The content of the file as a string.
        file_type (str): Type of the file ('python' or 'yaml').

    Returns:
        str: The content with comments removed.
    """
    if file_type.lower() == 'yaml':
        return remove_comments_from_yaml(content)
    else:
        return remove_comments_from_python(content)
