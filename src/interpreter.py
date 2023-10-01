# FUA: 
# consider if i want to make my life easier by distinguishing between left and right parantheses when lexing, if so EDIT lexer.py accordingly
# implement check for EVERY TOKEN that it is being used properly, implement a generic pair check and also different checks for different styles
    # paired token (ALL)
    # header (count number of +)
    # table (split by ;)
    # bul list, num list (split by ;, optionally count number of items)
# implement check for incomplete unpaired syntax even if the * is the last word of the entire document, or if the stylised text spans across multiple words
# incorporate a bash script that automatically calls the ooe interpreter with the 'ooe{version_number}' command called in terminal

def parser_interpreter(token_array:list):
    # print(token_array)
    final_string:str = ""
    # interpreter will need to actively handle the count of each kind of stylised word since we are not distinguishing between left and right for any styling option
    matching_counter_map:dict = {"ital_count":0, "bold_count":0, "under_count":0, "high_count":0, "header_count":0, "quote_count":0, "tabletop_count":0, "tablecont_count":0, "bullist_count":0, "numlist_count":0}
    for i in range(len(token_array)):
        print(token_array[i])
        match token_array[i]["type"]:
            case "ITAL":
                final_string = final_string.rstrip(" ") # python strings are immutable, the rstrip() method will return a copy of the word
                final_string += "*"
                # add code here!
            case "BOLD":
                final_string = final_string.rstrip(" ") 
                final_string += "**"
            case "UNDER":
                final_string = final_string.rstrip(" ") 
                final_string += "<ins>"
                # implement count for matching_counter_map["under_count"] to variate whether <ins> or </ins>
            case "HIGH":
                final_string = final_string.rstrip(" ") 
                pass
            case "HEADER":
                final_string = final_string.rstrip(" ") 
                pass
            case "QUOTE":
                final_string = final_string.rstrip(" ") 
                pass
            case "TABLETOP":
                final_string = final_string.rstrip(" ") 
                pass
            case "TABLECONT":
                final_string = final_string.rstrip(" ") 
                pass
            case "BULLIST":
                final_string = final_string.rstrip(" ") 
                pass
            case "NUMLIST":
                final_string = final_string.rstrip(" ") 
                pass
            case "NEWLINE":
                final_string += "\n"
            case "WORD":
                final_string += token_array[i]["value"]
                final_string += " "
            case _:
                print("edge case detected") # error logging
    return final_string.rstrip(" ")
