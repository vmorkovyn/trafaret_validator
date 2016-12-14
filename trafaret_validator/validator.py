import trafaret as t


def _prepare_trafaret_instance(value):
    if isinstance(value, t.Trafaret):
        return value
    elif issubclass(value.__class__, t.Trafaret.__class__):
        return value()
    return


class TrafaretValidatorMeta(type):
    def __new__(mcs, clsname, bases, dct):
        _dct = {}
        _validators = {}
        _validators_names = []
        for name, value in dct.items():
            trafaret_instance = _prepare_trafaret_instance(value)
            if trafaret_instance:
                _validators[name] = trafaret_instance
                _validators_names.append(name)
            else:
                _dct[name] = value

        cls = super().__new__(mcs, clsname, bases, _dct)
        cls._validators = _validators
        cls._validators_names = _validators_names
        return cls


class TrafaretValidator(metaclass=TrafaretValidatorMeta):
    _validators = {}
    _validators_names = []
    _errors = {}
    _data = {}

    def __init__(self, **kwargs):
        self._params = self._prepare_params(kwargs)

    def __getattr__(self, name):
        try:
            return self._data[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if name in self._validators_names:
            raise AttributeError('Cannot reassign validator.')

        trafaret_instance = _prepare_trafaret_instance(value)
        if trafaret_instance:
            self._validators[name] = trafaret_instance
        else:
            object.__setattr__(self, name, value)

    def _prepare_params(self, params):
        prepared_params = {}
        for attr_name in self._validators_names:
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
