from collections import defaultdict
from ctypes import Union
import pytest


@pytest.fixture(scope="session")
def XErrorData():
    default_values = ("🤪-aa-🤪", "", 1.1, -1.2, [1, 2], {"a": 1}, True, None, 1, 0)
    params_type = defaultdict(lambda: 0, {int: "Integer", str: "String"})

    def __jsonerr__(value, code, msg, attr):
        return dict(value=value, code=code, message_keys=[msg], attributes=attr)

    def _errorhandler(code, param, type_param, /, *, values=None, attr=None):
        values = values or default_values
        msg = params_type[type_param] or type_param
        key_type = list(params_type.keys())[
            list(params_type.values()).index(params_type[type_param])
        ]

        error_data = [
            __jsonerr__(value, code, msg, attr or {param: value})
            for value in values
            if type(value) != key_type
        ]
        return {param: error_data}

    def _validationfailed(param, type_param, /):
        return _errorhandler("validationFailed", param, type_param)

    def _badrequest(param, type_param, /):
        return _errorhandler("badRequest", param, type_param)

    class ContainerErrorData:
        validation_failed = _validationfailed
        bad_request = _badrequest
        error_data = _errorhandler

    return ContainerErrorData
