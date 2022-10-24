import sys
sys.path.append('/Users/narek/zipf/bin')
import optimize


actual_result = optimize.f(10, 20)
print(actual_result)
expected_result = 230400 


def test_f():
    assert abs(actual_result - expected_result) < 1.1

def test_g():
    assert expected_result == actual_result 





