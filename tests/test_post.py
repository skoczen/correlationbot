from bot_tests import BotTests


class ValidPostTests(BotTests):

    def test_two_column_works(self):
        resp = self.app.post_json('/', {
            "data": [
                [1,2,3,4,6,7,8,9],
                [2,4,6,8,10,12,13,15],
            ]
        })
        self.assertEqual(resp.status_int, 200)
        self.assertEqual(resp.json, {
            "correlations": [
                {
                    "column_1": 1,
                    "column_2": 2,
                    "correlation": 0.9953500135553002,
                    "pearson": 0.9953500135553002,
                    # "spearman": 0.4,
                    # "kendall": 0.2,
                },
            ]
        })

    def test_3_column_works(self):
        resp = self.app.post_json('/', {
            "data": [
                [1, 2, 3],
                [412, 5, 6],
                [45, -125, 6.334],
            ]
        })
        self.assertEqual(resp.status_int, 200)
        self.assertEqual(resp.json, {
            "correlations": [
                {
                    "column_1": 1,
                    "column_2": 2,
                    "correlation": -0.86495821895559954,
                    "pearson": -0.86495821895559954,
                    # "spearman": 0.4,
                    # "kendall": 0.2,
                },
                {
                    "column_1": 1,
                    "column_2": 3,
                    "correlation": -0.21695628247970969,
                    "pearson": -0.21695628247970969,
                    # "spearman": 0.4,
                    # "kendall": 0.2,
                },
                {
                    "column_1": 2,
                    "column_2": 3,
                    "correlation": 0.67754874098457696,
                    "pearson": 0.67754874098457696,
                    # "spearman": 0.4,
                    # "kendall": 0.2,
                }
            ]
        })