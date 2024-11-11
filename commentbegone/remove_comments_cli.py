# commentbegone/remove_comments_cli.py

import argparse
from commentbegone.remove_comments import remove_comments_from_text
import os
import sys

def remove_comments_from_file(input_file: str, output_file: str) -> None:
    """
    Reads a file, removes comments, and writes the cleaned content to a new file.

    Args:
        input_file (str): The path to the input file with comments.
        output_file (str): The path to the output file for cleaned content.
    """
    _, ext = os.path.splitext(input_file)
    file_type = 'yaml' if ext.lower() in ['.yaml', '.yml'] else 'python'

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input file '{input_file}': {e}", file=sys.stderr)
        sys.exit(1)

    try:
        cleaned_content = remove_comments_from_text(content, file_type=file_type)
    except Exception as e:
        print(f"Error processing file '{input_file}': {e}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
    except Exception as e:
        print(f"Error writing to output file '{output_file}': {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Comments removed and saved to '{output_file}'.")

def main():
    parser = argparse.ArgumentParser(description="Remove comments from a Python or YAML file.")
    parser.add_argument("input_file", help="Path to the input file with comments.")
    parser.add_argument("output_file", help="Path to save the cleaned output without comments.")
    args = parser.parse_args()

    remove_comments_from_file(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
