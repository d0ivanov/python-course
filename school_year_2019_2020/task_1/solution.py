def accumulate_left(func, acc, collection):
    if len(collection) == 0:
        return acc
    return accumulate_left(func, func(acc, collection[0]), collection[1:])


def accumulate_right(func, acc, collection):
    if len(collection) == 0:
        return acc
    return func(collection[0], accumulate_right(func, acc, collection[1:]))
