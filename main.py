import sys
import re
import math
import datetime

YEAR = datetime.datetime.now().date().year


def ifstmnt():
    pass


def polish(line: str):
    if 'the square root of ' in line:
        lst = list(line.replace('the square root of ', "math.sqrt("))
        lst.append(')')
        line = ''.join(lst)
    return line.replace("divided by", '/'
                        ).replace('times', '*'
                                  ).replace('multiplied by', '*'
                                            ).replace('to the power of', '**'
                                                      ).replace('plus', '+'
                                                                ).replace('minus', '-'
                                                                          ).replace('the value of ', ''
                                                                                    ).replace('this year', str(YEAR))


def main(file_lines: list):
    for count, line in enumerate(file_lines):
        dd = -0
        po = polish(line)
        if "if value of " in po and " is " in po:
            ifstmnt()
        elif 'convert' in po:
            diction = {
                'number': 'int(',
                'decimal': 'float(',
                'text': 'str('
            }
            prelist = po.replace('convert ', '').replace('to', '')
            for i in diction.keys():
                prelist = prelist.replace(i, diction[i])
            lst = list(prelist)
            if lst[-1] == '\n':
                lst.pop(-1)
            jj = ((''.join(lst)).replace('int(', '').replace('float(', '').replace('str(', '')).strip()
            fin = (''.join(lst)).replace(jj, '')
            exec(jj + '=' + fin.lstrip() + jj + ')')
        elif "set value of " in po and " to " in po:
            po = po.replace("set value of ", "").replace(" to ", "=")
            dd = 1
        elif "output " in po:
            # noinspection PyUnboundLocalVariable
            if lst[-1] == '\n':
                lst.pop(-1)
            lst = list(po.replace("output ", "print("))
            lst.append(')')
            exec(''.join(lst))
            continue
        if 'input from user with prompt of ' in line:
            lst = list(po.replace('input from user with prompt of ', 'input("'))
            if lst[-1] == '\n':
                lst.pop(-1)
            lst.append('"')
            lst.append(')')
            exec(''.join(lst))
        elif dd ==1:
            exec(po)

def stuff():
    pass


if len(sys.argv) == 2:
    main(open(sys.argv[1]).readlines())
else:
    stuff(sys.argv)
