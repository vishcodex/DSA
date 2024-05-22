
class Tree:
    def __init__(self, key=None, left=None, right=None):
        self.key=key
        self.left = left
        self.right = right

def levelOrderTraversal(root, level):

    while True:

        if root is None:
            return False

        if level == 1:
            print(root.key, end=" ")
            return True

        left = levelOrderTraversal(root.left, level-1)
        right = levelOrderTraversal(root.right, level-1)

        return left or right


def levelOrder(root):
    # start from level 1 — till the height of the tree
    level = 1

    while levelOrderTraversal(root, level):
        level = level + 1


if __name__ == '__main__':

    root = Tree(15)
    root.left = Tree(10)
    root.right = Tree(20)
    root.left.left = Tree(8)
    root.left.right = Tree(12)
    root.right.left = Tree(16)
    root.right.right = Tree(25)


    levelOrder(root)
