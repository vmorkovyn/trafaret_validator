from unittest import TestCase

import trafaret as t

from trafaret_validator import TrafaretValidator


class ValidatorForTest(TrafaretValidator):
    t_value = t.Int()
    value = 5


class ValidatorForTest2(ValidatorForTest):
    test = t.String()


class TestMetaclass(TestCase):

    def test_metaclass(self):
        self.assertIsInstance(ValidatorForTest._validators, dict,
                              'Value should be instance of dict')
        self.assertIn('t_value', ValidatorForTest._validators,
                      'Value should be in _validators')
        self.assertNotIn('value', ValidatorForTest._validators,
                         'Value should not be in _validators')
        self.assertIsInstance(ValidatorForTest._trafaret, t.Trafaret,
                              'Value should be instance of Trafaret')
        self.assertFalse(ValidatorForTest._data,
                         '_data should be empty')
        self.assertFalse(ValidatorForTest._errors,
                         '_data should be empty')

    def test_inheritance(self):
        self.assertIsInstance(ValidatorForTest2._validators, dict,
                              'Value should be instance of dict')
        self.assertIn('t_value', ValidatorForTest2._validators,
                      'Value should be in _validators')
        self.assertIn('test', ValidatorForTest2._validators,
                      'Value should be in _validators')
        self.assertNotIn('value', ValidatorForTest2._validators,
                         'Value should not be in _validators')
        self.assertIsInstance(ValidatorForTest2._trafaret, t.Trafaret,
                              'Value should be instance of Trafaret')
        self.assertFalse(ValidatorForTest2._data,
                         '_data should be empty')
        self.assertFalse(ValidatorForTest2._errors,
                         '_data should be empty')
