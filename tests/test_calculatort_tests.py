import pytest
from src import calculator



@pytest.mark.FEB_RELEASE
def test_add():
    # Arrange , Actions, Assertions 
    assert calculator.add(2,8) == 10 
    assert calculator.add(-2,-8) == -10
    assert calculator.add(-2,9) == 7
    assert calculator.add(0,-8) == -8



@pytest.mark.parametrize('a,b,exp_res',[(2,8,-6), (-2,-8,6), (-2,9,-11), (24,9,15)])
def test_sub(a, b , exp_res):
    assert calculator.sub(a , b) == exp_res


   

test_data = [(2,8,16),(-2,-8,16),(-2,9,-18),(0,-8,0), (3,5,15)]  

@pytest.mark.parametrize("input1, input2, expected_result",test_data)
def test_mul(input1, input2, expected_result):
    assert calculator.mul(input1, input2) == expected_result
   

@pytest.mark.FEB_RELEASE
def test_div():
    # Arrange , Actions, Assertions 
    assert calculator.div(2,8) == 0.25 
    assert calculator.div(-2,-1) == 0.25 #2
    assert calculator.div(18,9) == 2 
    assert calculator.div(0,-8) == 0

    with pytest.raises(ZeroDivisionError):
        calculator.div(2,0)


@pytest.mark.FEB_RELEASE    
def test_square_root():
    # Arrange , Actions, Assertions 
    assert calculator.square_root(169) == 13 
    assert calculator.square_root(64) == 8
    assert calculator.square_root(400) == 20 
    assert calculator.square_root(-81) == None
