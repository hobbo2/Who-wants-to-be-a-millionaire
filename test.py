import pytest
from project import option_check, time, profile
from unittest.mock import patch # Help from stack overflow here


def test_time():
    # Since time() returns a tuple we can assign a var to each member of the returned tuple
    # This will allow us to assert individually on those vars for the correct answers
    years, months = time(12)
    assert years == 1
    assert months == 0


# The mark parametrize will allow us to test multiple different inputs in one test function
# Got a lot of help on stack overflow for this part
@pytest.mark.parametrize("option", ["A", "B"])
def test_option_check(option):
    # Need to patch the input message for testing purposes
    # Then we can run the code with the return_value of 1 as the user input
    with patch("builtins.input", return_value=1):
        result = option_check(option)
        # This assertion allows us to assert on the correct message
        # given the option we passed in from the parametrize decorator
        assert result == ("It will take 77 years and 9 months investing 1 in the S&P500 to reach 1000 000" if option == "A" else "You will reach 1 000 000 in 1 years by investing 78892.66 in the S&P500 Monthly")


@pytest.mark.parametrize("letter", ["A", "a", "B", "b"])
def test_profile(letter):
    if letter in ["A", "a"]:
        result = profile(letter)
        assert result == "A"
    elif letter in ["B", "b"]:
        result = profile(letter)
        assert result == "B"
