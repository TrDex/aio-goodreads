import os

import pytest

from aio_goodreads.client import GoodreadsClient

client = GoodreadsClient(os.environ.get('GOODREADS_CLIENT_KEY'), os.environ.get('GOODREADS_CLIENT_SECRET'))

pytestmark = pytest.mark.asyncio


async def test_get_author():
    author_id = 15325  # random number

    author = await client.get_author(author_id)
    assert int(author.gid) == author_id


async def test_get_book():
    book_id = 148234  # random number

    book = await client.get_book(148234)
    assert int(book.gid) == book_id


async def test_search_books():
    books = await client.search_books('The root')
    assert books
