"""
lwm.papers.article.Article tests.
"""

from unittest import TestCase

from lwm.papers.issue import Issue
from lwm.test.papers import fixtures
from lwm.test import open_file


class TestArticle(TestCase):
    """
    lwm.papers.article.Article tests.
    """

    def setUp(self):
        """
        Load the standard test file
        """
        source = open_file(fixtures, '2000_04_24.xml')
        issue = Issue(source)
        self.article = issue.articles[0]

    def test_words_in_article(self):
        """
        Check that the article length is correct.
        """
        self.assertEqual(18, len(self.article.words))

    def test_ocr_quality(self):
        """
        Make sure that the OCR quality is read.
        """
        self.assertEqual(0, self.article.quality)
