from unittest.mock import patch
from io import StringIO
import main

def run_test(inputs):
    """Helper function to run tests with mocked input."""
    input_string = "\n".join(inputs) + "\n"

    with patch('sys.stdin', StringIO(input_string)):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            try:
                main.main()
            except SystemExit:
                # The 'exit' command will cause a SystemExit
                pass
            return mock_stdout.getvalue()

# Test with a Spanish sentence
output = run_test(["Hola, como estas?", "exit"])
print(output)

# Test with an English sentence
output = run_test(["Hello, how are you?", "exit"])
print(output)
