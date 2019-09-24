#/usr/bin/env python3
"""
title: 10_text_manipulaton.py
author: exm5840
date(created): 2019-09-19 11:25:39 EDT
date (updated): 2019-09-19 11:25:39 EDT
"""


def main():
    f_name = 'names.txt'
    new_f_name = 'new_names.txt'
    file_contents = read_file(f_name)
##    print(file_contents)
    add_last_name(file_contents)
    print(file_contents)
    write_contents_to_file(new_f_name, file_contents)


def read_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    return lines


def add_last_name(names):
    for idx,name in enumerate(names):
        if is_vowel(name[0]):
            names[idx] = name.rstrip() + " Phillips\n"
        else:
            names[idx] = name.rstrip() + " Moses\n"
    return names


def write_contents_to_file(file_name, contents):
    with open(file_name, 'w') as f:
        f.writelines(contents)


def is_vowel(c):
    return 0 == len({'a','e','i','o','u'}.intersection({c.lower()}))


if __name__ == '__main__':
    main()
