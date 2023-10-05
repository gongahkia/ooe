# required imports
import lexer as lx
import interpreter as inter # work on this later

# --- 

"""def debug_print_original():
    fhand = open(f"../samples/yes.ooe", "r") # opens ooe files in the samples folder
    for line in fhand:
        print(line,end="")"""
    
def main():
    file_name:str = input("Name of ooe file: ").split(".")[0]
    fhand = open(f"{file_name}.ooe", "r") # opens ooe files in the samples folder
    file_str:str = ""
    for line in fhand:
        file_str += f"{line.strip()} ^^ "
    fhand.close()
    # print(file_str, end="") # for debugging
    try:
        token_array_1 = lx.lexer(file_str)
        return (file_name, token_array_1)
    except ValueError as e:
        print(f"Error log: {e}") # error logging zzz

# ---

parsed_tuple_output:tuple = inter.parser_interpreter(main())
file_name, output_src = parsed_tuple_output[0], parsed_tuple_output[1]
fhand = open(f"{file_name}.html", "w")
fhand.write(output_src)
fhand.close()
