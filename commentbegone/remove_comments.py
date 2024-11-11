import re

def remove_comments_from_code(code: str) -> str:
    """
    Removes comments from the provided Python code.

    Args:
        code (str): The Python code as a string.

    Returns:
        str: The code with comments removed.
    """
    # Split the code into lines
    lines = code.splitlines()
    # Process each line
    cleaned_lines = []
    for line in lines:
        # Check if the line is only a comment
        if line.strip().startswith("#"):
            # Skip the line if it's a comment
            continue
        # Remove inline comments and strip trailing whitespace
        cleaned_line = re.sub(r'\s*#.*', '', line).rstrip()
        # Append the cleaned line if it's not empty
        if cleaned_line:
            cleaned_lines.append(cleaned_line)
    # Join the cleaned lines
    cleaned_code = '\n'.join(cleaned_lines)
    return cleaned_code
