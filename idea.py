import sys
import re
import standard_library as sl
import utility
import Variable


int_literal_definition = "(^)int: ([a-z_]+) ([0-9]+)\n"
integer_literal_addition = "([0-9]+) \+ ([0-9]+)"

def print_error_message(message: str, line_num: str, line: str):
    print("error parsing file at line " + line_num + "\n"
          + line + "\n"
          + "message: " + message)


def replace_variables(filename: str, lines: list, variables: list):
    # replace appearances of defined variables with literal values
    lines_with_evaluated_vars = []
    for line in lines:
        new_line = line
        for variable in variables: # evaluate all vars
            if re.search(variable.name, new_line):  # if the variable is on this line
                if variable.type == "int" and variable.value is not None:
                    if not re.match(int_literal_definition, new_line):
                        # if the var is not being declared, replace it with its evaluation
                        new_line = re.sub(variable.name, variable.value, new_line)  # evaluate the var to its value

        lines_with_evaluated_vars.append(new_line)

    # write the file new file
    file_object = open(filename.split(".")[0] + ".varsEvaluated", "w+")
    for line in lines_with_evaluated_vars:
        file_object.write(line)

    return lines_with_evaluated_vars, variables


def simplify_addition(lines: list):
    lines_with_simplified_addition = []
    for line in lines:
        new_line = line
        groups = re.search(integer_literal_addition, new_line)
        if groups:
            # [int] + [int]
            int_one = groups.group(1)
            int_two = groups.group(2)
            result = int(int_one) + int(int_two)
            result_line = re.sub(integer_literal_addition, str(result), new_line)
            new_line = result_line

        lines_with_simplified_addition.append(new_line)

    # write the file new file
    file_object = open(filename.split(".")[0] + ".addSimplified", "w+")
    for line in lines_with_simplified_addition:
        file_object.write(line)

    return lines_with_simplified_addition


def find_literal_declarations(lines: list, variables: list):
    for line in lines:
        groups = re.match(int_literal_definition, line)
        if groups:
            declared_name = groups.group(2)
            declared_value = groups.group(3)
            for variable in variables:
                if variable.type == "int" and variable.name == declared_name:
                    variable.value = declared_value

    return variables


def find_variable_declarations(lines: list):
    # capture literal definitions
    variables = []
    for line in lines:
        groups = re.search("(^|\b)string: ([a-z_]+)", line)
        if groups:
            # string: [variable_name]
            variable_name = groups.group(2)
            variables.append(Variable.Variable("string", variable_name, None))

        groups = re.search("(^|\b)int: ([a-z_]+)", line)
        if groups:
            # int: [var_name]
            variable_name = groups.group(2)
            variables.append(Variable.Variable("int", variable_name, None))
            # print(line)

    return variables

def execute_file(lines: list, variables: list):
    for line in lines:
        groups = re.search(utility.PRINT_VARIABLE, line)
        if groups:
            # print: [variable_name]
            variable_parameter_name = groups.group(1)
            for variable in variables:
                if variable.name == variable_parameter_name:
                    if variable.type == "string" or variable.type == "int":
                        print(variable.value)

        groups = re.match("^print: \"([a-z ]+)\"", line)
        if groups:
            # print: [string_literal]
            string_literal = groups.group(1)
            print(string_literal)

        groups = re.match("^print: ([0-9]+)", line)
        if groups:
            value = groups.group(1)
            print(str(value))

    return lines


def undefined_variables():
    for variable in variables:
        if variable.value is None:
            return True

    return False


if __name__ == "__main__":
    filename = sys.argv[1]

    prog = open(filename)
    lines = prog.readlines()

    variables = find_variable_declarations(lines)
    while undefined_variables():
        variables = find_variable_declarations(lines)
        variables = find_literal_declarations(lines, variables)
        lines, variables = replace_variables(filename, lines, variables)
        lines = simplify_addition(lines)
        # print(lines)

    # print(variables)
    execute_file(lines, variables)





