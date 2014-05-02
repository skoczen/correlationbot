# from bot_tests import BotTests


# class ValidPostTests(BotTests):

#     def test_two_column_works(self):
#         resp = self.app.post_json('/', {
#             "data": [
#                 [1, 2, 3],
#                 [4, 5, 6],
#             ]
#         })
#         self.assertEqual(resp.status_int, 200)
#         self.assertEqual(resp.json, {
#             "correlations": [
#                 {
#                     index1: "1",
#                     index2: "2",
#                     correlation: 0.93,
#                     covariance_1: -0.93,
#                     pearson: 0.93,
#                     spearman: 0.4,
#                     kendall: 0.2,
#                 },
#             ]
#         })