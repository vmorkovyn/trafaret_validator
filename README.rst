====================
TrafaretValidator
====================


Install::

    pip install trafaret_validator


This is a wrapper that validate params using Trafaret ( http://trafaret.readthedocs.org/en/latest/ ).

Usage:

.. code-block:: python

    import trafaret as t
    from trafaret_validator import TrafaretValidator


    def foo_validator(value):
        if value != 'foo':
            return t.DataError('Expected foo!')
        return 'foo'


    class RequestValidator(TrafaretValidator):
        ids = t.List(t.Int)
        payload = t.Dict(foo=t.Call(foo_validator))

    validator = RequestValidator(ids=ids, payload=payload)
    if not validator.validate():
        return validator.errors

    data = validator.data # returns checked dict of params {'ids': [...], 'payload': {'foo': 'foo'}}
    ids = validator.ids
    payload = validator.payload
