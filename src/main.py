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

        token_pattern = re.compile(r'\w+|[^\w\s]')
        tokens = token_pattern.findall(content)

        for token in tokens:
            print(f"{token}: {classify_token(token)}")

if __name__ == "__main__":
    # Creates The DFA Image
    create_dfa_image()

    # Reads and Classifies Tokens From The Input File
    read_and_classify_file('./input/example.txt')
