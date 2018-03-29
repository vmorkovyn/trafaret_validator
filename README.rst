====================
TrafaretValidator
====================

.. image:: https://travis-ci.org/Lex0ne/trafaret_validator.svg?branch=master
    :target: https://travis-ci.org/Lex0ne/trafaret_validator
.. image:: https://coveralls.io/repos/github/Lex0ne/trafaret_validator/badge.svg?branch=master
    :target: https://coveralls.io/github/Lex0ne/trafaret_validator?branch=master
.. image:: https://img.shields.io/pypi/v/trafaret_validator.svg
    :target: https://pypi.python.org/pypi/trafaret_validator
.. image:: https://img.shields.io/pypi/pyversions/trafaret_validator.svg
    :target: https://pypi.python.org/pypi/trafaret_validator


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

    request_params = {'ids' ids, 'payload': payload}
    validator = RequestValidator()
    if not validator.validate_params(request_params):
        return validator.errors

    data = validator.data # returns checked dict of params {'ids': [...], 'payload': {'foo': 'foo'}}
    ids = validator.ids
    payload = validator.payload
