def my_split(string,separator):
    result = []
    while separator in string:
        for i,j in enumerate(string):
            if j == separator:
                list_element = string[:i]
                string = string[i+1:]
                if not string == "":
                    result.append(list_element)
                break
    if not string == "":
        result.append(string)
    return result