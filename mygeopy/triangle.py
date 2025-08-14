# This is the full function with function and tests

import math
import cmath

def hypot(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def test_fc():
    assert hypot(9, 12) == 15
    assert hypot(2.1, 2.8) == 3.5
    assert hypot(1.5, 2.0) == 2.5
    #assert hypot(complex(1,2), complex(2,3))
    assert hypot(1,1) == math.sqrt(2)
    #assert hypot(1,1)*hypot(1,1) == 2
    math.isclose(hypot(1, 1) * hypot(1, 1), 2, rel_tol=1e-9)
    print("Test passed!")

#test_fc()

def test_fc1():
    assert hypot(-3, 4) == hypot(3, 4)
    print("No negative, should not be passed")


#test_fc1()
