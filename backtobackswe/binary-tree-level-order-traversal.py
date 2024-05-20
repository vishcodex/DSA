# Given a binary tree as input return its level order traversal.



def levelOrderTraversal(root):
    '''
    :type root: TreeNode
    :rtype: list of list of int
    '''
    level = []
    visited = []

    if root == None:
        return []

    queue = []
    queue.append(root)

    while len(queue) != 0:
        layer = []
        layer_size = len(layer)
        for i in range(0, layer_size):
            current_node = queue.pop(0)
            layer.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        level.append(layer)

    return level


if __name__ == "__main__" :

    a = levelOrderTraversal(1)

    # root.left = Node(2)
    # root.right = Node(3)
    # root.left.left = Node(4)
    # root.left.right = Node(5)
    print(a)

