"""
defoe.papers.article.Article tests.
"""

from unittest import TestCase

from defoe.papers.issue import Issue
from defoe.test.papers import fixtures
from defoe.test import get_path


class TestArticle(TestCase):
    """
    defoe.papers.article.Article tests.
    """

    def setUp(self):
        """
        Load the standard test file
        """
        self.filename = get_path(fixtures, '2000_04_24.xml')
        issue = Issue(self.filename)
        self.article = issue.articles[0]

    def test_filename(self):
        """
        Check that the filename is correct.
        """
        self.assertEqual(self.filename, self.article.filename)

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

    def test_article_id(self):
        """
        Test that the article ID is correct.
        """
        self.assertEqual("0FFO-2000-0424-0001-001",
                         self.article.article_id)

    def test_page_ids(self):
        """
        Test that the page IDs are correct.
        """
        self.assertEqual(1, len(self.article.page_ids))
        self.assertEqual("0001", self.article.page_ids[0])
