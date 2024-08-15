import pytest
from src import string as st 


def test_title():
    assert st.title('ahmed mohamed ali') == "Ahmed Mohamed Ali"


def test_concatenate():
    assert st.title(st.concatenate('ahmed mohamed', ' ali')) == "Ahmed Mohamed Ali"


def test_to_lower():
    assert st.tolower('HELLO') == 'hello'


def test_to_upper():
    assert st.toUpper('hello') == 'HELLO'

day = 28 
#@pytest.mark.skip(reason= "Not ready yet, featuer is not implmented")
@pytest.mark.skipif(not (day >= 28 and day<=30), reason='day must be in between 28 and 30')
def test_payment(): 
    assert 1 > 0 





