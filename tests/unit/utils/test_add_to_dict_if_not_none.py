"""Test the add_to_dict_if_not_none function."""
import pytest
from geneweaver.core.utils import add_to_dict_if_not_none


@pytest.mark.parametrize(
    "value",
    [
        1,
        1.0,
        "string",
        [1, 2, 3],
        {"key": "value"},
        (1, 2, 3),
        True,
        False,
        # Using None as the value should do nothing
        None,
    ],
)
@pytest.mark.parametrize(
    ("d", "expected"),
    [
        # Keys that won't be overwritten
        ({}, {}),
        ({"existing_key": "existing_value"}, {"existing_key": "existing_value"}),
        ({("other_tuple",): "existing_value"}, {("other_tuple",): "existing_value"}),
        ({2: "existing_value"}, {2: "existing_value"}),
        ({2.0: "existing_value"}, {2.0: "existing_value"}),
        ({frozenset("a"): "existing_value"}, {frozenset("a"): "existing_value"}),
        # Existing keys should be overwritten
        ({"key": "existing_value"}, {"key": "existing_value"}),
        ({("tuple",): "existing_value"}, {("tuple",): "existing_value"}),
        ({None: "existing_value"}, {None: "existing_value"}),
        ({True: "existing_value"}, {True: "existing_value"}),
        ({False: "existing_value"}, {False: "existing_value"}),
        ({1: "existing_value"}, {1: "existing_value"}),
        ({1.0: "existing_value"}, {1.0: "existing_value"}),
        ({frozenset(): "existing_value"}, {frozenset(): "existing_value"}),
    ],
)
@pytest.mark.parametrize(
    "key",
    [
        "key",
        ("tuple",),
        None,
        True,
        False,
        1,
        1.0,
        frozenset(),
    ],
)
def test_add_to_dict_if_not_none(d, key, value, expected):
    """The function should add the key-value pair to the dict if value is not None."""
    if value is not None:
        expected[key] = value
    add_to_dict_if_not_none(d, key, value)
    assert d == expected


INVALID_DICT_KEY_PAIRS = [
    # Invalid dicts, valid keys
    (None, "key"),
    (None, ("tuple",)),
    (None, None),
    (None, True),
    (None, False),
    (None, 1),
    (None, 1.0),
    (None, frozenset()),
    # Valid dicts, invalid keys
    ({}, set()),
    ({}, []),
    ({}, {}),
    ({}, bytearray(b"Hello")),
]


# Each of these values should be assignable to the dict as a value.
@pytest.mark.parametrize(
    "value",
    [
        1,
        1.0,
        "string",
        [1, 2, 3],
        {"key": "value"},
        (1, 2, 3),
        True,
        False,
    ],
)
@pytest.mark.parametrize(("d", "key"), INVALID_DICT_KEY_PAIRS)
def test_add_to_dict_if_not_none_errors(d, key, value):
    """Test that the function raises a TypeError if the dict or key is invalid."""
    with pytest.raises(TypeError):
        add_to_dict_if_not_none(d, key, value)


@pytest.mark.parametrize(("d", "key"), INVALID_DICT_KEY_PAIRS)
def test_add_to_dict_if_not_none_no_error_on_none(d, key):
    """Test that the function does nothing if the value is None.

    This should be the case even in the error conditions we tested in the previous
    test.
    """
    start_d = None
    if d is not None:
        start_d = d.copy()

    add_to_dict_if_not_none(d, key, None)

    if start_d is not None:
        assert d == start_d
