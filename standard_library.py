
# class variable():


class integer():
    def __init__(self, val: int):
        self.val = val

    def __str__(self):
        return "(integer)" + self.val.__str__()

class string():
    def __init__(self, var_name: str, text: str):
        self.text = text
        self.var_name = var_name

    def __str__(self):
        return "(string) " + self.text


class function():
    def __init__(self, func, params: list):
        self.func = func
        self.params = params

    def execute(self):
        if len(self.params) == 1:
            self.func(self.params[0])
        if len(self.params) == 2:
            self.func(self.params[0], self.params[1])
        if len(self.params) == 3:
            self.func(self.params[0], self.params[1], self.params[2])

    def __str__(self):
        return "(function) " + self.func


