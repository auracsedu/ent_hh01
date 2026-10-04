import pytest


@pytest.mark.parametrize(
    "stdin, expected",
    [
        ('23\n59\n50\n20\n', ['00:00:10', '+1일']),
        ('0\n0\n0\n0\n', ['00:00:00', '+0일']),
        ('12\n30\n0\n86400\n', ['12:30:00', '+1일']),
        ('1\n2\n3\n3661\n', ['02:03:04', '+0일']),
        ('0\n0\n0\n86399\n', ['23:59:59', '+0일']),
        ('23\n59\n59\n1\n', ['00:00:00', '+1일']),
        ('10\n0\n0\n300000\n', ['21:20:00', '+3일']),
        ('5\n5\n5\n0\n', ['05:05:05', '+0일']),
    ],
)
def test_add_seconds(run, stdin, expected):
    assert run("problem_01", stdin) == expected
