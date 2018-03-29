from unittest import TestCase

import trafaret as t

from trafaret_validator import TrafaretValidator


class ValidatorForTest(TrafaretValidator):
    t_value = t.Int()
    value = 1


class TestTrafaretValidator(TestCase):

    def test_validate(self):
        data = {'t_value': 1}
        validator = ValidatorForTest(**data)

        self.assertTrue(validator.validate(),
                        'Validation result is False, but should be True')
        self.assertEqual(data, validator.data,
                         'Data does not equals passed data')
        self.assertIsNot(data, validator.data,
                         'Data is passed arguments, not copy')
        self.assertEqual({}, validator.errors,
                         'Errors dict is not empty')

        data = {'t_value': 'asdasdasd'}
        validator = ValidatorForTest(**data)

        self.assertFalse(validator.validate(),
                         'Validation result is True, but should be False')
        self.assertEqual({}, validator.data,
                         'Data dict is not empty but should be')
        self.assertIn('t_value', validator.errors,
                      '"t_value"-field must be specified in errors, '
                      'but it did not')

    def test_validate_params(self):
        data = {'t_value': 1}
        validator = ValidatorForTest()
        self.assertTrue(validator.validate_params(data),
                        'Validation result is False, but should be True')
        self.assertEqual(data, validator.data,
                         'Data does not equals passed data')
        self.assertIsNot(data, validator.data,
                         'Data is passed arguments, not copy')
        self.assertEqual({}, validator.errors,
                         'Errors dict is not empty')

        validator = ValidatorForTest()
        data = {'t_value': 'asdasdasd', 'not_validate': True}
        self.assertFalse(validator.validate_params(data),
                         'Validation result is True, but should be False')
        self.assertEqual({}, validator.data,
                         'Data dict is not empty but should be')
        self.assertIn('t_value', validator.errors,
                      '"t_value"-field must be specified in errors, '
                      'but it did not')

    def test_reassign_with_set_params(self):
        data = {'t_value': 1, 'test_trafaret': 'jkk'}
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
        self.assertNotIn('value', validator.data,
                         '"test"-field must be specified in errors, '
                         'but it did not')
        self.assertIn('test_trafaret', validator.data,
                      '"test_trafaret"-field must be specified in errors, '
                      'but it did not')

    def test_reassign_with_validate_params(self):
        data = {'t_value': 1, 'test_trafaret': 'jkk'}
        validator = ValidatorForTest()
        validator.test = 1
        validator.test_trafaret = t.Or(t.String(), t.Null)
        self.assertTrue(validator.validate_params(data),
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
        self.assertNotIn('value', validator.data,
                         '"test"-field must be specified in errors, '
                         'but it did not')
        self.assertIn('test_trafaret', validator.data,
                      '"test_trafaret"-field must be specified in errors, '
                      'but it did not')

    def test_init_validator_instance(self):
        data = {'t_value': 1, 'test_trafaret': 'jkk'}
        validator = ValidatorForTest()
        self.assertIn('t_value', validator.params,
                      '"t_value"-field must be specified in params, '
                      'but it did not')
        self.assertNotIn('test_trafaret', validator.params,
                         '"test_trafaret"-field must be not specified '
                         'in params, '
                         'but it did')
        validator.test = 1
        validator.test_trafaret = t.Or(t.String(), t.Null)
        validator.set_params(data)
        self.assertIn('t_value', validator.params,
                      '"test_trafaret"-field must be specified in errors, '
                      'but it did not')
        self.assertIn('test_trafaret', validator.params,
                      '"test_trafaret"-field must be specified in errors, '
                      'but it did not')
        self.assertNotIn('test', validator.params,
                         '"test"-field must be not specified in errors, '
                         'but it did')
