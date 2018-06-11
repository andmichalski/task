import sys


def my_split(string, separator):
    result = []
    tmp_result = ""
    for char in string:
        if char == separator:
            if tmp_result:
                result.append(tmp_result)
            tmp_result = ""
        else:
            tmp_result += char
    if tmp_result:
        result.append(tmp_result)
    return result


def main():
    print(my_split(sys.argv[1], sys.argv[2]))


if __name__ == "__main__":
    main()
