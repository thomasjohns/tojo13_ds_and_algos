import pytest


@pytest.mark.parametrize('test_input,expected',[
    ([1, 2, 9], [1, 2, 9]),
    ([1, 9, 2], [1, 2, 9]),
    ([4, 4, 4], [4, 4, 4]),
    ([1], [1]),
    ([9, -9], [-9, 9]),
    ([0, 9, 6, 3, 5], [0, 3, 5, 6, 9]),
    ([], []),
    ([8, 7, 3, 4, 2], [2, 3, 4, 7, 8]),
])
def test_bubble_sort(test_input, expected):
    assert eval(test_input) == expected

