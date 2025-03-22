from collections import deque
from Node import Node

class RedblackBST():
    def __init__(self):
        # set the node as a null node so that we can use it we can use it for dummy variables later
        self.nullnode = Node(0)
        self.root = self.nullnode


    def left_rotate(self, node):
        rightchild = node.right
        node.right = rightchild.left

        if rightchild.left != self.nullnode:
            rightchild.left.parent = node

        rightchild.parent = node.parent

        if node.parent is None:  # Ensuring proper root update
            self.root = rightchild
        elif node == node.parent.left:
            node.parent.left = rightchild
        else:
            node.parent.right = rightchild

        rightchild.left = node
        node.parent = rightchild

    def right_rotate(self, node):
        leftchild = node.left
        node.left = leftchild.right

        if leftchild.right != self.nullnode:  # Ensure consistency with self.nullnode
            leftchild.right.parent = node

        leftchild.parent = node.parent

        if node.parent is None:  # Ensure correct root update
            self.root = leftchild
        elif node == node.parent.right:
            node.parent.right = leftchild
        else:
            node.parent.left = leftchild

        leftchild.right = node
        node.parent = leftchild

    #insert operation
    def insert(self, value):
        node = Node(value)
        node.parent = None
        node.left = self.nullnode
        node.right = self.nullnode
        node.color = 1

        checknode = self.root
        node_to_insert_at = None
        # find where to insert the node at
        while checknode != self.nullnode:
            node_to_insert_at = checknode
            if node.value > checknode.value:
                checknode = checknode.right
            else:
                checknode = checknode.left

        # tells which node is the parent
        node.parent = node_to_insert_at

        # this means that there is no elements in the BST
        if node_to_insert_at == None:
            self.root = node
        # insert the node
        elif node.value > node_to_insert_at.value:
            node_to_insert_at.right = node
        else:
            node_to_insert_at.left = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def fix_insert(self, node):
        while node.parent.color == 1:
            if node.parent == node.parent.parent.left:
                rightgp = node.parent.parent.right  # this is the uncle
                # case 1 , when the right child of gp (grandparent) is red
                if rightgp.color == 1:
                    rightgp.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                # case 2
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    # case 3
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.right_rotate(node.parent.parent)
            else:
                # same thing as above, just different side
                leftgp = node.parent.parent.left
                if leftgp.color == 1:
                    leftgp.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent

                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.left_rotate(node.parent.parent)
            if node == self.root:
                break

        self.root.color = 0
    def search_for_node(self,node,key):
        if node == None:
            return None
        if node.value == key:
            return node
        if node.value > key:
            return self.search_for_node(node.left,key)
        else:
            return self.search_for_node(node.right,key)

    def replace(self,deletenode,node):
        if deletenode.parent == None:
            self.root = node
        elif deletenode == deletenode.parent.left:
            deletenode.parent.left = node
        else:
            deletenode.parent.right = node
        node.parent = deletenode.parent

    def delete(self,key):
        node = self.search_for_node(self.root,key)
        if node == None:
            print("Node does not exist")
            return
        orginalColor = node.color
        if node.left == self.nullnode:
            self.replace(node,node.right)
        elif node.right == self.nullnode:
            self.replace(node,node.left)
        else:
            #find for minimum node
            minimum = node.right
            while minimum.left != self.nullnode:
                minimum = minimum.left
            orginalColor = minimum.color
            temp = minimum.right
            if minimum.parent == node:
                temp.parent = minimum
            else:
                self.replace(minimum,minimum.right)
                minimum.right = node.right
                minimum.right.parent = minimum
            self.replace(node, minimum)
            minimum.left = node.left
            minimum.left.parent = minimum
            minimum.color = node.color
        if orginalColor == 0:
            self.delete_fix(temp)
    def delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0
    def print_rbt_top_down(self):
        """ Print the Red-Black Tree in a visually structured format. """
        if not self.root or self.root == self.nullnode:
            print("Tree is empty.")
            return

        queue = deque([(self.root, 0, 0)])  # (node, level, position)
        levels = {}

        while queue:
            node, level, pos = queue.popleft()

            if level not in levels:
                levels[level] = {}

            if node == self.nullnode:
                levels[level][pos] = "  "  # Represent NIL nodes with empty spaces
            else:
                color = "🔴" if node.color == 1 else "⚫"
                levels[level][pos] = f"{node.value}{color}"

                queue.append((node.left if node.left else self.nullnode, level + 1, pos * 2))
                queue.append((node.right if node.right else self.nullnode, level + 1, pos * 2 + 1))

        # Formatting the output
        max_width = 6 * (2 ** (max(levels.keys())))  # Ensure even spacing

        for i in sorted(levels.keys()):
            row = ""
            connectors = ""

            for pos in sorted(levels[i].keys()):
                row += levels[i][pos].center(6)


            print(row.center(max_width))
            if i < max(levels.keys()):
                print(connectors.center(max_width))


# Example Usage:
rbt = RedblackBST()

# Inserting some values
rbt.insert(50)
rbt.insert(30)
rbt.insert(70)
rbt.insert(20)
rbt.insert(40)
rbt.insert(60)
rbt.insert(80)
rbt.insert(90)
rbt.insert(100)
rbt.insert(110)
rbt.insert(120)


# Printing the Red-Black Tree top-down
rbt.print_rbt_top_down()
rbt.delete(40)
rbt.delete(50)
rbt.delete(30)
rbt.print_rbt_top_down()