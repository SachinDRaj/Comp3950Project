import numpy


def read_from_file(filepath):
    in_file = open(filepath,'r')
    contents = in_file.read()
    in_file.close()
    return get_from_string(contents)


def get_from_string(contents):
    edgelist = []
    as_lines = contents.split('\n')
    for line in as_lines:
        split = line.strip().split()
        u = split[0].strip()
        edgelist.append(u)
    return edgelist
