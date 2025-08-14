import math
import triangle_fcn as fcn



def test_fc():
    assert fcn.hypot(9, 12) == 15
    assert fcn.hypot(2.1, 2.8) == 3.5
    assert fcn.hypot(1.5, 2.0) == 2.5
    #assert fcn.hypot(complex(1,2), complex(2,3))
    assert fcn.hypot(1,1) == math.sqrt(2)
    #assert hypot(1,1)*hypot(1,1) == 2
    math.isclose(fcn.hypot(1, 1) * fcn.hypot(1, 1), 2, rel_tol=1e-9)
    print("Test passed!")

def test_fc1():
    assert fcn.hypot(-3, 4) == fcn.hypot(3, 4)
    print("No negative, should not be passed")
