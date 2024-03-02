from project import title_name, get_name, return_times
import pytest

def test_itle_name():
    assert title_name("aaron xu") == "Aaron Xu"
    assert title_name("Harry") == "Harry"
    assert title_name("111") == "111"


def test_get_name():
    name_list = [1, 2, 3]
    assert get_name(3, name_list) == "Harry Potter"
    assert get_name(4, name_list) == ""


def test_return_times():
    assert return_times(1) == "1st "
    assert return_times(2) == "2nd "
    assert return_times(3) == "3rd "



