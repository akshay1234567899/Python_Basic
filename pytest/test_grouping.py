import pytest

class TestGrouping:
    @pytest.mark.sanity
    def test_method_m1(self):
        print("method m1  passed")

    @pytest.mark.regression
    def test_method_m2(self):
        print("method m1  passed")

    @pytest.mark.regression
    def test_method_m3(self):
        print("method m1  passed")

    @pytest.mark.sanity
    def test_method_m4(self):
        print("method m1  passed")

    @pytest.mark.smoke
    def test_method_m5(self):
        print("method m1  passed")

    @pytest.mark.regression
    def test_method_m6(self):
        print("method m1  passed")

    @pytest.mark.sanity
    def test_method_m7(self):
        print("method m1  passed")
# pytest -v -s -m "regression" /Users/akshaydhiman/PycharmProjects_SDET_08_01/pythonProject/pytest


