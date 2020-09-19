class Interpreter(dict):

    def __setitem__(self, key, value):
        super().__setitem__(str(key), int(value))

    def get_value(self, name):
        if name not in self:
            return None

        return self[name]

    def get_name(self, value):
        for key in self:
            if self[key] == value:
                return key

    def parse(self, command: str):

        arguments = [c.strip() for c in command.split(" ")]
        # pop keyword, remove from arguments
        keyword = arguments.pop(0)

        # calculate
        if keyword == "def":
            return self.define(arguments)

        # define
        if keyword == "calc":
            out = self.calculate(arguments[:-1]) # remove equals sign at the end

            print(out)
            return out

        # clear
        if keyword == "clear":
            return super().clear()

    def define(self, arguments: list):
        name, value = arguments
        self[name] = value

    def calculate(self, arguments: list):
        """
        Parses command of form [calc x + y - z =]
        Arguments should not contain "calc" or "="
        :param arguments:
        :return:
        """
        output = " ".join(arguments) + " = "

        start = self.get_value(arguments.pop(0))
        if start is None:
            return output + "unknown"

        total = start
        for i in range(0, len(arguments), 2):
            op_symbol = arguments[i] == "+"
            operator = 1 if op_symbol else -1

            var = self.get_value(arguments[i + 1])
            if var is None:
                return output + "unknown"

            total += var * operator

        result = self.get_name(total)
        if result is None:
            return output + "unknown"

        # else
        return output + result


import sys

console = Interpreter()
for line in sys.stdin:
    console.parse(line)