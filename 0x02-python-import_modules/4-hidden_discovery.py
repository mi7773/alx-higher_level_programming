#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    d_list = dir(hidden_4)
    for i in d_list:
        if i[0] == '_' and i[1] == '_':
            continue
        print(i)
