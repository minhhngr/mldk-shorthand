import pytest
import logging
import sys

sys.dont_write_bytecode = True  # Ignore __pycache__ folder

"""pytest_collection_modifyitems

Here is the order of execution:

Plugin1's pytest_collection_modifyitems is called because it is marked with tryfirst=True.
Plugin2's pytest_collection_modifyitems is called because it is marked with trylast=True (but even without this mark it would come after Plugin1).

Plugin3's
 - pytest_collection_modifyitems called until the yield point because it is a hook wrapper.
 - pytest_collection_modifyitems then executing the code after the yield point. 
The yield receives a Result instance which encapsulates the result from calling the non-wrappers. Wrappers shall not modify the result.

It's possible to use tryfirst and trylast also in conjunction with hookwrapper=True in which case it will influence the ordering of hookwrappers among each other.
"""

# Plugin 1
# @pytest.hookimpl(tryfirst=True)
# def pytest_collection_modifyitems(items):
#     # will execute as early as possible
#     print("pytest_collection_modifyitems: hookimpl(tryfirst=True)")

# Plugin 2
# @pytest.hookimpl(trylast=True)
# def pytest_collection_modifyitems(items):
#     # will execute as late as possible
#     print("pytest_collection_modifyitems: hookimpl(trylast=True)")

# Plugin 3
# @pytest.hookimpl(hookwrapper=True)
# def pytest_collection_modifyitems(items):
#     # will execute even before the tryfirst one above!
#     print("[BEFORE] pytest_collection_modifyitems: pytest.hookimpl(hookwrapper=True)")
#     outcome = yield
#     # will execute after all non-hookwrappers executed
#     print("[AFTER] pytest_collection_modifyitems: pytest.hookimpl(hookwrapper=True)")
