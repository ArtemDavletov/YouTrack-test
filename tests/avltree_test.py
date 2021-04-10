import pytest

from AVLTree import AVLTree


@pytest.mark.parametrize(
    ["values_for_inserting", "balanced_tree_in_list"],
    [
        ([], []),
        ([3], [3]),
        ([3, 6], [3, 6]),
        ([3, 6, 1], [3, 1, 6]),
        ([3, 6, 1, 5], [3, 1, 6, 5]),
        ([3, 6, 1, 5, 4], [3, 1, 5, 4, 6]),
        ([3, 6, 1, 5, 4, 7], [5, 3, 6, 1, 4, 7]),
        ([3, 6, 1, 5, 4, 7, 8], [5, 3, 7, 1, 4, 6, 8]),
    ]
)
def test_tree_insertion(values_for_inserting, balanced_tree_in_list):
    avl_tree = AVLTree()

    for value in values_for_inserting:
        avl_tree.insert(value)

    assert avl_tree.to_list() == balanced_tree_in_list


@pytest.mark.parametrize(
    ["values_for_inserting", "error"],
    [
        ([3, 3], ValueError),
        ([3, dict()], TypeError),
    ]
)
def test_tree_incorrect_input(values_for_inserting, error):
    avl_tree = AVLTree()

    with pytest.raises(error):
        for value in values_for_inserting:
            avl_tree.insert(value)
