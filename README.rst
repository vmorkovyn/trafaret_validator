====================
TrafaretValidator
====================


:Status: Beta

This is a wrapper that validate request using trafaret_.

Usage:

.. code-block:: python

    class RequestValidator(TrafaretValidator):
        ids = t.List(t.Int)
        payload = t.Dict(x=t.String)

    validator = RequestValidator(ids=ids, payload=payload)
    if not validator.validate():
        return validator.errors