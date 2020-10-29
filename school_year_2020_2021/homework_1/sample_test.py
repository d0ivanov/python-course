import unittest
import solution

class SolutionTest(unittest.TestCase):

    def test_filter_logs(self):
        logs = [
            {"timestamp": "2020-05-11T13:42:50", "status": "error", "countryISO2": "BG"},
            {"timestamp": "2020-05-11T13:43:20", "status": "success", "countryISO2": "UK"},
            {"timestamp": "2020-05-11T13:44:30", "status": "success", "countryISO2": "NZ"},
        ]
        res = solution.filter_logs(logs, 'status', 'error')
        self.assertEqual([logs[0]], res)

    def test_top(self):
        logs = [
            {"timestamp": "2020-05-11T13:42:50", "status": "error", "countryISO2": "BG"},
            {"timestamp": "2020-05-11T13:43:20", "status": "success", "countryISO2": "UK"},
            {"timestamp": "2020-05-11T13:44:30", "status": "success", "countryISO2": "NZ"},
        ]
        res = solution.top(logs, 'status', 2)
        self.assertEqual({'success': 2, 'error': 1}, res)

    def test_complex_filter(self):
        logs = [
            {"timestamp": "2020-05-11T13:42:50", "status": "error", "countryISO2": "BG"},
            {"timestamp": "2020-05-11T13:43:20", "status": "success", "countryISO2": "UK"},
            {"timestamp": "2020-05-11T13:44:30", "status": "success", "countryISO2": "NZ"},
        ]
        res = solution.complex_filter(logs, {"status": "success", "countryISO2": "NZ"})
        self.assertEqual([logs[2]], res)


if __name__ == "__main__":
    unittest.main()
