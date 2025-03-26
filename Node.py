# create class for a single node
class Node():
    def __init__(self,userid, value):
        # values needed for each node
        self.userid = userid
        self.parent = None
        self.right = None
        self.left = None
        self.value = value
        self.multiplier = 1
        self.color = 0  # 0 is black and 1 is red
        self.tier = "bronze"


    def __repr__(self):
        return "Userid:"+str(self.userid) + " value:" +str(self.value)