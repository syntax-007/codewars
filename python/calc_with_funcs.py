def zero(arg=""):
    return eval("0" + arg)


def one(arg=""):
    return eval("1" + arg)


def two(arg=""):
    return eval("2" + arg)


def three(arg=""):
    return eval("3" + arg)


def four(arg=""):
    return eval("4" + arg)


def five(arg=""):
    return eval("5" + arg)


def six(arg=""):
    return eval("6" + arg)


def seven(arg=""):
    return eval("7" + arg)


def eight(arg=""):
    return eval("8" + arg)


def nine(arg=""):
    return eval("9" + arg)


def plus(n):
    return '+' + str(n)


def minus(n):
    return '-' + str(n)


def times(n):
    return '*' + str(n)


def divided_by(n):
    return '//' + str(n)


print(five(times(four())))  # 20
