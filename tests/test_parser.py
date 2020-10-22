import pytest

from models.password_checker import PasswordChecker


@pytest.mark.parametrize(
    'first, second',
    [
        (None, 'asdczxvzxczx'),
        ('asdczxvzxczx', None),
    ]
)
def test_password_checker_with_one_pwd_is_none(first, second):
    with pytest.raises(ValueError) as e:
        PasswordChecker(password=first, password_confirm=second)
    assert e.match('Null password')


def test_password_checker_with_short_password():
    first, second = 'aaaaa', 'aaaaa'
    with pytest.raises(ValueError) as e:
        PasswordChecker(password=first, password_confirm=second)
    assert e.match('Very short password')


def test_password_checker_with_different_pwds():
    first, second = 'aaaazzza', 'vvaaaaaasd'
    with pytest.raises(ValueError) as e:
        print(first, second)
        PasswordChecker(password=first, password_confirm=second)
    assert e.match('passwords do not match')


def test_password_checker_without_capital_letters():
    first, second = 'aaaa123!!!', 'aaaa123!!!'
    with pytest.raises(ValueError) as e:
        print(first, second)
        PasswordChecker(password=first, password_confirm=second)
    assert e.match('Not ok password')


def test_password_checker_without_digits():
    first, second = 'aaaaAAA!!!', 'aaaaAAA!!!'
    with pytest.raises(ValueError) as e:
        PasswordChecker(password=first, password_confirm=second)
    assert e.match('Not ok password')


def test_password_checker_without_special_symbols():
    first, second = 'aaaaAAA123', 'aaaaAAA123'
    with pytest.raises(ValueError) as e:
        PasswordChecker(password=first, password_confirm=second)
    assert e.match('Not ok password')


@pytest.mark.parametrize(
    'first,second,mark',
    [
        ('aaaaAAA123!', 'aaaaAAA123!', 'ok'),
        ('aaaaAAA123!11@#$%^', 'aaaaAAA123!11@#$%^', 'good'),
        ('aaaaAAA123!11@#$%^zxcasdasdasdaczxf', 'aaaaAAA123!11@#$%^zxcasdasdasdaczxf', 'very good'),
    ]
)
def test_password_checker_with_password_len_lt_15(first, second, mark):
    result = PasswordChecker(password=first, password_confirm=second)
    assert result.password_strength == mark
