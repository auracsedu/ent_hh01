import pytest


@pytest.mark.parametrize(
    "stdin, expected",
    [
        ('1\n', ['0', '1']),
        ('2\n', ['1', '2']),
        ('3\n', ['7', '16']),
        ('6\n', ['8', '16']),
        ('7\n', ['16', '52']),
        ('27\n', ['111', '9232']),
        ('97\n', ['118', '9232']),
    ],
)
def test_collatz(run, stdin, expected):
    assert run("problem_02", stdin) == expected
