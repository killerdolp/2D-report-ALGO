
class User():
    def __init__(self, userid, node):
        # values needed for each node
        self.userid = userid
        self.node = node

    def __repr__(self):
        return "UserID: " +str(self.userid)
