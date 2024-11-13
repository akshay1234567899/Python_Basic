import pytest

class TestClass:

    @pytest.mark.parametrize("num1,num2",[(2,2),(8,5),(5,5)])
    def test_calculate(self,num1,num2):
        assert num1==num2
    