import utility
import re

integer_literal_addition = " ([0-9]+) \+ ([0-9]+)(\n| )"
line = 'int: fifteen 8 + 7\n'

if (re.search(integer_literal_addition, line)):
    print("found")
