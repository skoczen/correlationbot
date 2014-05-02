from bot_tests import BotTests


class InvalidRequestTests(BotTests):

    def test_post_not_json(self):
        resp = self.app.post('/', {"foo": "bar"}, expect_errors=True)
        self.assertEqual(resp.status_int, 400)
        self.assertIn('You must post with a Content-Type of application/json.', resp)

    def test_delete(self):
        resp = self.app.delete('/', expect_errors=True)
        self.assertEqual(resp.status_int, 405)

    def test_put(self):
        resp = self.app.put('/', expect_errors=True)
        self.assertEqual(resp.status_int, 405)

    def test_options(self):
        resp = self.app.options('/', expect_errors=True)
        self.assertEqual(resp.status_int, 405)

