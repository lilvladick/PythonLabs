import pytest
from lab4_solution import modules, generate_password, generate_passwords, multiply_arrays_pairs


@pytest.mark.parametrize("list1, list2, expected", [
    ([1, 2, 3], [4, 5, 6], [4, 10, 18]),
    ([7, 8, 9], [10, 11, 12], [70, 88, 108]),
    ([1, 1, 1], [2, 2, 2], [2, 2, 2]),
    ([], [], []),
    ([1, 2], [3, 4, 5], [3, 8]),
])
def test_multiply_arrays_pairs(list1, list2, expected):
    generator = multiply_arrays_pairs(list1, list2)
    result = list(generator)
    assert result == expected

@pytest.mark.parametrize("length, expected_length", [
    (12, 12),
    (10, 10),
    (5, 5),
])
def test_generate_password_length(length, expected_length):
    password = generate_password(length)
    assert len(password) == expected_length

def test_generate_password_invalid_length():
    with pytest.raises(ValueError):
        generate_password(0)

def test_generate_password_negative_length():
    with pytest.raises(ValueError):
        generate_password(-1)

@pytest.mark.parametrize("password_length, passwords_count, expected_count", [
    (12, 5, 5),
    (10, 3, 3),
    (5, 2, 2),
])
def test_generate_passwords_count(password_length, passwords_count, expected_count):
    passwords = generate_passwords(password_length, passwords_count)
    assert len(passwords) == expected_count

def test_generate_passwords_invalid_count():
    with pytest.raises(ValueError):
        generate_passwords(password_length=12, passwords_count=0)

def test_generate_passwords_negative_count():
    with pytest.raises(ValueError):
        generate_passwords(password_length=12, passwords_count=-1)

@pytest.mark.parametrize("a, b, expected", [
    (2, 6, [2, 3, 4, 5, 6]),
    (0, 5, [0, 1, 2, 3, 4, 5]),
    (-3, 2, [3, 2, 1, 0, 1, 2]),
])
def test_modules(a, b, expected):
    result = modules(a, b)
    assert result == expected

def test_modules_invalid_range():
    with pytest.raises(ValueError):
        modules(6, 2)