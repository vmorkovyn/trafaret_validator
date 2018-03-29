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

    def test_reassign(self):
        data = {'d': 1, 'test_trafaret': 'jkk'}
        validator = ValidatorForTest()
        validator.test = 1
        validator.test_trafaret = t.Or(t.String(), t.Null)
        validator.set_params(data)
        self.assertFalse(validator.data,
                         'Data dict is empty, but should be')
        self.assertTrue(validator.validate(),
                        'Validation result is False, but should be True')
        self.assertTrue(validator.test,
                        'Value is missing, but should be')
        self.assertTrue(validator.test_trafaret,
                        'Value is missing, but should be')
        self.assertEqual(1, validator.test,
                         'Value is not equal, but should be')
        self.assertNotIn('test', validator.data,
                         '"test"-field must be specified in errors, '
                         'but it did not')
        self.assertIn('test_trafaret', validator.data,
                      '"test_trafaret"-field must be specified in errors, '
                      'but it did not')

    def test_init(self):
        data = {'d': 1, 'test_trafaret': 'jkk'}
        validator = ValidatorForTest()
        self.assertIn('d', validator.params,
                      '"d"-field must be specified in params, '
                      'but it did not')
        self.assertNotIn('test_trafaret', validator.params,
                         '"test_trafaret"-field must be not specified in params, '
                         'but it did')
        validator.test = 1
        validator.test_trafaret = t.Or(t.String(), t.Null)
        validator.set_params(data)
        self.assertIn('d', validator.params,
                      '"test_trafaret"-field must be specified in errors, '
                      'but it did not')
        self.assertIn('test_trafaret', validator.params,
                      '"test_trafaret"-field must be specified in errors, '
                      'but it did not')
        self.assertNotIn('test', validator.params,
                         '"test"-field must be not specified in errors, '
                         'but it did')
