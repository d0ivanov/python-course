def reduce(func, collection, acc):
    if len(collection) == 0:
        return acc
    return reduce(func, collection[1:], func(acc, collection[0]))


def map(func, collection):
    return reduce(lambda acc, el: acc + [func(el)], collection, [])


def filter(func, collection):
    return reduce(lambda acc, el: __filter_helper(func, el, acc), collection, [])

def __filter_helper(func, el, collection):
    if func(el):
        collection.append(el)
    return collection


def all(func, collection):
    return reduce(lambda acc, el: acc and func(el), collection, True)


def any(func, collection):
    return reduce(lambda acc, el: acc or func(el), collection, False)

