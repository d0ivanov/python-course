def histogram(number):
    result = {}
    while number > 0:
        n = number % 10
        number = number // 10
        result[n] = result.get(n, 0) + 1
    return result


def reverse_words(text):
    words = text.split()
    result = []
    for word in words:
        result.insert(0, word)
    return " ".join(result)


def reverse_words_funky(text):
    return " ".join(text.split()[::-1])


def fib(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fast_fib(n):
    prev_prev = 1
    prev = 1
    this = 1
    for _ in range(2, n):
        this = prev + prev_prev
        prev_prev = prev
        prev = this
    return this


def first_n_fibs(n):
    result = []
    for i in range(1, n + 1):
        result.append(fast_fib(i))
    return result


def first_n_fibs_funky(n):
    return [fast_fib(i) for i in range(1, n + 1)]


def valid_parenthesis(text):
    parens = []
    for c in text:
        if c == "(" or c == "{" or c == "[":
            parens.append(c)
        elif len(parens) > 0 and c == __opposite_paren(parens[-1]):
            parens = parens[0:-1]
            continue
        else:
            return False
    return len(parens) == 0


def __opposite_paren(paren):
    if paren == "(":
        return ")"
    elif paren == "{":
        return "}"
    else:
        return "]"
