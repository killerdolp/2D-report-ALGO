# create class for a single node
class Node():
    def __init__(self,userid, value):
        # values needed for each node
        self.userid = userid
        self.parent = None
        self.right = None
        self.left = None
        self.value = value
        self.color = 0  # 0 is black and 1 is red
