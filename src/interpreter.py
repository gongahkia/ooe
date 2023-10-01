# required imports

# FUA: 
# - interpreter will need to actively handle the count of each kind of stylised word since we are not distinguishing between left and right for any styling option
# - implement check for EVERY TOKEN that it is being used properly
# - incorporate a bash script that automatically calls the ooe interpreter with the 'ooe{version_number}' command called in terminal
# implement the check i implemented for ITAL for every other case that functions the same way
# DEBUG ital issue, also implement check for incomplete syntax even if the * is the last word of the entire document

def parser_interpreter(token_array:list):
    # print(token_array)
    final_string:str = ""
    matching_counter_map:dict = {"ital_count":0, "bold_count":0, "under_count":0, "high_count":0, "header_count":0, "quote_count":0, "tabletop_count":0, "tablecont_count":0, "bullist_count":0, "numlist_count":0}
    for i in range(len(token_array)):
        print(token_array[i])
        match token_array[i]["type"]:
            case "ITAL":
                final_string = final_string.rstrip(" ") # python strings are immutable, the rstrip() method will return a copy of the word
                final_string += "*"
                match matching_counter_map["ital_count"]:
                    case 0: # should run once when there is no active waiting count for bold
                        matching_counter_map["ital_count"] += 1
                    case 1:
                        if token_array[i+2]["type"] == "ITAL":
                            matching_counter_map["ital_count"] += 1
                        else:
                            break
                            print(f"Syntax error detected. Unmatched italic after the word {token_array[i+1]['value']}.")
                    case 2:
                        matching_counter_map["ital_count"] = 0
                    case _:
                        print("Edge case hit, debug from this line!")
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
