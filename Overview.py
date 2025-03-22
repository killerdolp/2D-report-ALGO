from Node import Node
from Hashmap import HashMap
from User import User


def weeklyupdate(RBTsilver,RBTgold,RBTplat):

    placeholder , topsilverusers = RBTsilver.TOP_BTM("silver")
    for node in topsilverusers:
        node.tier = "gold"
        RBTsilver.delete(node)
        RBTgold.insert(node)

    btmgoldusers , topgoldusers = RBTgold.TOP_BTM("gold")
    for node in btmgoldusers:
        node.tier = "silver"
        RBTgold.delete(node)
        RBTsilver.insert(node)

    for node in topgoldusers:
        node.tier = "platinum"
        RBTgold.delete(node)
        RBTplat.insert(node)

    btmplatusers , placeholder = RBTplat.TOP_BTM('platinum')
    for node in btmplatusers:
        node.tier = "gold"
        RBTplat.delete(node)
        RBTgold.insert(node)


user_hashmap = HashMap()
user_hashmap.hm_insertnew(User(0,Node(0,0)))
user_hashmap.hm_insertnew(User(1,Node(1,0)))
user_hashmap.hm_insertnew(User(2,Node(2,0)))
user_hashmap.hm_insertnew(User(3,Node(3,0)))
user_hashmap.hm_insertnew(User(4,Node(4,0)))
