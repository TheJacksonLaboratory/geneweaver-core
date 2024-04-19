"""Test the api_response schemas."""

from typing import List

import pytest
from geneweaver.core.schema.api_response import CollectionResponse, Paging, PagingLinks
from geneweaver.core.schema.gene import Gene, GeneValue
from geneweaver.core.schema.geneset import BatchUpload, Geneset, GenesetTier
from geneweaver.core.schema.publication import Publication, PublicationInfo


def test_paging_links():
    """Test the PagingLinks schema."""
    links = PagingLinks(
        first="http://example.com/first",
        previous="http://example.com/previous",
        next="http://example.com/next",
        last="http://example.com/last",
    )
    assert links.first == "http://example.com/first"
    assert links.previous == "http://example.com/previous"
    assert links.next == "http://example.com/next"
    assert links.last == "http://example.com/last"


@pytest.mark.parametrize(
    "paging_links_kwargs",
    [
        {"first": "not a link", "previous": "http://example.com/previous"},
        {"first": "http://alink.com", "previous": "not a link"},
        {
            "first": "http://alink.com",
            "previous": "http://example.com/previous",
            "next": "not a link",
        },
        {
            "first": "http://alink.com",
            "previous": "http://alink.com",
            "next": "http://example.com/next",
            "last": "not a link",
        },
    ],
)
def test_paging_links_error(paging_links_kwargs):
    """Test the PagingLinks schema in error cases."""
    with pytest.raises(ValueError, match="not an allowed value"):
        PagingLinks(**paging_links_kwargs)


def test_paging():
    """Test the Paging schema in non-error cases."""
    paging = Paging(
        page=1,
        items=10,
        total_pages=5,
        total_items=50,
        links=PagingLinks(
            first="http://example.com/first",
            previous="http://example.com/previous",
            next="http://example.com/next",
            last="http://example.com/last",
        ),
    )
    assert paging.page == 1
    assert paging.items == 10
    assert paging.total_pages == 5
    assert paging.total_items == 50
    assert paging.links.first == "http://example.com/first"
    assert paging.links.previous == "http://example.com/previous"
    assert paging.links.next == "http://example.com/next"
    assert paging.links.last == "http://example.com/last"


@pytest.mark.parametrize(
    "paging_kwargs",
    [
        {"page": "not a number", "items": 10},
        {"page": 1, "items": "not a number"},
        {"page": 1, "items": 10, "total_pages": "not a number"},
        {"page": 1, "items": 10, "total_pages": 5, "total_items": "not a number"},
        {
            "page": 1,
            "items": 10,
            "total_pages": 5,
            "total_items": 50,
            "links": "not a link",
        },
    ],
)
def test_paging_errors(paging_kwargs):
    """Test the Paging schema in error cases."""
    with pytest.raises(ValueError, match="not an allowed value"):
        Paging(**paging_kwargs)


def test_collection_response():
    """Test the CollectionResponse schema in non-error cases."""
    collection_response = CollectionResponse(
        data=[1, 2, 3],
        paging=Paging(
            page=1,
            items=10,
            total_pages=5,
            total_items=50,
            links=PagingLinks(
                first="http://example.com/first",
                previous="http://example.com/previous",
                next="http://example.com/next",
                last="http://example.com/last",
            ),
        ),
    )

    assert collection_response.data == [1, 2, 3]
    assert collection_response.paging.page == 1
    assert collection_response.paging.items == 10
    assert collection_response.paging.total_pages == 5
    assert collection_response.paging.total_items == 50
    assert collection_response.paging.links.first == "http://example.com/first"
    assert collection_response.paging.links.previous == "http://example.com/previous"
    assert collection_response.paging.links.next == "http://example.com/next"
    assert collection_response.paging.links.last == "http://example.com/last"


@pytest.mark.parametrize(
    "data_class",
    [GeneValue, Gene, BatchUpload, Geneset, GenesetTier, Publication, PublicationInfo],
)
def test_inherit_from_collection_response(data_class):
    """Test that we can inherit from the CollectionResponse class."""

    class CollectionResponseSubclass(CollectionResponse):
        data: List[data_class]

    collection_response = CollectionResponseSubclass(
        data=[],
        paging=None,
    )

    assert collection_response is not None


def test_collection_response_error():
    """Test the CollectionResponse class in error cases."""
    with pytest.raises(ValueError, match="not an allowed value"):
        CollectionResponse(data="not a list")
