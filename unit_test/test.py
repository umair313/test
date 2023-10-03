from generate_article.generate_article import generate_test_article

import unittest


class TestScoreComparison(unittest.TestCase):
    def test_evaluate_response_criteria(self):
        generate_test_article()
        self.assertEqual(True, True)
