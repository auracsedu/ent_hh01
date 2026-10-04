import pytest


@pytest.mark.parametrize(
    "stdin, expected",
    [
        ('1\n', ['1', '1']),
        ('9\n', ['9', '9']),
        ('10\n', ['9', '9']),
        ('12\n', ['9', '9']),
        ('20\n', ['19', '10']),
        ('50\n', ['49', '13']),
        ('99\n', ['99', '18']),
        ('100\n', ['99', '18']),
        ('1000\n', ['999', '27']),
        ('4321\n', ['3999', '30']),
    ],
)
def test_max_digit_sum(run, stdin, expected):
    assert run("problem_03", stdin) == expected
