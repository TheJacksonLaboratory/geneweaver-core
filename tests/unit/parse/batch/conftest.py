"""Fixtures for parsing tests."""
from geneweaver.core.parse.batch import HEADER_CHARACTERS, REQUIRED_HEADERS

HAS_REQUIRED_HEADER_FIELDS = [
    # All required keys are present
    {
        f"{HEADER_CHARACTERS[h_key]}": f"value{idx}"
        for idx, h_key in enumerate(REQUIRED_HEADERS)
    },
    # Extra keys are present, but all required keys are still there
    {
        header_name: f"value{idx}"
        for idx, header_name in enumerate(HEADER_CHARACTERS.values())
    },
    {
        header_name: f"value{idx}"
        for idx, header_name in enumerate(
            list(HEADER_CHARACTERS.values()) + ["extra_key"]
        )
    },
]

MISSING_REQUIRED_HEADER_FIELDS = (
    [
        # Incorrect header format
        {":key1": "value1"},
        {":key1": "value1", "=key2": "value2"},
        # Empty header
        {},
    ]
    + [
        # Missing one required key
        {
            f"{key}key{idx}": f"value{idx}"
            for idx, key in enumerate(HEADER_CHARACTERS.keys())
            if idx != missing_key_idx
        }
        for missing_key_idx in range(len(HEADER_CHARACTERS))
    ]
    + [
        # Missing all but one required key
        {
            f"{key}key{idx}": f"value{idx}"
            for idx, key in enumerate(HEADER_CHARACTERS.keys())
            if idx == keep_key_idx
        }
        for keep_key_idx in range(len(HEADER_CHARACTERS))
    ]
)
