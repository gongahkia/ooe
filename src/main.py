# required imports
import lexer as lx
import interpreter as inter # work on this later

# --- 

# FUA: 
# - eventually, rewrite this segment of code into a function, and allow for ooe code to be read from a whole ooe file

# --- 

def main():
    file_name:str = input("Name of ooe file:").split(".")[0]
    fhand = open(f"../samples/{file_name}.ooe", "r") # opens ooe files in the samples folder
    file_str:str = ""
    for line in fhand:
        file_str += f"{line.strip()} ^^ "
    # print(file_str, end="") # for debugging
    try:
        token_array_1 = lx.lexer(file_str)
        return token_array_1
    except ValueError as e:
        print(f"Error log: {e}") # error logging zzz

# ---

# main event loop
output_src = inter.parser_interpreter(main())
print(output_src)
