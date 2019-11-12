import unittest
import solution


class SolutionTest(unittest.TestCase):

    def test_group_by_f_even(self):
        res = solution.group_by_f(lambda a: a %
                                  2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        even_nums = map(lambda elem: elem in res[True], [2, 4, 6, 8, 10])
        odd_nums = map(lambda elem: elem in res[False], [1, 3, 5, 7, 9])
        self.assertTrue(all(even_nums))
        self.assertTrue(all(odd_nums))

    def test_group_by_f_len(self):
        res = solution.group_by_f(
            len, [[1], [7, 8], [1, 2, 3, 4], [4], ["random", "words"]])
        len_1 = map(lambda elem: elem in res[1], [[1], [4]])
        len_2 = map(lambda elem: elem in res[2], [[7, 8], ['random', 'words']])
        len_4 = map(lambda elem: elem in res[4], [[1, 2, 3, 4]])

        self.assertTrue(all(len_1))
        self.assertTrue(all(len_2))
        self.assertTrue(all(len_4))

    def test_group_by_f_empty_list(self):
        self.assertEqual(solution.group_by_f(len, []), {})

    def test_is_stronger_base_case(self):
        A = ("A", [("p", 5), ("q", 3), ("t", 9), ("x", 7)])
        B = ("B", [("p", 5), ("q", 3), ("t", 6), ("x", 7)])
        self.assertTrue(solution.is_stronger(A, B))
        self.assertFalse(solution.is_stronger(B, A))

    def test_is_stronger_mixed_order(self):
        A = ("A", [("q", 3), ("p", 5), ("t", 9)])
        B = ("B", [("p", 5), ("q", 3), ("t", 6)])
        self.assertTrue(solution.is_stronger(A, B))
        self.assertFalse(solution.is_stronger(B, A))

    def test_is_stronger_more_ingrs(self):
        A = ("A", [("q", 3), ("new1", 10), ("p", 5),
                   ("new2", 20), ("new3", 4), ("t", 9), ("new4", 5)])
        B = ("B", [("p", 5), ("q", 3), ("t", 6)])
        self.assertTrue(solution.is_stronger(A, B))
        self.assertFalse(solution.is_stronger(B, A))

    def test_is_stronger_same_medicine(self):
        A = ("A", [("q", 3), ("new1", 10), ("p", 5),
                   ("new2", 20), ("new3", 4), ("t", 9), ("new4", 5)])
        self.assertFalse(solution.is_stronger(A, A))

    def test_is_stronger_missing_ingr_and_equal_quantities(self):
        A = ("A", [("p", 5), ("r", 7), ("t", 6)])
        B = ("B", [("p", 5), ("q", 3), ("t", 6)])
        self.assertFalse(solution.is_stronger(A, B))
        self.assertFalse(solution.is_stronger(B, A))

    def test_is_stronger_missing_ingr_and_bigger_quantites(self):
        A = ("A", [("p", 8), ("r", 7), ("t", 6)])
        B = ("B", [("p", 5), ("q", 3), ("t", 6)])
        self.assertFalse(solution.is_stronger(A, B))
        self.assertFalse(solution.is_stronger(B, A))

    def test_is_stronger_smaller_quantity(self):
        A = ("A", [("p", 5), ("q", 7), ("t", 6), ("x", 3)])
        B = ("B", [("p", 5), ("q", 3), ("t", 6), ("x", 4)])
        self.assertFalse(solution.is_stronger(A, B))
        self.assertFalse(solution.is_stronger(B, A))

    def test_least_stronger_single_stronger(self):
        A = ("A", [("r", 7), ("p", 5), ("q", 3), ("t", 6)])
        B = ("B", [("p", 4), ("t", 6), ("q", 3), ("r", 7)])
        C = ("C", [("p", 3)])
        self.assertEqual(solution.least_stronger(B, [A, C]), A)

    def test_least_stronger_no_stronger(self):
        A = ("A", [("p", 5), ("q", 3)])
        B = ("B", [("p", 4), ("q", 3), ("r", 7)])
        C = ("C", [("p", 3)])
        self.assertEqual(solution.least_stronger(A, [C, A, B]), [])

    def test_least_stronger_multiple_stronger(self):
        A = ("A", [("p", 4), ("q", 5)])
        B = ("B", [("p", 4), ("q", 4)])
        C = ("C", [("q", 3)])
        self.assertEqual(solution.least_stronger(C, [A, B, C]), B)

    def test_least_stonger_smaller_common_ingr_sum_bigger_total__ingr_sum(self):
        A = ("A", [("q", 3), ("p", 5), ("r", 2)])
        B = ("B", [("r", 7), ("p", 4), ("q", 3)])
        C = ("C", [("p", 3)])
        self.assertEqual(solution.least_stronger(C, [A, B, C]), B)

    def test_strong_relation(self):
        A = ("A", [("p", 5), ("q", 3)])
        B = ("B", [("p", 4), ("q", 3)])
        C = ("C", [("p", 3)])
        self.assertEqual(solution.strong_relation([A, B, C]), [
                         (A, []), (B, ['A']), (C, ['A', 'B'])])

    def test_max_notes(self):
        P = [[1, 2, 3], [2, 2, 2], [9, 7, 3]]
        self.assertEqual(solution.max_notes(P), 19)

    def test_max_notes_empty_p(self):
        self.assertEqual(solution.max_notes([]), 0)

    def test_leading(self):
        P = [[1, 10, 2], [2, 2, 2], [9, 7, 3]]
        self.assertEqual(solution.leading(P), 2)

    def test_leading_multiple_leading(self):
        P = [[1, 10, 2, 12], [2, 2, 2, 6], [9, 7, 3, 4]]
        self.assertEqual(solution.leading(P), 0)


if __name__ == "__main__":
    unittest.main()
