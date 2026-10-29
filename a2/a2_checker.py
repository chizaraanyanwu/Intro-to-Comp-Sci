"""A simple checker for functions in bridge_functions.py."""

import sys
from typing import Any

PYTA_LOCATION = 'pyta'

# pytest is bundled with PyTA in PYTA_LOCATION.
sys.path.insert(0, PYTA_LOCATION)

import pytest  # noqa: E402

import checker  # noqa: E402
import bridge_functions as bf  # noqa: E402

FILENAME = 'bridge_functions.py'
PYTA_CONFIG = 'pyta/a2_pyta.txt'
TARGET_LEN = 79
SEP = '='

CONSTANTS = {
    'ID_INDEX': 0,
    'NAME_INDEX': 1,
    'HIGHWAY_INDEX': 2,
    'LAT_INDEX': 3,
    'LON_INDEX': 4,
    'YEAR_INDEX': 5,
    'LAST_MAJOR_INDEX': 6,
    'LAST_MINOR_INDEX': 7,
    'NUM_SPANS_INDEX': 8,
    'SPAN_DETAILS_INDEX': 9,
    'LENGTH_INDEX': 10,
    'LAST_INSPECTED_INDEX': 11,
    'BCIS_INDEX': 12,
    'FROM_SEP': '=',
    'TO_SEP': ';',
    'HIGH_PRIORITY_BCI': 60,
    'MEDIUM_PRIORITY_BCI': 70,
    'LOW_PRIORITY_BCI': 100,
    'HIGH_PRIORITY_RADIUS': 500,
    'MEDIUM_PRIORITY_RADIUS': 250,
    'LOW_PRIORITY_RADIUS': 100,
    'EARTH_RADIUS': 6371
}

# Sample data. (The checker functions copy their arguments, so functions
# that modify their arguments cannot change it.)
SAMPLE_BRIDGES = [
    [1, 'Highway 24 Underpass at Highway 403', '403', 43.167233,
     -80.275567, '1965', '2014', '2009', 4,
     [12.0, 19.0, 21.0, 12.0], 65.0, '04/13/2012',
     [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]],
    [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582,
     '1963', '2014', '2007', 4, [
         12.2, 18.0, 18.0, 12.2], 61.0,
     '04/13/2012', [71.5, 68.1, 69.0, 69.4, 69.4, 70.3,
                    73.3]],
    [3, 'STOKES RIVER BRIDGE', '6', 45.036739, -81.33579, '1958',
     '2013', '', 1, [16.0], 18.4, '08/28/2013',
     [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]]
]

SAMPLE_RAW_DATA = [
    ['1 -  32/', 'Highway 24 Underpass at Highway 403', '403',
     '43.167233', '-80.275567', '1965', '2014', '2009', '4',
     'Total=64  (1)=12;(2)=19;(3)=21;(4)=12;', '65', '04/13/2012',
     '72.3', '', '72.3', '', '69.5', '', '70', '', '70.3', '', '70.5',
     '', '70.7', '72.9', ''],
    ['1 -  43/', 'WEST STREET UNDERPASS', '403', '43.164531',
     '-80.251582', '1963', '2014', '2007', '4',
     'Total=60.4  (1)=12.2;(2)=18;(3)=18;(4)=12.2;', '61',
     '04/13/2012', '71.5', '', '71.5', '', '68.1', '', '69', '',
     '69.4', '', '69.4', '', '70.3', '73.3', ''],
    ['2 -   4/', 'STOKES RIVER BRIDGE', '6', '45.036739', '-81.33579',
     '1958', '2013', '', '1', 'Total=16  (1)=16;', '18.4',
     '08/28/2013', '85.1', '85.1', '', '67.8', '', '67.4', '', '69.2',
     '70', '70.5', '', '75.1', '', '90.1', '']]

# A simple checker (NOT a full tester!) for assignment functions: for
# functions returning simple types, the function's name, the arguments to
# call it with and the type it should return.
SIMPLE_CASES = [
    ('get_average_bci', [SAMPLE_BRIDGES, 1], float),
    ('get_total_length_on_hwy', [SAMPLE_BRIDGES, '403'], float),
    ('get_distance_between', [SAMPLE_BRIDGES[0], SAMPLE_BRIDGES[1]], float),
    ('get_closest_bridge', [SAMPLE_BRIDGES, 1], int),
    ('inspect_bridges', [SAMPLE_BRIDGES, [1], '09/15/2018', 71.9],
     type(None)),
    ('add_rehab', [SAMPLE_BRIDGES, 1, '2023', False], type(None)),
    ('format_data', [SAMPLE_RAW_DATA], type(None)),
]

