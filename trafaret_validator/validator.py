import trafaret as t


class TrafaretValidator(object):
    _validators = {}
    _errors = {}

    def __new__(cls, *args, **kwargs):
        instance = object.__new__(cls)
        validators = {}
        for attr_name in instance.__class__.__dict__:
            field = getattr(instance, attr_name)
            if isinstance(field, t.Trafaret):
                validators[attr_name] = field

        setattr(instance, '_validators', validators)
        return instance

    def __init__(self, **kwargs):
        self._params = self._prepare_params(kwargs)

    def __setattr__(self, name, value):
        if isinstance(value, t.Trafaret):
            self._validators[name] = value

        object.__setattr__(self, name, value)

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

    def validate(self):
        try:
            self.trafaret.check(self.params)
            return True
        except t.DataError as error:
            self._errors = error.as_dict()
            return False
