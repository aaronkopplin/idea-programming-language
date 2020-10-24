STRING_LITERAL =                    "\"([a-z ]+)\""
VARIABLE =                          "([a-z_]+)"
STRING_DECLARATION =                "(^|\b)string: " + VARIABLE
PRINT_VARIABLE =                    "^print: " + VARIABLE
PRINT_STRING_LITERAL =              "^print: " + STRING_LITERAL
INTEGER =                           "\b([0-9]+)"
INTEGER_DECLARATION =               "(^|\b)int: " + VARIABLE
INTEGER_LITERAL_DECLARATION =       "(^|\b)int: " + VARIABLE + " " + INTEGER
ADD_INTEGER_VARIABLE_VARIABLE =     VARIABLE + " \+ " + VARIABLE
ADD_INTEGER_INTEGER_INTEGER =       INTEGER + " \+ " + INTEGER
ADD_INTEGER_INTEGER_VARIABLE =      INTEGER + " \+ " + VARIABLE
ADD_INTEGER_VARIABLE_INTEGER =      VARIABLE + " \+ " + INTEGER


def error_message(line, line_num):
    GREEN = '\033[31m'
    RESET = '\033[m'
    print("error parsing file at line " + str(line_num) + "\nline: " + GREEN + line + RESET)