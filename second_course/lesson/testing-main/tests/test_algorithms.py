from src.algorithms import find_closest_number, contains_duplicat, is_anagram
import pytest
from contextlib import nullcontext as does_not_raise


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3], 1),
        ([-1, -2, -3], -1),
        ([2, 3, -1, 1, -2, -3], 1),
        ([1, 2, 3, -1, -2, -3, 0], 0),
        ([1, 2, 3, -1, -2, -3, 0, 0], 0),
        ([1, 2, 3, -1, -2, -3, 0, 0, 0], 0),
        ([1, 2, 3, -1, -2, -3, 0, 0, 0, 0], 0),
        ([1, 2, 3, -1, -2, -3, 0, 0, 0, 0, 0], 0),
        ([-1000, -1000], -1000),
        ([42], 42),
        ([-7], -7),
        ([-5, 5], 5),
        ([1000, -1000], 1000),
        ([10, -10, 5, -2, 2, 1, 0], 0),
        ([0, 0, 5, -5, 2, -2], 0),
        ([3, 3, -3, -2, -2, 2, 2, 1, 1], 1),
        ([999999999, -1000000000, 500, -500], 500),
        ([100, 50, 25, -3, 3, 10, 20], 3),
    ],
)
def test_find_numbers_closest_to_zero(numbers, expected):
    assert find_closest_number(numbers) == expected


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3], False),
        ([-1, -2, -3], False),
        ([2, 3, -1, 1, -2, -3], False),
        ([1, 2, 3, -1, -2, -3, 0], False),
        ([1, 2, 3, -1, -2, -3, 0, 0], True),
        ([1, 2, 3, -1, -2, -3, 0, 0, 0], True),
        ([1, 2, 3, -1, -2, -3, 0, 0, 0, 0], True),
        ([1, 2, 3, -1, -2, -3, 0, 0, 0, 0, 0], True),
        ([-1000, -1000], True),
        ([42], False),
        ([-7], False),
        ([-5, 5], False),
        ([1000, -1000], False),
        ([10, -10, 5, -2, 2, 1, 0], False),
        ([0, 0, 5, -5, 2, -2], True),
        ([3, 3, -3, -2, -2, 2, 2, 1, 1], True),
        ([999999999, -1000000000, 500, -500], False),
        ([100, 50, 25, -3, 3, 10, 20], False),
    ],
)
def test_contains_duplicate_success(numbers, expected):
    assert contains_duplicat(numbers) == expected


@pytest.mark.parametrize(
    'numbers, expected',
    [
        ('[1, 2, 3]', TypeError),
        (5j, TypeError),
        (5.0, TypeError),
        (5, TypeError),
        ({1, 2, 3, 3, 5}, TypeError),
    ]
)
def test_contains_duplicate_failure(numbers, expected):
    pytest.raises(TypeError, contains_duplicat, numbers)


@pytest.mark.parametrize(
    's, t, expected, raises',
    [
        ('anagram', 'nagaram', True, does_not_raise()),
        ('rat', 'car', False, does_not_raise()),
        ('listen', 'silent', True, does_not_raise()),
        ('evil', 'vile', True, does_not_raise()),
        ('elvis', 'lives', True, does_not_raise()),
        ('elvis', 'lives!', False, does_not_raise()),
        ('elvis', 'lives', True, does_not_raise()),
        ({'a', 'n', 'a', 'g', 'r', 'a', 'm'}, 'nagaram', TypeError, pytest.raises(TypeError)),
        ('anagram', {'n', 'a', 'g', 'a', 'r', 'a', 'm'}, TypeError, pytest.raises(TypeError)),
        ('anagram', 5, TypeError, pytest.raises(TypeError)),
        (5, 'anagram', TypeError, pytest.raises(TypeError)),
        (5.0, 'anagram', TypeError, pytest.raises(TypeError)),
        ('anagram', 5.0, TypeError, pytest.raises(TypeError)),
        (5j, 'anagram', TypeError, pytest.raises(TypeError)),
        ('anagram', 5j, TypeError, pytest.raises(TypeError)),
    ]
)
def test_is_anagram(s, t, expected, raises):
    with raises:
        assert is_anagram(s, t) == expected
