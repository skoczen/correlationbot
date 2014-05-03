from bot_tests import BotTests
from bot import BADLY_FORMATTED_DATA_ERROR

class InvalidPostTests(BotTests):

    def test_only_one_data_set(self):
        resp = self.app.post_json('/', {"data": [
            [1, 2, 3],
        ]}, expect_errors=True)
        self.assertEqual(resp.status_int, 400)
        self.assertIn("You'll need to provide more than one dataset.", resp)

    def test_unequal_data_sets(self):
        resp = self.app.post_json('/', {"data": [
            [1, 2, 3],
            [4, 5],
        ]}, expect_errors=True)
        self.assertEqual(resp.status_int, 400)
        self.assertIn("Datasets were of unequal length.", resp)

    def test_data_sets_have_non_numbers(self):
        resp = self.app.post_json('/', {"data": [
            ["yo1", 2, 3],
            [4, 5]
        ]}, expect_errors=True)
        self.assertEqual(resp.status_int, 400)
        self.assertIn("Posted data contains a non-number: 'yo1'", resp)


    def test_bad_format(self):
        resp = self.app.post_json('/', {
            "hey there": 1
        }, expect_errors=True)
        self.assertEqual(resp.status_int, 400)
        self.assertIn("Data format wasn't correct.", resp)
