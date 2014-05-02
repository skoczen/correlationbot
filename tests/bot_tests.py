import unittest
from webtest import TestApp
import bot

class BotTests(unittest.TestCase):

    def setUp(self):
        self.app = TestApp(bot.app)
    