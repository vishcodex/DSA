# Given a binary tree as input return its level order traversal.


# A node structure
class TreeNode:

    # A utility function to create a new node
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative Method to print the
class Solution:
    def levelOrderTraversal(self, root):
        '''
        :type root: TreeNode
        :rtype: list of list of int
        '''

        if root is None:
            return []

        levels_list = []

        queue = []
        queue.append(root)

        while len(queue) != 0:
            current_layer = []

            layer_size = len(queue)

            for i in range(0, layer_size):
                current_node = queue.pop(0)

                current_layer.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)

            levels_list.append(current_layer)
        return levels_list


if __name__ == "__main__" :
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()

    res = sol.levelOrderTraversal(root)

    print(res)


