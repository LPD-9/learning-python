"""Binary search trees: keeping data sorted so it can be searched quickly.

Implement each function so the tests in test_bst_exercises.py pass.
Run them with:
    pytest topics/05-data-structures-and-algorithms/06-binary-search-trees

In a binary tree each node has up to two children, left and right. A
binary search tree adds one rule: everything in a node's left subtree is
smaller than the node, and everything in its right subtree is larger.

            8
          /   \\
         3     10
        / \\      \\
       1   6      14

To find a value, start at the top and go left or right at each node, as
in binary search. Every step rules out a whole subtree.

A tree is represented by its top node, the root. An empty tree is None.
Most of these are shortest when written recursively: a tree is a node
plus two smaller trees.
"""


class TreeNode:
    """Given. One node of a tree."""

    def __init__(
        self,
        value: int,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


def contains(root: TreeNode | None, value: int) -> bool:
    """Return True if value is in the tree.

    Use the ordering rule to choose one direction at each node. Don't
    search both sides.

    >>> contains(TreeNode(8, TreeNode(3), TreeNode(10)), 3)
    True
    """
    raise NotImplementedError


def min_value(root: TreeNode | None) -> int:
    """Return the smallest value in the tree. Raise ValueError if it's empty.

    Where must the smallest value be, given the ordering rule?

    >>> min_value(TreeNode(8, TreeNode(3, TreeNode(1)), TreeNode(10)))
    1
    """
    raise NotImplementedError


def insert(root: TreeNode | None, value: int) -> TreeNode:
    """Add value to the tree in the right place, and return the root.

    Walk down as if searching for the value. Where the search falls off
    the tree is where the new node belongs. If the value is already in
    the tree, change nothing. Inserting into an empty tree returns the
    new node, which is now the root.

    >>> root = insert(None, 8)
    >>> root = insert(root, 3)
    >>> root.left.value
    3
    """
    raise NotImplementedError


def in_order(root: TreeNode | None) -> list[int]:
    """Return every value in the tree, smallest to largest.

    For each node: everything on its left, then the node itself, then
    everything on its right. The ordering rule makes that come out
    sorted, with no sorting needed.

    >>> in_order(TreeNode(8, TreeNode(3), TreeNode(10)))
    [3, 8, 10]
    """
    raise NotImplementedError


def height(root: TreeNode | None) -> int:
    """Return the number of levels in the tree. An empty tree has 0.

    The height decides how fast a tree is to search. A tree built by
    inserting 1, 2, 3, 4 in order is as tall as it is long, and no
    faster than a linked list.

    >>> height(TreeNode(8, TreeNode(3), TreeNode(10)))
    2
    """
    raise NotImplementedError


def is_valid_bst(root: TreeNode | None) -> bool:
    """Return True if the tree obeys the ordering rule everywhere.

    Checking each node against its own two children isn't enough. A
    value deep in the left subtree must be smaller than every ancestor
    it sits to the left of, not only its parent. Either pass the allowed
    range down as you go, or use what you know about in_order. An empty
    tree is valid, and a tree with a repeated value is not.

    >>> is_valid_bst(TreeNode(8, TreeNode(3), TreeNode(10)))
    True
    >>> is_valid_bst(TreeNode(8, TreeNode(9), TreeNode(10)))
    False
    """
    raise NotImplementedError


def remove(root: TreeNode | None, value: int) -> TreeNode | None:
    """Remove value from the tree and return the root. (Stretch)

    The tree must still obey the ordering rule afterwards. There are
    three cases for the node being removed:

    - no children: it disappears
    - one child: that child takes its place
    - two children: copy in the smallest value from its right subtree,
      then remove that value from the right subtree instead

    If the value isn't in the tree, nothing changes.

    >>> in_order(remove(TreeNode(8, TreeNode(3), TreeNode(10)), 8))
    [3, 10]
    """
    raise NotImplementedError
