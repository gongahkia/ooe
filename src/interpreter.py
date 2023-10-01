# required imports

# FUA: 
# - write python code that iterates through the list and replace each word if necessary in groff / markdown / latex
# - interpreter will need to actively handle the count of each kind of stylised word since we are not distinguishing between left and right for any styling option
# - eventually incorporate a bash script that automatically calls the ooe interpreter with the 'ooe{version_number}' command called in terminal
# continue to account for edge cases where there should be NO spaces between * and words
# continue working on this

def parser_interpreter(token_array:list):
    # print(token_array)
    final_string = ""
    matching_counter_map:dict = {"ital_count":0, "bold_count":0, "under_count":0, "high_count":0, "header_count":0, "quote_count":0, "tabletop_count":0, "tablecont_count":0, "bullist_count":0, "numlist_count":0}
    for token in token_array:
        print(token)
        match token["type"]:
            case "ITAL":
                final_string += "*"
                final_string = final_string.rstrip(" ") # python strings are immutable, the rstrip() method will return a copy of the word
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
                final_string += token["value"]
                final_string += " "
            case _:
                print("edge case detected") # error logging
    return final_string.rstrip(" ")
