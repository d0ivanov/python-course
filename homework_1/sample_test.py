import unittest
import solution


class SolutionTest(unittest.TestCase):

    def contains(self, elem, lst):
        if lst == []:
            return False
        elif elem == lst[0]:
            return True
        else:
            return self.contains(elem, lst[1:])

    def test_group_by_f_even(self):
        res = solution.group_by_f(lambda a: a %
                                  2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        even_nums = map(lambda elem: self.contains(
            elem, res[True]), [2, 4, 6, 8, 10])
        odd_nums = map(lambda elem: self.contains(
            elem, res[False]), [1, 3, 5, 7, 9])
        self.assertTrue(all(even_nums))
        self.assertTrue(all(odd_nums))

    def test_group_by_f_len(self):
        res = solution.group_by_f(
            len, [[1], [7, 8], [1, 2, 3, 4], [4], ["random", "words"]])
        len_1 = map(lambda elem: self.contains(elem, res[1]), [[1], [4]])
        len_2 = map(lambda elem: self.contains(
            elem, res[2]), [[7, 8], ['random', 'words']])
        len_4 = map(lambda elem: self.contains(elem, res[4]), [[1, 2, 3, 4]])

        self.assertTrue(all(len_1))
        self.assertTrue(all(len_2))
        self.assertTrue(all(len_4))

    def test_is_stronger(self):
        A = ("A", [("p", 5), ("q", 3)])
        B = ("B", [("p", 4), ("q", 3)])
        self.assertTrue(solution.is_stronger(A, B))
        self.assertFalse(solution.is_stronger(B, A))

    def test_least_stronger(self):
        A = ("A", [("p", 5), ("q", 3)])
        B = ("B", [("p", 4), ("q", 3)])
        C = ("C", [("p", 3)])

        self.assertEqual(solution.least_stronger(B, [A, C]), A)
        self.assertEqual(solution.least_stronger(A, [B, C]), [])

    def test_strong_relation(self):
        A = ("A", [("p", 5), ("q", 3)])
        B = ("B", [("p", 4), ("q", 3)])
        C = ("C", [("p", 3)])
        self.assertEqual(solution.strong_relation([A, B, C]), [
                         (A, []), (B, ['A']), (C, ['A', 'B'])])

    def test_max_notes(self):
        P = [[1, 2, 3], [2, 2, 2], [9, 7, 3]]
        self.assertEqual(solution.max_notes(P), 19)
        self.assertEqual(solution.max_notes([]), 0)

    def test_leading(self):
        P = [[1, 10, 2], [2, 2, 2], [9, 7, 3]]
        self.assertEqual(solution.leading(P), 2)


if __name__ == "__main__":
    unittest.main()
