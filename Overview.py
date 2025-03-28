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

def update_points(node,value):
        node.value += (value * node.multiplier)
        if node.value >= 1000 and node.tier == "bronze":
            node.tier = "silver"
            node.value = 0
            RBTsilver.insert(node.userid , node)
            return "User id:"+str( node.userid) + " has reached silver"



user_hashmap = HashMap()
bronze_HM = HashMap()
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
            RBTgold.insert(customnode)
        elif tier =="platinum":
            RBTplat.insert(customnode)
        else:
            bronze_HM.hm_insertnew(customnode)
        user_hashmap.hm_insertnew(User(i,customnode ))

def luckytier(tier , multiplier):
    if tier == "silver":
        for node in RBTsilver.inorder_traversal(RBTsilver.root,[]):
            node.multiplier = multiplier
    elif tier == "gold":
        for node in RBTgold.inorder_traversal(RBTgold.root,[]):
            node.multiplier = multiplier
    elif tier == "platinum":
        for node in RBTplat.inorder_traversal(RBTplat.root, []):
            node.multiplier = multiplier

def inputs():
    inp =0
    while True:
        if inp != 0:
            inp = input("Would you like to continue? (y/n)")
            if inp == "n":
                break
        print("1: Show users in each tier")
        print("2: Show users in top/bottom of each tier")
        print("3: Simulate weekly updates")
        print("4: Add or remove points from a single user")
        print("5: Get single user information")
        print("6: Assign lucky user")
        print("7: Assign lucky tier")

        inp = input("What would you like to do? Input:")
        if inp =="1":
            print("\n********Showing Bronze users ********")
            print(bronze_HM.getall())
            sleep(0.4)
            print("\n********Showing RBT silver users using in-order traversal (ascending order of values) ********")
            print(RBTsilver.inorder_traversal(RBTsilver.root, []))
            sleep(0.4)
            print("\n********Showing RBT gold users using in-order traversal (ascending order of values)******** ")
            print(RBTgold.inorder_traversal(RBTgold.root, []))
            sleep(0.4)
            print("\n********Showing RBT plat users using in-order traversal (ascending order of values)********")
            print(RBTplat.inorder_traversal(RBTplat.root, []))
            sleep(0.4)
        elif inp == "2":
            placeholder, topsilver = RBTsilver.TOP_BTM()
            print("\ntop users in silver     ", str(topsilver))

            btmgold, topgold = RBTgold.TOP_BTM()
            print("bottom users in gold    ", str(btmgold))
            print("top users in gold       ", str(topgold))

            btmplat, placeholder = RBTplat.TOP_BTM()
            print("bottom users in platinum", str(btmplat))
            sleep(1)
        elif inp == "3":
            print("Updating users...")
            sleep(0.5)
            weeklyupdate(RBTsilver, RBTgold, RBTplat)
            print("Update done, showing users after the update")
            print("\n********Showing Bronze users ********")
            print(bronze_HM.getall())
            sleep(0.4)
            print("\n********Showing RBT silver users using in-order traversal (ascending order of values) ********")
            print(RBTsilver.inorder_traversal(RBTsilver.root, []))
            sleep(0.4)
            print("\n********Showing RBT gold users using in-order traversal (ascending order of values)******** ")
            print(RBTgold.inorder_traversal(RBTgold.root, []))
            sleep(0.4)
            print("\n********Showing RBT plat users using in-order traversal (ascending order of values)********")
            print(RBTplat.inorder_traversal(RBTplat.root, []))
        elif inp == "4":
            userid = int(input("What is userid of user you would like to change? Input:"))
            value = int(input("How much to update the points by? Input:"))
            #finish this
            user_info = user_hashmap.hm_getuser(userid)
            update_points(user_info.node,value)
            print("User " + str(userid) + " points updated.")
        elif inp == "5":
            user_id = int(input("What is the user id of user to be retrived? Input:"))
            user_info = user_hashmap.hm_getuser(user_id)
            print("\n******** User "+ str(user_id) +" info ********")
            print("points      : " + str(user_info.node.value))
            print("multiplier  : " + str(user_info.node.multiplier))
            print("current tier: " + str(user_info.node.tier))
        elif inp == "6":
            userid = int(input("What is userid of user you would like to make as a lucky user? Input:"))
            value = float(input("How much to multiply the points by?(number above 1.0) Input:"))
            user_info = user_hashmap.hm_getuser(userid)
            user_info.node.multiplier = value
            print("Updated the multiplier!")
        elif inp == "7":
            tier = input("Which tier would you like to make lucky? (bronze , silver , gold , platinum) Input:")
            value = float(input("How much to multiply the points by?(number above 1.0) Input:"))
            if tier == "bronze":
                for node in bronze_HM.getall():
                    node.multiplier = value
                print("Updated the multiplier of tier!")
            elif tier == "silver":
                for node in RBTsilver.inorder_traversal(RBTsilver.root):
                    node.multiplier = value
                print("Updated the multiplier of tier!")
            elif tier == "gold":
                for node in RBTgold.inorder_traversal(RBTgold.root):
                    node.multiplier = value
                print("Updated the multiplier of tier!")
            elif tier == "platinum":
                for node in RBTplat.inorder_traversal(RBTplat.root):
                    node.multiplier = value
                print("Updated the multiplier of tier!")
            else:
                print("Invalid! Try again")

        else:
            print("Invalid input! Please only input numbers from 1 to 7")

createuser(100)
print("CREATED 100 random users, in random tiers \n")
inputs()
 