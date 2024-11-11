# tests/test_remove_comments_cli.py

import subprocess
import sys
import textwrap
import os
import tempfile
import shutil

def test_remove_comments_cli_for_python_file():
    # Prepare input and expected output
    input_content = textwrap.dedent('''
        def add(a, b):
            # This function adds two numbers
            return a + b  # Return the sum
    ''').strip()

    expected_output = textwrap.dedent('''
        def add(a, b):
            return a + b
    ''').strip()

    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    try:
        # Create temporary input and output files within the temporary directory
        input_file = os.path.join(temp_dir, "temp_input.py")
        output_file = os.path.join(temp_dir, "temp_output.py")

        # Write input content to the input file
        with open(input_file, 'w') as f:
            f.write(input_content)

        # Run the CLI command with PYTHONPATH set to the project root
        subprocess.run(
            [sys.executable, "commentbegone/remove_comments_cli.py", input_file, output_file],
            env={"PYTHONPATH": os.getcwd()}
        )

        # Check the output
        with open(output_file, 'r') as f:
            assert f.read().strip() == expected_output

    finally:
        # Clean up the temporary directory and all its contents
        shutil.rmtree(temp_dir)


def test_remove_comments_cli_for_yaml_file():
    # Prepare input and expected output
    input_content = textwrap.dedent('''
        key1: value1  # Inline comment
        # Full line comment
        key2: value2
        nested:
          # Nested comment
          key3: value3  # Another inline comment
    ''').strip()

    expected_output = textwrap.dedent('''
        key1: value1
        key2: value2
        nested:
          key3: value3
    ''').strip()

    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    try:
        # Create temporary input and output files within the temporary directory
        input_file = os.path.join(temp_dir, "temp_input.yaml")
        output_file = os.path.join(temp_dir, "temp_output.yaml")

        # Write input content to the input file
        with open(input_file, 'w') as f:
            f.write(input_content)

        # Run the CLI command with PYTHONPATH set to the project root
        subprocess.run(
            [sys.executable, "commentbegone/remove_comments_cli.py", input_file, output_file],
            env={"PYTHONPATH": os.getcwd()}
        )

        # Check the output
        with open(output_file, 'r') as f:
            assert f.read().strip() == expected_output

    finally:
        # Clean up the temporary directory and all its contents
        shutil.rmtree(temp_dir)
