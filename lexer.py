# this lexer was originally implemented by chatGPT 3.5

# ---

# FUA
# - learn regex to better implement additional syntax from https://regexone.com/lesson/introduction_abcs
# - implement additional syntax checks under the grammer_pattern array
    # - other kinds of brackets
    # - other syntax for practice markup language
# - separate job of lexer, parser and interpreter 

# ---

# handles lexical analysis --> left to right

import re # python regex library for easy lexing

# ideas for ooe syntax
    # italicised `text`
    # bolded *text*
    # underlined _text_
    # highlighted &text&
    # header +text+
        # header depth ++ reflected by number of +, max left depth of 6
    # quotes @quotes text@
    # tables
        # table %table name; column name; column name; column name%
            # column names separated by semicolons
        # table values $table value; table value; table value$
            # table values separated by semicolons
    # lists
        # bulleted lists
            # bullet lists -list name; list value; list value-
                # list values separated by semicolons
        # numbered lists
            # numbered list !list name; list value; list value!

# defines the grammer rules for the markup language
 # order of patterns matters since they're checked from top to bottom. Place more specific patterns before generic ones.
grammer_pattern = [
    ('ITAL', r'\`'),
    ('BOLD', r'\*'),
    ('UNDER', r'\_'),
    ('HIGH', r'\&'),
    ('HEADER',r'\+{1,6}'),
    ('QUOTE', r'\@'),
    ('TABLETOP', r'\%'),
    ('TABLECONT', r'\$'),
    ('BULLIST', r'\-'),
    ('NUMLIST', r'\!'),
    ('NEWLINE', r'\^\^'),
    ('WORD', r'[A-Za-z]+'),
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