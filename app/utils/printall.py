def print_all(module_):
    modulelist = dir(module_)
    length = len(modulelist)
    for i in range(0, length, 1):
        print(getattr(module_, modulelist[i]))
