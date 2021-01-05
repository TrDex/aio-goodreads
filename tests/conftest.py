import asyncio

import pytest


@pytest.fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for the entire test session"""
    loop = asyncio.get_event_loop()
    return loop
