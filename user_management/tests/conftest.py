import pytest
from pytest_django.plugin import _blocking_manager


@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    from django.test.utils import CaptureQueriesContext
    from django.db import connection

    _blocking_manager.unblock()

    with CaptureQueriesContext(connection) as context:
        yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    from django.test.utils import CaptureQueriesContext
    from django.db import connection

    with CaptureQueriesContext(connection) as context:
        yield

    print(context.captured_queries)
    print(item._nodeid, context.final_queries)
