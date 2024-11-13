import pytest

class Testordering:
    # @pytest.mark.first


    @pytest.mark.run(order=2)
    def test_methodC_(self):
        print("this is ordering method")

    @pytest.mark.run(order=1)
    def test_methodA_(self):
        print("this is ordering method")

    @pytest.mark.run(order=4)
    def test_methodD_(self):
        print("this is ordering method")

    @pytest.mark.run(order=3)
    def test_methodB_(self):
        print("this is ordering method")