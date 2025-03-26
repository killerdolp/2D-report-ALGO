from time import sleep
from Node import Node
from Hashmap import HashMap
from User import User
from redblacktree import RedblackBST
import random
RBTsilver = RedblackBST("silver")
RBTgold = RedblackBST("gold")
RBTplat = RedblackBST("platinum")
def weeklyupdate(RBTsilver,RBTgold,RBTplat):

    placeholder , topsilverusers = RBTsilver.TOP_BTM()
    for node in topsilverusers:
        node.tier = "gold"
        RBTsilver.delete(node)
        RBTgold.insert(node)

    btmgoldusers , topgoldusers = RBTgold.TOP_BTM()
    for node in btmgoldusers:
        node.tier = "silver"
        RBTgold.delete(node)
        RBTsilver.insert(node)

    for node in topgoldusers:
        node.tier = "platinum"
        RBTgold.delete(node)
        RBTplat.insert(node)

    btmplatusers , placeholder = RBTplat.TOP_BTM()
    for node in btmplatusers:
        node.tier = "gold"
        RBTplat.delete(node)
        RBTgold.insert(node)

def update_points_bronze(node,value):
        node.value += (value * node.multiplier)
        if node.value >= 1000 and node.tier == "bronze":
            node.tier = "silver"
            node.value = 0
            RBTsilver.insert(node.userid , node)
            return "User id:"+str( node.userid) + " has reached silver"


user_hashmap = HashMap()

#function to generate users
def createuser(howmany):
    tiername = ["bronze", "silver", "gold", "platinum"]
    for i in range(howmany):
        value = random.randint(1,99)
        customnode = Node(i,value)
        tier = tiername[random.randint(0,3)]
        customnode.tier = tier
        if tier == "silver":
            RBTsilver.insert(customnode)
        elif tier =="gold":
            RBTgold.insert( customnode)
        elif tier =="platinum":
            RBTplat.insert( customnode)
        user_hashmap.hm_insertnew(User(i,customnode ))


print("CREATING 100 random users, in random tiers")
createuser(100)
sleep(1)

print("\n********Showing RBT silver in-order traversal (ascending order of values) ********")
print(RBTsilver.inorder_traversal(RBTsilver.root,[]))
sleep(1)
print("********Showing RBT gold in-order traversal (ascending order of values)******** ")
print(RBTgold.inorder_traversal(RBTgold.root,[]))
sleep(1)
print("********Showing RBT plat in-order traversal (ascending order of values)********")
print(RBTplat.inorder_traversal(RBTplat.root,[]))
sleep(1)

placeholder , topsilver = RBTsilver.TOP_BTM()
print("\ntop users in silver     " , str(topsilver))

btmgold , topgold = RBTgold.TOP_BTM()
print("bottom users in gold    " , str(btmgold))
print("top users in gold       " , str(topgold))

btmplat , placeholder = RBTplat.TOP_BTM()
print("bottom users in platinum" , str(btmplat))

#use weekly update function to move the nodes
weeklyupdate(RBTsilver,RBTgold,RBTplat)
print("\nAFTER weekly update")
print("\n********Showing RBT silver in-order traversal (ascending order of values) ********")
print(RBTsilver.inorder_traversal(RBTsilver.root,[]))
sleep(1)
print("********Showing RBT gold in-order traversal (ascending order of values)******** ")
print(RBTgold.inorder_traversal(RBTgold.root,[]))
sleep(1)
print("********Showing RBT plat in-order traversal (ascending order of values)********")
print(RBTplat.inorder_traversal(RBTplat.root,[]))