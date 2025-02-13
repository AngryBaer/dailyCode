"""
    Daily Coding Problem 3:

    Given the root to a binary tree, implement serialize(root), which serializes the tree into a
    string, and deserialize(s), which deserializes the string back into the tree.

    For example, given the following Node class

    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    The following test should pass:

    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
"""


# ----------------------------------------------------------------------------------------------- #
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root: Node) -> str:
    if root is None:
        return 'None'

    return f"{root.val} {serialize(root.left)} {serialize(root.right)}"


def deserialize(s: str) -> Node:
    def resolve_subtree():
        value = next(all_values)

        if value == "None":
            return None

        node_object = Node(value)
        node_object.left = resolve_subtree()
        node_object.right = resolve_subtree()
        return node_object

    all_values = iter(s.split())
    return resolve_subtree()


# ----------------------------------------------------------------------------------------------- #
if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
# ----------------------------------------------------------------------------------------------- #
