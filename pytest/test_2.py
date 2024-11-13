import pytest
class TestClass:
    # @pytest.fixture() # decorator -- anotation in testNG
    def setup(self):
        print("launching browser")
        yield
        # print("open URL")
        print("close browser")

    def test_login(self):
        print("this is login method:")


    @pytest.mark.skip(reason="skip this test method")
    def test_search(self):
        print("this is your search method:")


    def test_addtocart(self,setup):
        print("added item list under cart:")

        # pytest: it is a framework, used to handle multiple class method in one place.
