from itertools import * # useful to have around


def head(l):
    print(l[0:4])
    
def tail(l):
    print(l[-4:])

def cat(l):
    return ''.join(l)

def get_filepath(day: str):
    return './inputs/' + day + '.txt'

def read_input_as_list(day: str, linesplit=None):
    with open(get_filepath(day)) as file:
        lines = file.readlines()
        if len(lines) == 1:
            return lines[0].split(linesplit)
        else: # return as list of lists
            if linesplit == '':
                return [
                    line.strip() for line in lines
                ]
            elif linesplit is None:
                return [
                    line.strip().split() for line in lines
                ]
            else:
                return [
                    line.strip().split(linesplit) for line in lines
                ]

def read_input_as_tuples(day: str, linesplit=None):
    return list(map(tuple, read_input_as_list(day, linesplit)))


def read_input_as_file(day: str):
    return open(get_filepath(day))