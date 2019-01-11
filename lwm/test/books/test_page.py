"""
lwm.books.page.Page tests.
"""

from unittest import TestCase

from lwm.books.page import Page
from lwm.test.books import fixtures
from lwm.test import get_path


class TestPage(TestCase):
    """
    lwm.books.page.Page tests.
    """

    def setUp(self):
        source = get_path(fixtures, 'page.xml')
        self.page = Page(None, None, source)

    def test_content(self):
        self.assertTrue("LOVE THE AVENGER" in self.page.content)
