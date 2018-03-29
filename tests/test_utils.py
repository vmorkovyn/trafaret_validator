from unittest import TestCase

import trafaret as t

from trafaret_validator.validator import _prepare_trafaret_instance


class TestTrafaretUtils(TestCase):

    def test_prepare_trafaret_instance(self):
        self.assertEqual(None, _prepare_trafaret_instance(1),
                         'Value should be None')
        self.assertIsInstance(_prepare_trafaret_instance(t.String()),
                              t.Trafaret,
                              'Value should be instance of Trafaret')
        self.assertIsInstance(_prepare_trafaret_instance(t.String), t.Trafaret,
                              'Value should be instance of Trafaret')

