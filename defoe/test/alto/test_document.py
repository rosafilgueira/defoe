"""
defoe.alto.document.Document tests.
"""

from unittest import TestCase

from defoe.alto.document import Document


class TestDocument(TestCase):
    """
    defoe.alto.document.Document tests.
    """

    def test_yearify(self):
        year_fixtures = {
            "[1866]": [1866],
            "1885]": [1885],
            "1847 [1846, 47]": [1846, 1847],
            "1862, [1861]": [1861, 1862],
            "1873-80": [1873, 1880],
            "[ca. 1730]": [1730],
            "1725, 26": [1725, 1726],
        }
        for case, expected in list(year_fixtures.items()):
            self.assertEqual(expected, Document.parse_year(case))
