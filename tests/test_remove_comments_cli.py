# tests/test_remove_comments_cli.py

import subprocess
import sys
import textwrap
import os
import tempfile
import shutil

def test_remove_comments_cli_for_python_file():
    input_content = textwrap.dedent('''
        def add(a, b):
            # This function adds two numbers
            return a + b  # Return the sum
    ''').strip()

    expected_output = textwrap.dedent('''
        def add(a, b):
            return a + b
    ''').strip()

    temp_dir = tempfile.mkdtemp()
    try:
        input_file = os.path.join(temp_dir, "temp_input.py")
        output_file = os.path.join(temp_dir, "temp_output.py")

        with open(input_file, 'w', encoding='utf-8') as f:
            f.write(input_content)

        result = subprocess.run(
            [sys.executable, "-m", "commentbegone.remove_comments_cli", input_file, output_file],
            env={"PYTHONPATH": os.getcwd()},
            capture_output=True,
            text=True
        )

        # Check if there were any errors
        assert result.returncode == 0, f"CLI failed with output:\n{result.stderr}"

        with open(output_file, 'r', encoding='utf-8') as f:
            output = f.read().strip()
            assert output == expected_output, f"Expected:\n{expected_output}\n\nGot:\n{output}"

    finally:
        shutil.rmtree(temp_dir)

def test_remove_comments_cli_for_yaml_file():
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

    temp_dir = tempfile.mkdtemp()
    try:
        input_file = os.path.join(temp_dir, "temp_input.yaml")
        output_file = os.path.join(temp_dir, "temp_output.yaml")

        with open(input_file, 'w', encoding='utf-8') as f:
            f.write(input_content)

        result = subprocess.run(
            [sys.executable, "-m", "commentbegone.remove_comments_cli", input_file, output_file],
            env={"PYTHONPATH": os.getcwd()},
            capture_output=True,
            text=True
        )

        # Check if there were any errors
        assert result.returncode == 0, f"CLI failed with output:\n{result.stderr}"

        with open(output_file, 'r', encoding='utf-8') as f:
            output = f.read().strip()
            assert output == expected_output, f"Expected:\n{expected_output}\n\nGot:\n{output}"

    finally:
        shutil.rmtree(temp_dir)
