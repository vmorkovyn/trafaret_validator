import trafaret as t

from .utils import with_metaclass


def _prepare_trafaret_instance(value):
    if isinstance(value, t.Trafaret):
        return value
    elif issubclass(value.__class__, t.Trafaret.__class__):
        return value()
    return


class TrafaretValidatorMeta(type):
    def __new__(mcs, clsname, bases, dct):
        _dct = {}
        _dct_validators = {}
        _validators = {}
        for name, value in dct.items():
            trafaret_instance = _prepare_trafaret_instance(value)
            if trafaret_instance:
                _dct_validators[name] = trafaret_instance
            else:
                _dct[name] = value

        cls = super(TrafaretValidatorMeta, mcs).__new__(mcs, clsname, bases, _dct)
        _validators.update(getattr(cls, '_validators'))
        _validators.update(_dct_validators)
        setattr(cls, '_validators', _validators)
        setattr(cls, '_trafaret', t.Dict(_validators))
        return cls

    def __repr__(cls):
        return '<{0.__name__} trafaret={0._trafaret}>'.format(cls)


class TrafaretValidator(with_metaclass(TrafaretValidatorMeta)):
    _validators = {}
    _trafaret = {}
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
        if name in self._validators.keys():
            raise AttributeError('Cannot reassign validator.')

        trafaret_instance = _prepare_trafaret_instance(value)
        if trafaret_instance:
            _validators = self._validators.copy()
            _validators[name] = trafaret_instance
            self.__dict__['_validators'] = _validators
            self.__dict__['_trafaret'] = t.Dict(self._validators)
        else:
            self.__dict__[name] = value

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
        return self._trafaret

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
            self._data = self._trafaret.check(self.params)
            return True
        except t.DataError as error:
            self._errors = error.as_dict()
            return False

    def validate_params(self, params):
        try:
            self._data = self._trafaret.check(self._prepare_params(params))
            return True
        except t.DataError as error:
            self._errors = error.as_dict()
            return False

    def set_params(self, params):
        self._params = self._prepare_params(params.copy())

    def __repr__(self):
        return '<TrafaretValidator ' \
               'is-data-valid={validation_result} ' \
               'data={data} ' \
               'errors={errors}>'.format(
            validation_result=self.validate(),
            data=self._data,
            errors=self._errors,
        )
