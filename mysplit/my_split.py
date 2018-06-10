def my_split(string,separator):
    out_list = []
    while separator in string:
        for i,j in enumerate(string):
            if j == separator:
                list_element = string[:i]
                string = string[i+1:]
                if not string == "":
                    out_list.append(list_element)
                break
    if not string == "":
        out_list.append(string)
    return out_list