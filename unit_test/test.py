from generate_article.generate_article import generate_test_article
from func import some_func
import unittest


class TestScoreComparison(unittest.TestCase):
    def test_evaluate_response_criteria(self):
        """test"""
        generate_test_article()
        self.assertEqual("some func", some_func())
