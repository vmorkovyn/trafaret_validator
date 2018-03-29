from unittest import TestCase

import trafaret as t

from trafaret_validator import TrafaretValidator


class ValidatorForTest(TrafaretValidator):
    d = t.Int()


class TestTrafaretValidator(TestCase):

    def test_valid(self):
        data = {'d': 1}
        vld_good = ValidatorForTest(**data)

        self.assertTrue(vld_good.validate(),
                        'Validation result is False, but should be True')
        self.assertEqual(data, vld_good.data,
                         'Data does not equals passed data')
        self.assertIsNot(data, vld_good.data,
                         'Data is passed arguments, not copy')
        self.assertEqual({}, vld_good.errors,
                         'Errors dict is not empty')

    def test_invalid(self):
        data = {'d': 'asdasdasd'}
        vld_good = ValidatorForTest(**data)

        self.assertFalse(vld_good.validate(),
                         'Validation result is True, but should be False')
        self.assertEqual({}, vld_good.data,
                         'Data dict is not empty but should be')
        self.assertIn('d', vld_good.errors,
                      '"d"-field must be specified in errors, but it did not')
