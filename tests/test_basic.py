import math
import pytest

def test_sqrt():  #test
   num = 25
   assert math.sqrt(num) == 5

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,33),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output