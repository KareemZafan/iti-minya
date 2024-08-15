from src.stack import Stack
import pytest

class TestStack:
    def test_push(self):
        stc= Stack()
        stc.push(1)
        stc.push(2)
        stc.push(44)

        assert stc.peek() == 44
        assert stc.size() == 3
        assert stc.current_stack() == [1,2,44]
    
    def test_pop(self):
        stc= Stack()
        stc.push(1)
        stc.push(2)
        stc.push(44)
        stc.push(50)
        stc.push(60)
        

        assert stc.peek() == 60
        assert stc.size() == 5
        assert stc.current_stack() == [1,2,44,50,60]
        assert stc.pop() == 60 
        assert stc.peek() == 50 
        assert stc.size() == 4 
        assert stc.current_stack() ==  [1,2,44,50] 
        