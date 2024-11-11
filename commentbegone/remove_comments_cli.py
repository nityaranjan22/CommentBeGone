# remove_comments_cli.py

import argparse
from commentbegone.remove_comments import remove_comments_from_text

def remove_comments_from_file(input_file: str, output_file: str) -> None:
    """
    Reads a file, removes comments, and writes the cleaned content to a new file.

    Args:
        input_file (str): The path to the input file with comments.
        output_file (str): The path to the output file for cleaned content.
    """
    # Read the input file
    with open(input_file, 'r') as f:
        content = f.read()

    # Remove comments
    cleaned_content = remove_comments_from_text(content)

    # Write the cleaned content to the output file
    with open(output_file, 'w') as f:
        f.write(cleaned_content)

    print(f"Comments removed and saved to {output_file}")

# Set up the CLI interface
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove comments from a Python or YAML file.")
    parser.add_argument("input_file", help="Path to the input file with comments.")
    parser.add_argument("output_file", help="Path to save the cleaned output without comments.")

    args = parser.parse_args()

    remove_comments_from_file(args.input_file, args.output_file)
