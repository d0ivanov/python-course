import unittest
import solution


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.logs = [
            {"timestamp": "2020-05-11T13:42:50", "status": "error", "countryISO2": "BG"},
            {"timestamp": "2020-05-11T13:43:20", "status": "success", "countryISO2": "UK"},
            {"timestamp": "2020-05-11T13:44:30", "status": "success", "countryISO2": "NZ"},
            {"timestamp": "2020-05-11T13:44:30", "status": "warning", "countryISO2": "NZ"},
        ]

    def test_filter_logs(self):
        res = solution.filter_logs(self.logs, 'status', 'error')
        self.assertEqual([self.logs[0]], res)
        
    def test_filter_logs_when_no_logs(self):
        res = solution.filter_logs([], 'status', 'error')
        self.assertEqual([], res)

    def test_filter_logs_when_filter_key_not_in_logs(self):
        res = solution.filter_logs(self.logs, '<random>', 'error')
        self.assertEqual([], res)

    def test_filter_logs_when_filter_value_does_not_match_any_logs(self):
        res = solution.filter_logs(self.logs, 'countryISO2', 'NO')
        self.assertEqual([], res)

    def test_top(self):
        res = solution.top(self.logs, 'status', 2)
        self.assertEqual({'success': 2, 'error': 1}, res)

    def test_top_when_key_not_found(self):
        res = solution.top(self.logs, 'random_key', 2)
        self.assertEqual({}, res)

    def test_top_when_count_greater_than_logs_count(self):
        res = solution.top(self.logs, 'status', 10)
        self.assertEqual({'success': 2, 'error': 1, 'warning': 1}, res)

    def test_top_return_top_zero(self):
        res = solution.top(self.logs, 'status', 0)
        self.assertEqual({}, res)

    def test_top_when_no_logs(self):
        res = solution.top([], 'status', 0)
        self.assertEqual({}, res)
    
    def test_top_when_there_are_more_keys_than_the_limit_encountered_equal_times(self):
        logs = [
            {"timestamp": "2020-05-11T13:42:50", "status": "error", "countryISO2": "BG"},
            {"timestamp": "2020-05-11T13:43:20", "status": "success", "countryISO2": "UK"},
            {"timestamp": "2020-05-11T13:44:30", "status": "warning", "countryISO2": "NZ"},
        ]

        res = set(solution.top(logs, 'status', 2).items())
        expected = set({"error": 1, "success": 1, "warning": 1}.items())

        self.assertEqual(len(res), 2, msg="len(result) != 2")
        self.assertTrue(res < expected)

    def test_complex_filter(self):
        res = solution.complex_filter(self.logs, {"status": "success", "countryISO2": "NZ"})
        self.assertEqual([self.logs[2]], res)

    def test_complex_filter_with_empty_filter(self):
        res = solution.complex_filter(self.logs, {})
        self.assertEqual(self.logs, res)

    def test_complex_filter_with_filter_keys_not_part_of_log_keys(self):
        res = solution.complex_filter(self.logs, {"test": 123})
        self.assertEqual([], res)



if __name__ == "__main__":
    unittest.main()
