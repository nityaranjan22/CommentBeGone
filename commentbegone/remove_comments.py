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

    for line in lines:
        # Remove inline comments
        cleaned_line = re.sub(r'(?<!\\)#.*', '', line).rstrip()
        # Add cleaned line if not empty
        if cleaned_line.strip():
            cleaned_lines.append(cleaned_line)

    # Join the cleaned lines back into a single string
    cleaned_content = '\n'.join(cleaned_lines)
    return cleaned_content
