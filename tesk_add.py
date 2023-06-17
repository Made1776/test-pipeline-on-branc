import pytest 

def test_addition_returns_results_when_have_two_numbers():
    first_number = 10
    second_number = 20
    expected_result = 30


    result = addition(first_number, second_number)

    assert expected_result == result 