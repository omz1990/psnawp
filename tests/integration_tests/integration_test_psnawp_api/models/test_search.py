import inspect

import pytest
from psnawp_api import PSNAWP
from psnawp_api.models import SearchDomain

from tests.integration_tests.integration_test_psnawp_api import my_vcr


@pytest.mark.vcr()
def test_search__universal_search(psnawp_fixture: PSNAWP) -> None:
    with my_vcr.use_cassette(f"{inspect.currentframe().f_code.co_name}.yaml"):
        search = psnawp_fixture.search(search_query="GTA", search_domain=SearchDomain.FULL_GAMES, limit=1)
        actual_count = 0
        for _ in search:
            actual_count += 1
        assert actual_count == 1


@pytest.mark.vcr()
def test_search__get_game_content_id(psnawp_fixture: PSNAWP) -> None:
    with my_vcr.use_cassette(f"{inspect.currentframe().f_code.co_name}.yaml"):
        search = psnawp_fixture.search(search_query="GTA", search_domain=SearchDomain.FULL_GAMES, limit=1)
        for result in search:
            assert result["result"]["invariantName"] == "Grand Theft Auto V (PlayStation®5)"
            assert result["result"]["defaultProduct"]["id"] == "UP1004-PPSA03420_00-GTAOSTANDALONE01"
            break