# For functions returning a list[int], the function's name and the
# arguments to call it with.
LIST_OF_INT_CASES = [
    ('get_bridges_in_radius', [SAMPLE_BRIDGES, 43.10, -80.15, 50]),
    ('get_bridges_with_bci_below', [SAMPLE_BRIDGES, [1, 2], 72]),
    ('get_bridges_containing', [SAMPLE_BRIDGES, '403']),
]


@pytest.mark.parametrize('fname, args, ret_type', SIMPLE_CASES,
                         ids=[case[0] for case in SIMPLE_CASES])
def test_returns_type(fname: str, args: list, ret_type: type) -> None:
    """Check that function fname, called with args, returns a value of
    type ret_type."""

    result = checker.type_check_simple(getattr(bf, fname), args, ret_type)
    assert result[0], result[1]


@pytest.mark.parametrize('fname, args', LIST_OF_INT_CASES,
                         ids=[case[0] for case in LIST_OF_INT_CASES])
def test_returns_list_of_int(fname: str, args: list) -> None:
    """Check that function fname, called with args, returns a list[int]."""

    result = checker.returns_list_of(getattr(bf, fname), args, int)
    assert result[0], result[1]


def test_get_bridge() -> None:
    """Check that get_bridge returns a valid bridge record."""

    result = checker.type_check_full(bf.get_bridge, [SAMPLE_BRIDGES, 1],
                                     _is_bridge)
    assert result[0], result[1]


def test_assign_inspectors() -> None:
    """Check that assign_inspectors returns a list[list[int]]."""

    result = checker.type_check_full(
        bf.assign_inspectors, [SAMPLE_BRIDGES, [[43.10, -80.15]], 2],
        _is_list_of_list_of_int)
    assert result[0], result[1]


@pytest.mark.parametrize('name, expected', CONSTANTS.items())
def test_constants(name: str, expected: Any) -> None:
    """Check that the value of constant name has not been changed."""

    actual = getattr(bf, name)
    assert actual == expected, \
        f'The value of constant {name} should be {expected} but is {actual}.'


def _is_list_of_list_of_int(obj: Any) -> tuple[bool, str]:
    """Return (True, '') if obj is a list[list[int]], and (False, an error
    message) otherwise."""

    if (isinstance(obj, list)
            and all(isinstance(row, list)
                    and all(isinstance(item, int) for item in row)
                    for row in obj)):
        return (True, '')
    return (False, 'assign_inspectors should return a list[list[int]]')


def _is_bridge(obj: Any) -> tuple[bool, str]:
    """Return (True, '') if obj is a valid bridge record, and (False, an
    error message) otherwise."""

    msg = 'The return value should be a list'
    if not isinstance(obj, list):
        return (False, msg)
    if len(obj) != 13:
        return (False, msg + ' of length 13')

    correct_types = (int, str, str, float, float, str, str, str, int,
                     list, float, str, list)
    for (i, correct_type) in enumerate(correct_types):
        if not isinstance(obj[i], correct_type):
            msg += (f' and the value at index {i}'
                    f' should be a {correct_type.__name__}')
            return (False, msg)
    return (True, '')


if __name__ == '__main__':
    checker.ensure_no_io('bridge_functions')
    print(''.center(TARGET_LEN, SEP))
    print(' Start: checking coding style '.center(TARGET_LEN, SEP))
    checker.run_pyta(FILENAME, PYTA_CONFIG)
    print(' End checking coding style '.center(TARGET_LEN, SEP))

    print(' Start: checking type contracts '.center(TARGET_LEN, SEP))
    pytest.main(['-v', '-p', 'no:cacheprovider', __file__])
    print(' End checking type contracts '.center(TARGET_LEN, SEP))

    print('\nScroll up to see ALL RESULTS:')
    print('  - checking coding style')
    print('  - checking type contract\n')
