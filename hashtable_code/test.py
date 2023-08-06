from karpRabin import KarpRabin
import pytest

@pytest.fixture(scope="module")
def t_list():
    return ["zzz", "xyz", "my beautiful string"]

@pytest.fixture(scope="module")
def s_list():
    return ["x", "zzz" , "beautiful"]

def test_matching(s_list, t_list):
    kr = KarpRabin()
    assert kr.search(s_list[0], t_list[0]) == -1
    assert kr.search(s_list[0], t_list[1]) == 0
    assert kr.search(s_list[1], t_list[0]) == 0
    assert kr.search(s_list[1], t_list[2]) == -1
    assert kr.search(s_list[2], t_list[2]) == 3
