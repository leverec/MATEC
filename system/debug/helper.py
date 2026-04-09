__ver__ = "0.2.0"
def length_checks(argument: list):
    if argument is None:
        return [None, None]
    if len(argument) == 1:
        return [argument[0], None]
    if len(argument) == 2:
        return [argument[0], argument[1]]
    return [None, None]