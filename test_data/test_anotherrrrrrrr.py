import sys
sys.path.append('/Users/narek/zipf/bin')
import optimize


actual_result = optimize.f(10, 20)
expected_result = 239400

def test_ffffffff():
    assert actual_result < expected_result

def test_gggggggg():
    assert expected_result == 239400





