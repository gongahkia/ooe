# FUA: 
# continue implementing checks for other syntax options
# implement check for EVERY TOKEN that it is being used properly, implement a generic pair check and also different checks for different styles
    # paired token (ALL)
    # header (count number of +)
    # table (split by ;)
    # bul list, num list (split by ;, optionally count number of items)
# incorporate a bash script that automatically calls the ooe interpreter with the 'ooe{version_number}' command called in terminal
# add colored text for the ooe interpreter has stopped compiling part!

def parser_interpreter(token_array:list):
    print(token_array)
    final_string:str = ""
    mcm:dict = {"ital_count":True, "bold_count":True, "under_count":True, "high_count":True, "quote_count":True, "header_count":True, "tabletop_count":0, "tablecont_count":0, "bullist_count":0, "numlist_count":0}
    header_stored_value:int = 0
    line_counter:int = 1

    for i in range(len(token_array)):

        # print(token_array[i])

        match token_array[i]["type"]:

            # DONE ✅
            case "ITAL":
                if mcm["ital_count"]:
                    ital_initial_index = i
                    # print(mcm["ital_count"])
                    mcm["ital_count"] = False
                    final_string += "<i>"
                    type_array:list = [pair["type"] for pair in token_array[ital_initial_index+1:]]
                    if "ITAL" not in type_array:
                        # print(type_array)
                        print(f"Syntax error detected in UNMATCHED ITALICS ICON [`] on line {line_counter}.")
                        print("OOE interpreter has stopped compiling.")
                        return final_string.rstrip(" ")
                    elif type_array.index("NEWLINE") < type_array.index("ITAL"):
                        # print(type_array)
                        print(f"Syntax error detected in UNMATCHED ITALICS ICON [`] on line {line_counter}.")
                        print("OOE interpreter has stopped compiling.")
                        return final_string.rstrip(" ")
                else:
                    # print(mcm["ital_count"])
                    mcm["ital_count"] = True
                    final_string = final_string.rstrip(" ") 
                    final_string += "</i>"
                    final_string += " "

            # DONE ✅
            case "BOLD":
                if mcm["bold_count"]:
                    bold_initial_index = i
                    # print(mcm["bold_count"])
                    mcm["bold_count"] = False
                    final_string += "<b>"
                    # CHECKS FOR WRONG UNMATCHED PAIRS SYNTAX
                    # CHECKS FOR WHETHER BOLDED SYNTAX IS ON SAME LINE OR NEWLINE
                    type_array = [pair["type"] for pair in token_array[bold_initial_index+1:]]
                    if "BOLD" not in type_array:
                        # print(type_array)
                        print(f"Syntax error detected in UNMATCHED BOLD ICON [*] on line {line_counter}.")
                        print("OOE interpreter has stopped compiling.")
                        return final_string.rstrip(" ")
                    elif type_array.index("NEWLINE") < type_array.index("BOLD"):
                        # print(type_array)
                        print(f"Syntax error detected in UNMATCHED BOLD ICON [*] on line {line_counter}.")
                        print("OOE interpreter has stopped compiling.")
                        return final_string.rstrip(" ")
                else:
                    # print(mcm["bold_count"])
                    mcm["bold_count"] = True
                    final_string = final_string.rstrip(" ") 
                    final_string += "</b>"
                    final_string += " "

            # DONE ✅
            case "UNDER":
                if mcm["under_count"]:
                    under_initial_index = i
                    # print(mcm["under_count"])
                    mcm["under_count"] = False
                    final_string += "<u>"
                    type_array = [pair["type"] for pair in token_array[under_initial_index+1:]]
                    if "UNDER" not in type_array:
                        # print(type_array)
                        print(f"Syntax error detected in UNMATCHED UNDERLINE ICON [_] on line {line_counter}.")
                        print("OOE interpreter has stopped compiling.")
                        return final_string.rstrip(" ")
                    elif type_array.index("NEWLINE") < type_array.index("UNDER"):
                        # print(type_array)
                        print(f"Syntax error detected in UNMATCHED UNDERLINE ICON [_] on line {line_counter}.")
                        print("OOE interpreter has stopped compiling.")
                        return final_string.rstrip(" ")
                else:
                    # print(mcm["under_count"])
                    mcm["under_count"] = True
                    final_string = final_string.rstrip(" ") 
                    final_string += "</u>"
                    final_string += " "

            # DONE ✅
            case "HIGH":
                if mcm["high_count"]:
                    high_initial_index = i
                    # print(mcm["high_count"])
                    mcm["high_count"] = False
                    final_string += "<mark>"
                    type_array = [pair["type"] for pair in token_array[high_initial_index+1:]]
                    if "HIGH" not in type_array:
                        # print(type_array)
                        print(f"Syntax error detected in UNMATCHED HIGHLIGHT ICON [&] on line {line_counter}.")
                        print("OOE interpreter has stopped compiling.")
                        return final_string.rstrip(" ")
                    elif type_array.index("NEWLINE") < type_array.index("HIGH"):
                        # print(type_array)
                        print(f"Syntax error detected in UNMATCHED HIGHLIGHT ICON [&] on line {line_counter}.")
                        print("OOE interpreter has stopped compiling.")
                        return final_string.rstrip(" ")
                else:
                    # print(mcm["high_count"])
                    mcm["high_count"] = True
                    final_string = final_string.rstrip(" ") 
                    final_string += "</mark>"
                    final_string += " "

            # DONE ✅
            case "QUOTE":
                if mcm["quote_count"]:
                    quote_initial_index = i
                    # print(mcm["quote_count"])
                    mcm["quote_count"] = False
                    final_string += "<blockquote>"
                    type_array = [pair["type"] for pair in token_array[quote_initial_index+1:]]
                    if "QUOTE" not in type_array:
                        # print(type_array)
                        print(f"Syntax error detected in UNMATCHED QUOTATION ICON [@] on line {line_counter}.")
                        print("OOE interpreter has stopped compiling.")
                        return final_string.rstrip(" ")
                    elif type_array.index("NEWLINE") < type_array.index("QUOTE"):
                        # print(type_array)
                        print(f"Syntax error detected in UNMATCHED QUOTATION ICON [@] on line {line_counter}.")
                        print("OOE interpreter has stopped compiling.")
                        return final_string.rstrip(" ")
                else:
                    # print(mcm["quote_count"])
                    mcm["quote_count"] = True
                    final_string = final_string.rstrip(" ") 
                    final_string += "</blockquote>"
                    final_string += " "

            # DONE ✅
            case "HEADER":
                if mcm["header_count"]:
                    header_initial_index = i
                    # print(mcm["header_count"])
                    mcm["header_count"] = False
                    header_count:int = list(token_array[i]["value"]).count("+")
                    header_stored_value = header_count 
                    header_value:str = ""
                    match header_count:
                        case 0:
                            print(f"Syntax error detected in NULL HEADER COUNT [+] on line {line_counter}.")
                            print("OOE interpreter has stopped compiling.")
                            return final_string.rstrip(" ")
                        case 1:
                            header_value = "h1"
                        case 2:
                            header_value = "h2"
                        case 3:
                            header_value = "h3"
                        case 4:
                            header_value = "h4"
                        case 5:
                            header_value = "h5"
                        case 6:
                            header_value = "h6"
                        case _:
                            print(f"Syntax error detected in EXCESS HEADER COUNT [+] on line {line_counter}.")
                            print(f"MAX HEADER COUNT possible is 6.")
                            print("OOE interpreter has stopped compiling.")
                            return final_string.rstrip(" ")
                    final_string += f"<{header_value}>" # REPLACE THIS!
                    type_array = [pair["type"] for pair in token_array[header_initial_index+1:]]
                    if "HEADER" not in type_array:
                        # print(type_array)
                        print(f"Syntax error detected in UNMATCHED HEADER ICON [+] on line {line_counter}.")
                        print("OOE interpreter has stopped compiling.")
                        return final_string.rstrip(" ")
                    elif type_array.index("NEWLINE") < type_array.index("HEADER"):
                        # print(type_array)
                        print(f"Syntax error detected in UNMATCHED HEADER ICON [+] on line {line_counter}.")
                        print("OOE interpreter has stopped compiling.")
                        return final_string.rstrip(" ")
                else:
                    # print(mcm["header_count"])
                    mcm["header_count"] = True
                    header_count = list(token_array[i]["value"]).count("+")
                    if header_stored_value != header_count:
                        print(f"Syntax error detected in UNMATCHED HEADER COUNT [+] on line {line_counter}.")
                        print(f"Number of HEADER ICONS must match [+].")
                        print("OOE interpreter has stopped compiling.")
                        return final_string.rstrip(" ")
                    header_value = ""
                    match header_count:
                        case 0:
                            print(f"Syntax error detected in NULL HEADER COUNT [+] on line {line_counter}.")
                            print("OOE interpreter has stopped compiling.")
                            return final_string.rstrip(" ")
                        case 1:
                            header_value = "h1"
                        case 2:
                            header_value = "h2"
                        case 3:
                            header_value = "h3"
                        case 4:
                            header_value = "h4"
                        case 5:
                            header_value = "h5"
                        case 6:
                            header_value = "h6"
                        case _:
                            print(f"Syntax error detected in EXCESS HEADER COUNT [+] on line {line_counter}.")
                            print(f"MAX HEADER COUNT possible is 6.")
                            print("OOE interpreter has stopped compiling.")
                            return final_string.rstrip(" ")
                    final_string = final_string.rstrip(" ") 
                    final_string += f"</{header_value}>" # REPLACE THIS!
                    final_string += " "
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

            # DONE ✅
            case "NEWLINE":
                final_string += "\n"
                line_counter += 1

            # DONE ✅
            case "WORD":
                final_string += token_array[i]["value"]
                final_string += " "

            # DONE ✅
            case _:
                print("edge case detected") # error logging

    return final_string.rstrip(" ")
