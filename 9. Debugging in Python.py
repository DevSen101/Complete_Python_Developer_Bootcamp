# Debugging
# 1 use linting
# 2 use IDE / Editors like PyCharm and Vs Code
# 3 read errors using pdb
import pdb


def add(n1, n2):
    pdb.set_trace()
    t = 4 * 5
    return n1 + n2

add(3,5)