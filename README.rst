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

    class RequestValidator(TrafaretValidator):
        ids = t.List(t.Int)
        payload = t.Dict(x=t.String)

    validator = RequestValidator(ids=ids, payload=payload)
    if not validator.validate():
        return validator.errors