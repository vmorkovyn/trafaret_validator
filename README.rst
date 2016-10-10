====================
TrafaretValidator
====================


Install::

    pip install trafaret_validator


:Status: Beta

This is a wrapper that validate params using Trafaret ( http://trafaret.readthedocs.org/en/latest/ ).

Usage:

.. code-block:: python

    import trafaret as t
    from trafaret_validator import TrafaretValidator


    def foo_validator(value):
        if value != "foo":
            return t.DataError("I want only foo!")
        return 'foo'


    class ParamsValidator(TrafaretValidator):
        ids = t.List(t.Int)
        payload = t.Dict(foo=t.Call(foo_validator))

    validator = ParamsValidator(ids=ids, payload=payload)
    if not validator.validate():
        return validator.errors
