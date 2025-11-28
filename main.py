
from main import add
from main import multiply
from main import subtract
from main import divide

def test_add():
    result = add(4,2)
    assert result == 6
    print("success the add numbers")

def test_multiply():
    result = multiply(4,2)
    assert result == 8
    print("success the multiply numbers")

def test_subtract():
    result = subtract(4,2)
    assert result == 2
    print("succes the subtract numbers")

def test_divide():
    result = divide(4,2)
    assert result == 2
    print('success the divide numbers')
   

if __name__ == "__main__" :
    test_add()
    test_multiply()
    test_divide()
    test_subtract()
