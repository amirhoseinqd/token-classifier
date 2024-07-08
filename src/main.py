import os
import re
from dfa_visualizer import create_dfa_image
from dfa_classifier import classify_token

def read_and_classify_file(file_path):
    absolute_path = os.path.abspath(file_path)
    if not os.path.isfile(absolute_path):
        raise FileNotFoundError(f"No such file: '{absolute_path}'")
    
    with open(absolute_path, 'r') as file:
        content = file.read()

        # Regular expression to split text into tokens
        token_pattern = re.compile(r'\w+|[^\w\s]')
        tokens = token_pattern.findall(content)

        for token in tokens:
            print(f"{token}: {classify_token(token)}")

if __name__ == "__main__":
    # Create DFA image
    create_dfa_image()

    # Read and classify tokens from example file
    read_and_classify_file('./input/example.txt')
