
---
# Title page

<div align="center">
  <table>
    <tr>
      <th>Team Members</th>
      <th> Student id</th>
    </tr>
    <tr>
      <td>Ryan</td>
      <td>Data 2</td>
    </tr>
        <tr>
      <td>Kendrix</td>
      <td>Data 2</td>
    </tr>
        <tr>
      <td>Shana</td>
      <td>Data 2</td>
    </tr>
        <tr>
      <td>Jing Jie</td>
      <td>Data 2</td>
    </tr>
        <tr>
      <td>Darren</td>
      <td>Data 2</td>
    </tr>
        <tr>
      <td>Gerald</td>
      <td>Data 2</td>
    </tr>
        <tr>
      <td>Donovan</td>
      <td>Data 2</td>
    </tr>
  </table>
</div>

---
# Executive summary

As tasked by the CEO of YouTwitFace, Denis, our newly formed "Rewards System Team" has designed a database system to store the points/tier for all users of YouTwitFace.

Users gain/lose points from their interactions on any of YouTwitFace's platforms, similar to [Reddit's karma](https://support.reddithelp.com/hc/en-us/articles/204511829-What-is-karma) system. On top of the points system, users are categorised into 4 tiers, namely Bronze, Silver, Gold and Platinum. At the end of every week (Sunday 12am), the system will promote/demote users between tiers based on the points that they have accumulated over the past week.

Each of YouTwitFace's platforms will offer more benefits for being in a higher tier, such as access to unique emotes, and advertisement skips.

This hybrid points/tier system approach aims to encourage users of YouTwitFace's various platforms to **1. maintain consistent usage**, and **2. reward positive conduct**.

### Maintain Consistent Usage
By making our promotion/demotion cycles weekly, we aim to encourage users to consistently interact on the platform to rise/maintain their tier level. This protects the tier system against one-hit wonders, where a user gains a high rank for one extraordinary upload/comment.
### Reward Positive Conduct
By implementing a system where users can gain/lose points based on their interactions on various platforms, we aim to create a self-moderating ecosystem that encourages positive and inclusive behaviour. This system aims to address SDG goals 3, 5 and 10.
## Service Requirements
 The rewards system serves as core service to the various app teams in YouTwitFace, and each app team must be able to:
- add/retrieve any user's current point and tier
- increase/reduce points based on a user's usage on any of YouTwitFace's platforms
- query for an ordered list of users in any of the tiers, when a user wants to view the the leaderboard on any of YouTwitFace's platforms


---
# User Ranking System

The ranking system is designed in a way to incentivise user engagement and reward top-performing users. There are 4 tiers in this system (Bronze, Silver, Gold and Platinum). A user can gain points by gaining likes and comments on their posts and videos. They would lose points by receiving dislikes and reports. Rank progression is determined by a weekly leaderboard, where high performing users, are promoted, and low performing users are demoted. Weekly rankings are only based on points accumulated **only** in that week.

## Ranking Progression Rules
- **Bronze to Silver**
	- Bronze tier users would be promoted to Silver upon obtaining 1000 points.
	- Users would not be able to demote from Bronze to Silver.
- **Silver to Gold**
	- Silver tier users in the top 20% of the weekly leaderboard would be promoted to Gold.
- **Gold to Platinum**
	- Gold tier users in the top 10% of the weekly leaderboard would be promoted to Platinum.
   
#### Demotion Rules
To ensure user engagement and competitive fairness, Gold and Platinum players have to maintain their rankings.
- If a **Gold** user is in the bottom 20%, the user will be demoted to Silver
- If a **Platinum** user is in the bottom 10%, the user will be demoted to Gold.

A **Silver** user is not able to be demoted to Bronze. This allows the user to have a sense of accomplishment reinforcing a positive user experience. Furthermore, by preventing the demotion to bronze, it ensures motivation for those users who had a temporary decline in activity for the week.

---
# Database diagram
==Figure 1== 
<div align="center">
<img alt="center" src="Untitled Diagram.drawio (1).png" width="500px" height="300px">
</div>

==Figure 1== is a high-level overview of the tables.  The diagram illustrates that the User table contains a User class, which includes a nested Node class along other attributes, detailed below. Each user belongs to **only** one tier at any given moment. This is determined by the attribute `user.node.tier` to which specifies the tier and determine the corresponding table which the user would be stored. For simplicity, we will collectively refer to `Hashmap_bronze` , `rbt_silver` , `rbt_gold` and `rbt_platinum` as the **Rewards Points table**
##### User class 
```
Class User:
	integer userid     
	Node node
```

> [!Other attributes, such as username and password exist in the user class, but they are not relevant to the data structure.]

This are 2 main attributes that are needed in the User class 
- The `userid` to uniquely identify each user.
- The `node` a custom class that stores user's points and tier (E.g node.points = 0 and node.tier  ="bronze")
##### Node Class
```
Class Node(user_id):
	Requires: a new user id from the User table
	
	String color  <- "red"      // Default color of new nodes are red
	integer points <- 0         // Default membership points
	integer weekly_points <-0   // amount of points gained in that week
	String tier <- "Bronze"     // Default membership tier
	Node left <- NIL
	Node right <- NIL
	Node parent <- NIL
	integer userid <- user_id
```

The `Node` class contains several key attributes essential for maintaining the Reward points table structure and functionality of a **RBT**. The `color` attribute ensures the tree remains balanced according to Red-Black Tree properties. The `points` attribute stores the user’s reward points, while `tier` represents the user's membership ranking. The `left`, `right`, and `parent` attributes establish links between nodes. Finally, `user_id` uniquely identifies each node, associating it with a specific user.


---

# Algorithms
## HashMap
The data structure used to store the **User** table would be a HashMap.  HashMap offers average-case $O(1)$ time complexity for insertion, deletion and lookups ,making it much faster than most algorithms. While HashMap has a worst-case time complexity of $O(n)$ due to collisions (adding all into one key) , this can be negated by choosing an effective hash function and maintaining a low load factor. 
```
Class HashMap():
	Table <- An array of lists     // Create default hash map
	integer table_size <- 100      //default size
	integer total_users <- 0
	load_factor <- 0.75            //Load factor is used for resizing table 
```

```
FUNCTION HM_HASHING(userid)
	Require: userid of the user

	return user_id % table_size
```
The `HM_hashing` function is a sub function used in most HashMap functions. It takes in the `userid` of the user and returns a value index within the HashMap table.

```
FUNCTION HM_INSERTNEW(hashmap,user)
	Require: hashmap containing user class
	Require: User class containing userid and node

	IF (Hashmap.total_users / Hashmap.table_size) > hashmap.load_factor do
		HM_RESIZETABLE(Hashmap)
	index <- HM_HASHING(user.userid)
	table[index] <- table[index] + user  //insert user into table
	
```
The `HM_INSERTNEW` function is used when a new user creates their account. The main information of the users is then inserted into the HashMap. It function works by checking if the table exceeds the threshold (load factor) and resizes the table using `HM_RESIZETABLE()` then it uses `HM_HASHING` to determine index to store the user at. Using the index, we add the user to the hash table.

```
FUNCTION HM_RESIZETABLE(hashmap)
	Require: hashmap containing user class
	
	new_table_size <- table_size * 2 
	newtable <-  An array of lists (size of new_table_size)

	FOR each list in hashmap.table do
		For each (index,user) in list do 
			new_index = HM_HASHING(user.id)
			newtable[index] <- newtable[index] + user

	Hashmap.table <- newtable 
	Hashmap.table_size <- new_table_size
```
When the the table exceed threshold ,`HM_RESIZETABLE` is used. This is to prevent excessive collisions and maintain efficiency , ensuring that the worse case $O(n)$ would never happen. This is done by making the new table size twice as big, getting all elements in HashMap ,  re-indexing the elements , and adding them to the new table.

```
FUNCTION HM_GETUSER(hashmap,useridkey)
	Require: hashmap containing user class
	Require: a userid of a User class 

	index <- HM_HASHING(useridkey)
	FOR user in hashmap.table[index]
		IF user.userid == useridkey do
			return user
	return NIL
```
The function `HM_GETUSER`is the most commonly used function in this  data structure.  Since it contains the relevant user information, including the node which contains points and tier. Given its frequent usage, it is **crucial** that the operation for this maintains at least an average case of $O(1)$ time complexity by managing the load factor and choosing a good hash function.

```
FUNCTION HM_DELELEUSER(RBT,userid)
	Require: RedBlackTree class of silver ,gold or platinum members that has nodes as elements
	Require: userid of a user class
	
	index <- HM_HASHING(useridkey)
	FOR user in hashmap.table[index]
		IF user.userid == useridkey do
			REMOVE user from hashmap.table[index]
			
			IF user.tier == "SILVER" do
				DELETE_USER(RBT,user.node)
			ELSE IF user.tier == "GOLD" do
				DELETE_USER(RBT,user.node)
			ELSE IF user.tier == "PLATINUM" do
				DELETE_USER(RBT,user.node)
				
			return "removed"
	return NIL
```
The function `HM_DELETEUSER` removes a user from the **HashMap** and ensures that their corresponding **tiered data** is also deleted from the appropriate **Red-Black Tree (RBT)** based on their membership tier. The `DETELE_USER` function would be explain more later. [[Report#Delete Operation]]
## Red black Tree
The algorithm used to store **Reward point** table for each tier would be the **Red-Black Tree** algorithm. For every tier except for the Bronze tier, it would have its own RBT tree.
- Bronze users are stored in a much simpler structure (e.g. an unsorted list or hash table) as sorting is unnecessary. Promotion to silver happens immediately at 100 points and the user is unable to drop back to bronze. 
- Silver, Gold and Platinum tiers each have there own RBT because sorting is required (only the top / bottom users are eligible for promotion or demotion)
- When a user is promoted or demoted, they are removed from the current RBT and inserted into the corresponding tier's RBT 

The Red Black Tree is an modified version of the Binary Search Tree. This are the few reasons why this algorithm was chosen :
- A normal Binary Search tree can degrade to $O(n)$ lookup time while RBT maintains at $O(log n)$ time due to its self balancing nature
- Among all the Binary Search trees, Red Black Tree offers one of the most efficient update times. Since updates to the rewards points table occur only at the end of the week, requiring $n$ updates but only a single traversal of the graph, the Red-Black Tree is a well-suited choice.
- Better then heap when getting an ordered retrieval. As a min/max heap is great for getting the highest or lowest point, but it is not efficient when doing range queries (E.g. getting top 20% of players).

<div align="center">
<b>Example of Red Black Tree</b>
<img alt="center" src="Pasted image 20250321225017.png" width="650px" height="350px">
</div>

In a red-black tree there are 4 rules to be followed:
1. A node can only be black or red
2. The root and leaf nodes are black
3. If a node is red, then the children nodes are black
4. ALL paths from a node to its descendants should have the same number of black nodes

```
Class RedBlackTree:
	Node root <- NIL   //Default empty Tree
	Integer size <- 0  // Integer Size
```

The **RBT** class only contain 2 key attributes, 
The Node `root`  represents the starting of point of the tree. When the tree is empty, root is NIL as there are no nodes yet. All main operations such as insert, delete and update starts from this `root` node.
The integer `size` use to retrieve the top people in the scoreboard efficiently

### Sub-Operations
Before we dive into the main operations for the rewards system, there are some fundamental sub-operations that would be used in the following main operations (insert, delete and update).
##### Rotation Operation
```
FUNCTION ROTATE_LEFT(RBT,node):
	Require: RedBlackTree class that has nodes as elements
	Require: A node from RBT

	rightchild <- node.right 
	node.right <- rightchild.left
	IF rightchild.left != NIL do
		rightchild.left.parent <- node
		
	rightchild.parent = node.parent

	//If node is the root
	IF node.parent is NIL:
		RBT.root <- rightchild
	ELSE IF node == node.parent.left do 
		node.parent.left <- rightchild 
	ELSE do
		node.parent.right <- rightchild

	rightchild.left <- node 
	node.parent <- rightchild
	
```

```
FUNCTION ROTATE_RIGHT(node):
	Require: RedBlackTree class that has nodes as elements
	Require: A node from RBT

	leftchild <- node.left
	node.left <- leftchild.right
	IF leftchild.right != NIL do
		leftchild.right.parent <- node 

	leftchild.parent = node.parent

	// IF node is the root
	if node.parent is NIL do
		RBT.root <- leftchild
	ELSE IF node == node.parent.right do 
		node.parent.right <- leftchild 
	ELSE do
		node.parent.left <- leftchild 

	leftchild.left <- node 
	node.parent <- leftchild
	
```

These are the 2 types of rotations.
- The left rotation helps to balance the right-heavy tree by shifting the node down and bringing the right child of the node up
- The right rotation helps to balance the left-heavy trees by shifting the node down and bringing the left child of the node up.

<div align="center">
    <img src="rotateleft.jpg" alt="Image 1" width="35%">
    <img src="rotateright.jpg" alt="Image 2" width="35%">
</div>


(Change the colour of the picture and make only A highlight red)

Both ROTATE_LEFT and ROTATE_RIGHT are functions originally used in the Binary Search Tree to help restructure the tree. They are used in RBT to not only help maintain the balanced tree structure but helps to update the colours to preserve RBT properties after some operations.
##### Move Tree operations
```
FUNCTION MOVETREE(RBT,replacednode,node)
	Require: RedBlackTree class that has nodes as elements
	Require: a node that is to be removed from the RBT 
	Require: node to replaced at the replaced node
	
	if deletenode.parent == NIL do 
		RBT.root <- node
	elif deletenode == deletenode.parent.left:
		deletenode.parent.left. <- node 
	else:
		delelenode.parent.right <- node
	node.parent <- deletenode.parent
```

The move tree operation  replaces the subtree of `replace` with the subtree of `node`. Which adjusts the parent-child relationship of the node accordingly.

##### In-order Traversal Operation
```
FUNCTION INORDERTRAVERSAL(node,nodelist):
	Requires: an interger value
	Requires: nodelist which is an array of nodes
	
	IF node == NIL do
		return nodelist
		
	INORDERTRAVERSAL(node.left,nodelist)
	nodelist <- nodelist + node
	INORDERTRAVERSAL(node.right,nodelist)
	return nodelist
```
The `INORDERTRAVERSAL` function is a recursive algorithm that performs a in order traversal of the binary tree and records the node traversed. An in-order traversal visits the left subtree first, followed by the node then the right subtree. This would return the nodes in ascending order.

```
FUNCTION FIND_MAX(node):
	Require: A node from RBT
	
	max_node <- node
	WHILE node.right != NIL do
		max_node <- node.right

	return max_node
```
```
FUNCTION FIND_MIN(node):
	Require: A node from RBT
	min_node <- node
	WHILE node.left != NIL do
		min_node <- node.left

	return min_node
```
The `FIND_MAX` and `FIND_MIN` functions work as the largest value is found in the right most node and the smallest value is found in the left most node. therefore, the function only has to traverse the right or left most node to find the maximum and minimum.

```
FUNCTION FIND_SUCCESSOR(node):
	Require: A node from RBT
	//**** CASE 1 ****
	IF node.right != NIL do 
		return FIND_MIN(node.right)
	//**** CASE 2 ****
	successor <- node.parent
	WHILE successor != NIL and node = successor.right do 
		node <- successor
		successor <- successor.parent
	return successor	
```
The function `FIND_SUCCESSOR` finds the largest node smaller than the given node. There are 2 cases to find for the successor.
- **Case 1:** If the node has a right child
		The successor would be the left most node in the right subtree. We can do this by calling function `FIND_MIN(node.right)`  which returns the left most value in the `node.right` subtree 
- **Case 2:** If the node has no right child
		The successor is the first ancestor where the give node is in the left subtree. Until we find such ancestor, we move up the tree using `node.parent`

```
FUNCTION FIND_PREDECESSOR(node):
	Require: A node from RBT
	
	IF node.left != NIL do 
		return FIND_MAX(node.left)
	predecessor <- node.parent
	WHILE predecessor != NIL and node == predecessor.left do 
		node <- predecessor
		predecessor <- predecessor.parent
	return predecessor
```
The function `FIND_PREDECESSOR` finds the smallest node larger than the given node. There are 2 cases to find for the successor.
- **Case 1:** If the node has a left child
		The predecessor would be the right most node in the left subtree. We can do this by calling function `FIND_MAX(node.right)`  which returns the right most value in the `node.left` subtree 
- **Case 2:** If the node has no left child
		The predecessor is the first ancestor where the give node is in the right subtree. Until we find such ancestor, we move up the tree using `node.parent`

### Main Operations
##### Insert operation
```
FUNCTION RB_INSERTNEW(RBT,user_id)
	Require: RedBlackTree class that has nodes as elements
	Require: User_id from the User table

	node <- NEW Node(user_id)
	node.color <- "red"             //make the node red
	node.parent <- NIL 
	node.left <- NIL
	node.right <- NIL 
	node.point <- 0             // new user always starts with 0 points
	
	IF RBT.root != NIL do
		node.color <- "black"
		RBT.root = node
		return
		
	//find where to insert the node 
	check_node <- RBT.node
	node_to_insert_at <- NIL
	WHILE check_node != NIL do
		node_to_insert_at <- check_node 
		IF node.points > check_node.points do 
			check_node <- check_node.right
		ELSE
			check_node <- check_node.left
	
	//tells which node is the parent	
	node.parent <- node_to_insert_at 

	//is the node is a left or right child
	IF node_to_insert_at == None:
		RBT.root <- node 
	ELIF node.points > node_to_insert_at.points do
		node_to_insert_at.right <- node 
	ELSE do
		node_to_insert_at.right <- node

	//Ensure that the red-black property is maintained
	RBT.size <- RBT.size + 1
	FIX_INSERT(node)
```

In this implementation, the insert operation is used when a new user is created or when updating the weekly scoreboard. The process follows these steps:
	1. **Check if the tree is empty:** If the root is empty, the new node is directly set as the root 
	2. **Find appropriate position :** If the root is not empty, we traverse the tree to locate the correct parent node where the new node is added a leaf.
	3. **Determine if the node is a left or right child :** Depending on the value of the new node, it is added as either a left or right child of the parent node
But when a new node is added to the BST, this may violate the RBT properties. Hence, to fix the tree, a corrective operation called `FIX_INSERT` is applied.
##### Fix Insert Operation
```
FUNCTION FIX_INSERT(node):
	Require: A node from RBT
	
	// if both parent and node are red, it violates the 3rd rule
	WHILE node.parent.color == "red" do 
		// check if the parent node is left child
		IF node.parent == node.parent.parent.left do
			//uncle node
			rightgrandpa <- node.parent.parent.right
			
			//**** CASE 1 ****
			IF rightgrandpa.color == "red" do:
				rightgrandpa.color <- "black"
				node.parent.color <- "black" 
				node.parent.parent.color <- "red"
				node <- node.parent.parent
				
			//**** CASE 2 ****
			ELSE IF node == node.parent.right do
				node <- node.parent
				LEFT_ROTATE(node) 
				
			//**** CASE 3 ****
			ELSE do
				node.parent.color = "black"
				node.parent.parent.color = "red"
				RIGHT_ROTATE(node.parent.parent)
				
		// check if parent node is right child
		//Repeat the same process, just now on the right side
		ELSE do
			//uncle node
			leftgrandpa <- node.parent.parent.left 
			
			//**** CASE 1 ****
			IF leftgrandpa.color == "red" do
				leftgrandpa.color <- "black"
				node.parent.color <- "black"
				node.parent.parent.color <- "red"
				node <- node.parent.parent
				
			//**** CASE 2 ****
			ELIF node == node.parent.left do 
				 node <- node.parent
				 RIGHT_ROTATE(node)
				 
			//**** CASE 3 ****
			ELSE do
				node.parent.color <- "Black"
				node.parent.parent.color <- "Red"
				LEFT_ROTATE(node.parent.parent)
			
		if node == RBT.root:
			break
	
	self.root.color <- "black"
```

When inserting a new node, there are 3 cases that could happen that violate the RBT properties:
- **Case 1:** When the uncle node is red
	- Set both the uncle and parent node colors to black, and grandparents to red then move up the tree to check for any further violations in the Tree 
- **Case 2:** When the uncle node is black and the node is a right child
	- Call a left rotation on the parent 
- **Case 3:** When the uncle node is black and the node is a left child 
	- Set the parent color to black and the grandparent color to red, then perform a left rotate on the the grandparent
So the pseudocode above checks if there is any **Red-Red violation** with the node and the parent node, then checks if the parent node is a left or right node as this affects the uncle's position. Then it handles any of the 3 cases. If needed, the tree will continue to adjust upwards until the Red-Black Tree properties are fully restored.

(Add why this is log n)
##### Delete Operation
```
FUNCTION DELETE_USER(RBT,node):
	Require: RedBlackTree class that has nodes as elements
	Require: a node from user table to be deleted

	orginalcolor <- node.color 
	//**** CASE 1 ****
	IF node.left == NIL do 
		fix_node <- right 
		MOVETREE(RBT,node,node.right)
	
	//**** CASE 2 ****
	ELSE IF node.right == NIL do
		fix_node <- node.left
		MOVETREE(RBT,node,node.left)

	//**** CASE 3 ****
	ELSE do 
		// Find smallest node bigger than node
		minimum <- node.right
		WHILE minimum.left != NIL do
			minimum <- minimum.left 
		orginalColor <- minimum.color 
		temp <- minimum.right
		
		IF minimum.parent == node do 
				temp.parent <- minimum 
		ELSE do 
			MOVETREE(RBT,minimum, minimum.right)
			minimum.right <- node.right 
			minimum.right.parent <- minimum 

		MOVETREE(node,minimum)
		minimum.left <- node.left
		minimum.left.parent <- minimum 
		minimum.color <- node.color

	RBT.size <- RBT.size - 1

	if orginalColor == "black":
		FIX_DELETE(RBT,temp)
```

The delete operation removes a `node` from a Red-Black Tree while ensuring that the tree maintains its balance and Red-Black properties after the deletion. The method works by considering the different cases:
- **Case 1**: Node has no left child
		When the node has only one child, the node can be simply replaced with the right child to maintain the tree structure.
- **Case 2**: Node has no right child
		Similarly to case 1, the node is replaced by the single left child 
- **Case 3**: Node has both children
		If the node has both children, the node would be replaced by the successor(smallest node bigger than node). It starts by looking at the right child, and the `while` loop finds the smallest node in the right subtree.
		Then, we handle the case where the `minimum node` parent is the `node` to be deleted. Since the `minimum node` is the right child of the `node `that is needed to be deleted,  we would not need to adjust the parent of the right child. 
		If the `minimum node` parent is not the node to be deleted, we swap the `minimum node` with the `node` to be deleted. 
Lastly, if the colour of the deleted `node` is black, we would have fix the tree using `DELETE_FIX` to maintain the red-black properties. 

The delete operation is used in two scenarios:
1. Account Deletion:
		When a user deletes their account, the data would be removed from the database and the corresponding node must be removed from **RBT**
2.  Points Update:
		When a user gain or loses points, their position in the RBT may change. To maintain the tree structure, the existing node is removed and a new node with the updated points is inserted

##### Fix Delete Operation
```
FUNCTION FIX_DELETE(RBT,node):
	Require: RedBlackTree class that has nodes as elements
	Require: node that replaced the deleted node

	WHILE NODE != RBT.root and node.color == "black"
		// check if node is left child 
		IF node == node.parent.left
			sibling <- node.parent.right
			
			//**** CASE 1 ****
			IF sibling.color == "red" do
				sibling.color <- "black"
				node.parent.color <- "red"
				LEFT_ROTATE(node.parent)
				sibling <- node.parent.right

			//**** CASE 2 ****
			IF sibling.left.color == "black" and sibling.right.color == "black" do
				sibling.color <- "red"
				node <- node.parent
				
			//**** CASE 3 ****
			ELSE do
				//**** CASE 3a ****
				IF sibling.right.color == "black"
					sibling.left.color <- "black"
					sibling.color <- "red"
					RIGHT_ROTATE(sibling)
					sibling <- node.parent.right 

				sibling.color <- node.parent.color
				node.parent.color <- "black"
				sibling.right.color <- "black"
				LEFT_ROTATE(node.parent)
				node <- RBT.root
				
		//MIRROR (if node is right child)
		ELSE:
			sibling <- node.parent.left 
			IF sibling.color <- "red"
				sibling.color <- "black"
				node.parent.color <- "red"
				RIGHT_ROTATE(node.parent)
				sibling <- node.parent.left

			IF sibling.right.color == "black" and sibling.right.color == "black" do
				sibling.color <- "red"
				node <- node.parent

			ELSE:
				IF sibling.left.color == "black"
					sibling.right.color <- "black"
					sibling.color <- "red"
					LEFT_ROTATE(sibling)
					sibling <-node.parent.left
				sibling.color <- node.parent.color 
				node.parent.color <- "black"
				sibling.left.color <- "black"
				RIGHT_ROTATE(node.parent)
				node <- RBT.root
		
	node.color <- 0								
```

The `FIX_DELETE` function restores RBT properties after deleting a node, specifically when the node deleted was black. This is necessary as removing a black node would violate the 4th rule of the RBT , which states that every path from the root to the leaf should contain the same number of black nodes. Hence, to restore balance, a correction is need. This is done by correcting this 3 cases:
- **Case 1** :  Sibling of `node` is red
		If `sibling` is red , we rotate left around the parent of `node` to move the `sibling` upwards
- **Case 2:** Both children of `sibling` are black
		If both children of sibling are black, we recolour `sibling` to red and move problem up to the parent node (to be re-iterated again)]
- **Case 3:**
	- **Case 3a**: Sibling right child is black, but left child is red
			To prepare for the next step(balancing the tree ), perform `RIGHT ROTATION` on `sibling` to bring the red node higher. 
		Since both child of `sibling` is red, we recolour the nodes and perform `LEFT_ROTATION` 
Finally we check that the `node` colour remains black, preserving the RBT properties.

##### Update operation
There are 2 update operations for different cases:

```
FUNCTION UPDATE_RANKINGS(RBT)
	Require: RedBlackTree class of silver ,gold or platinum members that has nodes as elements
	nodelist <- INORDERTRAVERSAL(node)

	FOR node in nodelist do
		IF node.points  != node.weekly_points do 
			updatednode <- new Node(node.weekly_points)
			updatenode.userid <- node.userid 
			updatenode.tier <- node.tier
			INSERT(updatenode)
			DETELE(node)
	
```
The `UPDATE_RANKING` operation would only be used at the end of the week, where the points would be needed to be tallied to determine which user would qualify for a promotion and demotion. The `UPDATE_RANKINGS` works by traversing the tree to get all nodes, and for each node, if the value does not equal to the `weekly_points` , we remove the node and add all important values to the new node with the value of `weekly_points`

The second update operation is used for tiers of bronze, where the points not in a red-black tree but directly taken form the `User` table HashMap. This operation happens every time the user gains or lose points.
```
FUNCTION UPDATE_POINTS(node,value)
		Require: node from a user_table
		Require: an integer value
		
		node.points <- node.points + value
		//Update tier to silver
		IF node.points > 100 and node.tier == "bronze":
			node.tier <- "silver"
			RB_INSERT(RBT_silver,node.userid)
			return "You have reached silver!!"
```

Since the bronzer tier does not require sorting, we can store the bronze users in a HashMap instead. Once a user reaches 100 points, the user's `node` is inserted into the Silver RBT. 

##### Promotion and Demotion
```
FUNCTION TOP_BTM(RBT,tier)
	Require: RedBlackTree class of silver ,gold or platinum members that has nodes as elements
	Require: A string that is either "silver" , "gold" or "platinum"

	toppercent <- 0
	btmpercent <- 0
	toppercentlist <- [] //empty array or list
	btmpercentlist <- [] //empty array or list	
	
	IF tier == "silver" do
		toppercent <- ROUNDDOWN(RBT.size * 0.20) //top 20%
	ELSE IF tier == "gold" do 
		btmpercent <- ROUNDDOWN(RBT.size * 0.20) //btm 20%
		toppercent <- ROUNDDOWN(RBT.size * 0.10) //top 10%
	ELSE do  //platinum 
		btmpercent <-ROUNDDOWN(RBT.size * 0.10) //btm 10%
	
	IF toppercent != 0 do
		node <- FIND_MAX(RBT.root)
		For i = 1 to toppercent:
			toppercentlist <- toppercentlist + node 
			node <- FIND_PREDECESSOR(node)
	IF btmpercent != 0 do
		node <- FIND_MIN(RBT.root)
		For i = 1 to btmpercent:
			btmpercentlist <- btmpercentlist + node
			node <- FIND_SUCCESSOR(node)
			
	return btmpercentlist , toppercentlist
		
```
In order to determine which users are eligible for promoting or demoting, we first identify the membership tier:
<div align="center">
  <table>
    <tr>
      <th>Tier</th>
      <th>Top percentage</th>
      <th>btm percentage</th>
    </tr>
    <tr>
      <td>Silver</td>
      <td>20%</td>
      <th>NIL</th>
    </tr>
        <tr>
      <td>Gold</td>
      <td>10%</td>
      <td>20%</td>
    </tr>
        <tr>
      <td>Platinum</td>
      <th>NIL</th>
      <td>10%</td>
    </tr>
  </table>
</div>

Based on the table above, we calculate the number of users eligible for promotion and demotion. For promotion, we identify the top users by finding the node with the highest points. Then, using the predecessor function, we traverse the graph backwards to find next  with the highest points.
For demotion, we identify the bottom users by finding the node with the lowest points. Then, using the successor function, we traverse the graph forward to find the next user with the lowest points

```
FUNCTION WEEKLY_UPDATE(RBT_silver,RBT_gold,RBT_plat)
	Require: RedBlackTree class of silver members that has nodes as elements
	Require: RedBlackTree class of gold members that has nodes as elements
	Require: RedBlackTree class platinum members that has nodes as elements
	
	//promotion from silver to gold 
	placeholder , topsilverusers <- TOP_BTM(RBT_silver,"silver")
	FOR node in topsilverusers do 
		node.tier <- "gold"
		DELETE_USER(RBT_silver,node)
		RB_INSERT(RBT_gold,node)

	//demotion from gold to silver and promotion from gold to plat
	btmgoldusers , topgoldusers <- TOP_BTM(RBT_gold,"gold")
	//demotion
	FOR node in btmgoldusers do 
		node.tier <- "silver"
		DELETE_USER(RBT_gold,node)
		RB_INSERT(RBT_silver,node)
	//promotion
	FOR node in topgoldusers do 
		node.tier <- "platinum"
		DELETE_USER(RBT_gold,node)
		RB_INSERT(RBT_plat,node)

	//demotion to plat to gold 
	btmplatusers , placeholder <- TOP_BTM(RBT_plat,"platinum")
	FOR node in btmplatusers do 
		node.tier <- "gold"
		DELETE_USER(RBT_plat,node)
		RB_INSERT(RBT_gold,node)
```
The `WEEKLY_UPDATE` function performs tier promotions and demotions within the reward points table at the end of the week. For each tier , the system retrieves the top and bottom users as needed, updates the tier of the user's node, removes them from their current tier, and inserts them into the appropriate tier.

**References**
Figure 1: Using https://dbdiagram.io/home to create my own db diagram
Figure 2: https://builtin.com/data-science/b-tree-index
Figure 3: https://www.geeksforgeeks.org/introduction-to-red-black-tree/

