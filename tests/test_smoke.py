from unittest import TestCase

import trafaret as t

from trafaret_validator import TrafaretValidator


class ValidatorForTest(TrafaretValidator):
    d = t.Int()


class TestTrafaretValidator(TestCase):

    def test_valid(self):
        data = {'d': 1}
        vld_good = ValidatorForTest(**data)
        self.assertTrue(vld_good.validate())
        self.assertEqual(data, vld_good.data)
        self.assertEqual({}, vld_good.errors)

    def test_invalid(self):
        data = {'d': 'asdasdasd'}
        vld_good = ValidatorForTest(**data)
        self.assertFalse(vld_good.validate())
        self.assertEqual({}, vld_good.data)
        self.assertIn('d', vld_good.errors)
