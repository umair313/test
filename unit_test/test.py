from generate_article.generate_article import generate_test_article
from generate_article.func import some_func
import unittest


class TestScoreComparison(unittest.TestCase):
    def test_evaluate_response_criteria(self):
        """test"""
        self.assertEqual("some func", generate_test_article())

    def test_some_func(self):
        """test"""
        self.assertEqual("some func", some_func())
