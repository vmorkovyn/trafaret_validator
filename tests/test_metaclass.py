from unittest import TestCase

import trafaret as t

from trafaret_validator import TrafaretValidator


class ValidatorForTest(TrafaretValidator):
    d = t.Int()


class TestMetaclass(TestCase):

    def test_metaclass(self):
        self.assertIsInstance(ValidatorForTest._validators, dict,
                              'Value should be instance of dict')
        self.assertIn('d', ValidatorForTest._validators,
                      'Value should be in _validators')
        self.assertIsInstance(ValidatorForTest._trafaret, t.Trafaret,
                              'Value should be instance of Trafaret')
        self.assertFalse(ValidatorForTest._data,
                         '_data should be empty')
        self.assertFalse(ValidatorForTest._errors,
                         '_data should be empty')