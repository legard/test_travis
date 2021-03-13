# content of test_sample.py
import pytest

def inc(x):
    return x + 1

@pytest.mark.parametrize("expected_result", [3, 4, 5])
def test_answer(expected_result):
    assert inc(3) == expected_result
