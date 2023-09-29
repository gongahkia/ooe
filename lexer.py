# this lexer is implemented by chatGPT 3.5

# FUA
# - learn regex to better implement additional syntax
# - implement additional syntax checks
    # - other kinds of brackets
    # - actual coding syntax
# - separate job of lexer, parser and interpreter 

# ---

# handles lexical analysis --> left to right

import re # regex for easy lexing

grammer_pattern = [
    ('NUM', r'\d+(\.\d+)?'), # matches integers and floating point
    ('OP', r'[\+\-\*/]'), # matches four basic arithmetic operators
    ('LPARENT', r'\('), # matches any occurence of left paranthesis
    ('RPARENT', r'\)')
        ]

def lexer(input_string):
    token_array = []
    while input_string: # iterates over each 1,2,4 byte character in input string
        match_val = None # variable initialisation and assignment 
        for data_type, regex_pattern in grammer_pattern:
            regex_1 = re.compile(regex_pattern) # .compile() method takes in a string and converts it to a machine readable regular expression pattern which can be applied to a string
            match_val = regex_1.match(input_string)
            if match_val:
                value = match_val.group(0)
                token_array.append((data_type, value))
                input_string = input_string[len(value):].lstrip() # iterating after each character / chunk that matches regex
                break
        if not match_val:
            raise ValueError(f"cb follow the syntax: {input_string}")
    return token_array

if __name__ == "__main__": # checks whether this file being run directly from interpreter
    # if script is being run directly using 'python3', __name__ variable takes on the value of string "__main__"
    # elif script is imported as a module in another file, then __name__ will take on the value of original script file name minus .py file extenstion
    user_input = input("Enter an arithmetic expression: ")
    try:
        token_array_1 = lexer(user_input)
        print(f"Token array: {token_array_1}")
    except ValueError as e:
        print(f"Error log: {e}")
