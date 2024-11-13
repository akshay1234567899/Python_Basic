import pytest
from pytest_dependency import depends


# setup -- passed/failed
# login --skipped/failed
# search --- skipped
# advance ----search
# logout

# @pytest.mark.dependent

class Test:
    @pytest.mark.dependency()
    def test_openApp(self):
        assert True

    @pytest.mark.dependency(depends=['Test::test_openApp'])
    def test_login(self):
        assert True

    @pytest.mark.dependency(depends=['Test::test_login'])
    def test_search(self):
        assert False

    @pytest.mark.dependency(depends=['Test::test_login','Test::test_search'])
    def test_AdvancedSearch(self):
        assert True

    def test_logout(self):
        assert True
