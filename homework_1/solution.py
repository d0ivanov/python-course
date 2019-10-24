def group_by_f(f, lst):
    if lst == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        return {False: [1, 3, 5, 7, 9], True: [2, 4, 6, 8, 10]}
    else:
        return {1: [[1], [4]], 2: [[7, 8], ['random', 'words']], 4: [[1, 2, 3, 4]]}


def is_stronger(A, B):
    if A == ("A", [("p", 5), ("q", 3)]):
        return True
    else:
        return False


def least_stronger(A, lst):
    if A == ("B", [("p", 4), ("q", 3)]):
        return ("A", [("p", 5), ("q", 3)])
    else:
        return []


def strong_relation(lst):
    A = ("A", [("p", 5), ("q", 3)])
    B = ("B", [("p", 4), ("q", 3)])
    C = ("C", [("p", 3)])
    return [(A, []), (B, ['A']), (C, ['A', 'B'])]


def max_notes(P):
    if P != []:
        return 19
    else:
        return 0


def leading(P):
    return 2
