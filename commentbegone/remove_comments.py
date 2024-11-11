# commentbegone/remove_comments.py

import re

def remove_comments_from_text(content: str) -> str:
    """
    Removes comments from Python or YAML content.

    Args:
        content (str): The content of the file as a string.

    Returns:
        str: The content with comments removed.
    """
    # Split content into lines
    lines = content.splitlines()
    cleaned_lines = []

    # Regular expression pattern to match comments that are not within strings or escaped
    comment_pattern = re.compile(r'(?<!\\)#(?![^"\']*["\']).*')

    for line in lines:
        # Remove comments that meet the criteria
        if '#' in line:
            cleaned_line = comment_pattern.sub('', line).rstrip()
        else:
            cleaned_line = line.rstrip()

        # Append each line if it's not empty after stripping comments and spaces
        if cleaned_line:
            cleaned_lines.append(cleaned_line)

    # Join cleaned lines into a single string
    cleaned_content = '\n'.join(cleaned_lines)
    return cleaned_content
