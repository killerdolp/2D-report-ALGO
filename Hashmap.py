from Node import Node
from User import User
class HashMap:
    def __init__(self):
        self.table_size = 100
        self.table = [[] for j in range(self.table_size)]
        self.total_users = 0
        self.load_factor = 0.75

    def hm_hashing(self,userid):
        return userid % self.table_size

    def hm_insertnew(self,user):
        if (self.total_users / self.table_size) > self.load_factor:
            self.hm_resizetable()
        index = self.hm_hashing(user.userid)
        self.table[index].append(user)

    def hm_resizetable(self):
        newtablesize = self.table_size * 2
        newtable = [[] for j in range(newtablesize)]

        for i in range(0,self.table_size):
            for user in self.table[i]:
                new_index = self.hm_hashing(user.userid)
                newtable[new_index].append(user)
        self.table = newtable
        self.table_size = newtablesize

    def hm_getuser(self,userid):
        index = self.hm_hashing(userid)
        for user in self.table[index]:
            if user.userid == userid:
                return user
        return None

    def hm_deleteuser(self):
        pass

user_hashmap = HashMap()

user_hashmap.hm_insertnew(User(0,Node(0,0)))
user_hashmap.hm_insertnew(User(1,Node(1,0)))
user_hashmap.hm_insertnew(User(2,Node(2,0)))
user_hashmap.hm_insertnew(User(3,Node(3,0)))
user_hashmap.hm_insertnew(User(4,Node(4,0)))
