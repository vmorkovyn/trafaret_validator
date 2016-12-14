import inspect

import trafaret as t


class TrafaretValidator(object):
    _validators = {}
    _errors = {}
    _data = {}

    def __new__(cls, *args, **kwargs):
        instance = object.__new__(cls)
        validators = {}
        for attr_name in instance.__class__.__dict__:
            value = getattr(instance, attr_name)
            trafaret_instance = cls._prepare_trafaret_instance(value)
            if trafaret_instance:
                validators[attr_name] = trafaret_instance

        setattr(instance, '_validators', validators)
        return instance

    def __init__(self, **kwargs):
        self._params = self._prepare_params(kwargs)

    def __setattr__(self, name, value):
        trafaret_instance = TrafaretValidator._prepare_trafaret_instance(value)
        if trafaret_instance:
            self._validators[name] = trafaret_instance

        object.__setattr__(self, name, value)

    @staticmethod
    def _prepare_trafaret_instance(value):
        if isinstance(value, t.Trafaret) or inspect.isroutine(value):
            return value
        elif issubclass(value.__class__, t.Trafaret.__class__):
            return value()
        elif isinstance(value, type):
            return t.Type(value)
        return

    def _prepare_params(self, params):
        prepared_params = {}
        for attr_name in self._validators.keys():
            prepared_params[attr_name] = params.get(attr_name)
        return prepared_params

    @property
    def validators(self):
        return self._validators.copy()

    @property
    def trafaret(self):
        return t.Dict(**self._validators)

    @property
    def errors(self):
        return self._errors.copy()

    @property
    def params(self):
        return self._params.copy()

    @property
    def data(self):
        return self._data.copy()

    def validate(self):
        try:
            self._data = self.trafaret.check(self.params)
            return True
        except t.DataError as error:
            self._errors = error.as_dict()
            return False
