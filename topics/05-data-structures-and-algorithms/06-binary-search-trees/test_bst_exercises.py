import pytest
from bst_exercises import (
    TreeNode,
    contains,
    height,
    in_order,
    insert,
    is_valid_bst,
    min_value,
    remove,
)

ALL_VALUES = [1, 3, 4, 6, 7, 8, 10, 13, 14]


def example_tree():
    """Build this tree by hand:

            8
          /   \\
         3     10
        / \\      \\
       1   6      14
          / \\    /
         4   7  13
    """
    six = TreeNode(6, TreeNode(4), TreeNode(7))
    three = TreeNode(3, TreeNode(1), six)
    ten = TreeNode(10, None, TreeNode(14, TreeNode(13)))
    return TreeNode(8, three, ten)


def read(root):
    """Read a tree's values in sorted order, without using the exercises."""
    if root is None:
        return []
    return [*read(root.left), root.value, *read(root.right)]


def obeys_the_rule(root, low=float("-inf"), high=float("inf")):
    if root is None:
        return True
    return (
        low < root.value < high
        and obeys_the_rule(root.left, low, root.value)
        and obeys_the_rule(root.right, root.value, high)
    )


class TestContains:
    def test_every_value_is_found(self):
        tree = example_tree()
        assert all(contains(tree, value) for value in ALL_VALUES)

    def test_absent_values(self):
        tree = example_tree()
        assert not any(contains(tree, value) for value in [0, 2, 5, 9, 99])

    def test_empty_tree(self):
        assert contains(None, 5) is False


class TestMinValue:
    def test_example_tree(self):
        assert min_value(example_tree()) == 1

    def test_root_is_the_smallest(self):
        assert min_value(TreeNode(5, None, TreeNode(9))) == 5

    def test_empty_tree(self):
        with pytest.raises(ValueError):
            min_value(None)


class TestInsert:
    def test_into_an_empty_tree(self):
        root = insert(None, 8)
        assert (root.value, root.left, root.right) == (8, None, None)

    def test_smaller_goes_left_and_larger_goes_right(self):
        root = insert(None, 8)
        insert(root, 3)
        insert(root, 10)
        assert root.left.value == 3
        assert root.right.value == 10

    def test_returns_the_same_root(self):
        root = TreeNode(8)
        assert insert(root, 3) is root

    def test_goes_several_levels_down(self):
        root = None
        for value in [8, 3, 10, 1, 6]:
            root = insert(root, value)
        assert root.left.left.value == 1
        assert root.left.right.value == 6

    def test_duplicates_are_ignored(self):
        root = example_tree()
        insert(root, 6)
        assert read(root) == ALL_VALUES

    def test_tree_stays_valid(self):
        root = None
        for value in [50, 30, 70, 20, 40, 60, 80, 35, 45]:
            root = insert(root, value)
        assert obeys_the_rule(root)
        assert read(root) == [20, 30, 35, 40, 45, 50, 60, 70, 80]


class TestInOrder:
    def test_example_tree(self):
        assert in_order(example_tree()) == ALL_VALUES

    def test_single_node(self):
        assert in_order(TreeNode(5)) == [5]

    def test_empty_tree(self):
        assert in_order(None) == []


class TestHeight:
    def test_example_tree(self):
        assert height(example_tree()) == 4

    def test_single_node(self):
        assert height(TreeNode(5)) == 1

    def test_empty_tree(self):
        assert height(None) == 0

    def test_lopsided_tree(self):
        chain = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
        assert height(chain) == 4


class TestIsValidBst:
    def test_example_tree(self):
        assert is_valid_bst(example_tree()) is True

    def test_empty_and_single(self):
        assert is_valid_bst(None) is True
        assert is_valid_bst(TreeNode(5)) is True

    def test_child_on_the_wrong_side(self):
        assert is_valid_bst(TreeNode(8, TreeNode(9), TreeNode(10))) is False

    def test_deep_value_that_breaks_the_rule_for_an_ancestor(self):
        # 9 is a correct right child of 3, but it sits in the left subtree of 8.
        tree = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(9)), TreeNode(10))
        assert is_valid_bst(tree) is False

    def test_deep_value_on_the_right(self):
        # 7 is a correct left child of 14, but it sits in the right subtree of 8.
        tree = TreeNode(8, TreeNode(3), TreeNode(10, None, TreeNode(14, TreeNode(7))))
        assert is_valid_bst(tree) is False

    def test_repeated_value(self):
        assert is_valid_bst(TreeNode(8, TreeNode(8))) is False


class TestRemove:
    def check(self, root, expected):
        assert read(root) == expected
        assert obeys_the_rule(root)

    def test_a_leaf(self):
        root = remove(example_tree(), 4)
        self.check(root, [1, 3, 6, 7, 8, 10, 13, 14])

    def test_a_node_with_one_child(self):
        root = remove(example_tree(), 10)
        self.check(root, [1, 3, 4, 6, 7, 8, 13, 14])

    def test_a_node_with_two_children(self):
        root = remove(example_tree(), 3)
        self.check(root, [1, 4, 6, 7, 8, 10, 13, 14])

    def test_the_root(self):
        root = remove(example_tree(), 8)
        self.check(root, [1, 3, 4, 6, 7, 10, 13, 14])

    def test_value_not_in_the_tree(self):
        root = remove(example_tree(), 99)
        self.check(root, ALL_VALUES)

    def test_the_only_node(self):
        assert remove(TreeNode(5), 5) is None

    def test_empty_tree(self):
        assert remove(None, 5) is None

    def test_removing_everything_one_by_one(self):
        root = example_tree()
        remaining = list(ALL_VALUES)
        for value in [8, 1, 14, 6, 3, 10, 13, 4, 7]:
            root = remove(root, value)
            remaining.remove(value)
            self.check(root, remaining)
        assert root is None
