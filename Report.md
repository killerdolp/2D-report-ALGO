
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
# Exclusive summary

The **Tier Membership** system consists of four tiers: **Bronze, Silver, Gold, and Platinum**. Every member starts at the Bronze tier with 0 points. To advance to Silver, a user must accumulate at least **500 points**. However, progression to **Gold** or **Platinum** is competitive and only the top users with the highest points will qualify for these tiers, based on the rankings.

The proposed database system is as followed, there would be 2 tables: a **User table** and a **Reward Point table**. The database would ensure **O(1)** time complexity whenever the user retrieves their own points. Furthermore , the **User table** would make use of database indexing to ensure the system lookups would be **O(log n)**.

The **Reward Point table** ,would be organised using a **Red and Black Tree**, which is an self balancing version of Binary Search Tree (BST). This algorithm provides efficient sorting and searching while maintaining a balanced tree structure, ensuring O(log n) time complexity for search operations. It is also slightly faster than the AVL tree (another self balancing version of BST) as it would have lesser rotations during updates.


---
# Database diagram
==Figure 1== 
<div align="center">
<img alt="center" src="Screenshot 2025-03-13 at 7.58.30 PM.png" width="400px" height="200px">
</div>

==Figure 1== shows the tables that would be used in the proposed solution. This tables would have a **one to one relationship**, where the points_id column in the User table serves as a foreign key referencing the Primary key (id) in the Reward_Points table. This ensures that whenever the user's points are needed to be displayed in his own account, it would only take **O(1)** time.

==Figure 2== 
<div align="center">
<img alt="center" src="Screenshot 2025-03-14 at 6.07.56 PM.png" width="400px" height="200px">
</div>

> [!Take note that in Figure 2, the key is used for indexing , while Index (e.g Index:15) points to the actual index in the database]

Searching for a person's username and id in the user table requires the database to check every data sequentially resulting in **O(n)** time complexity. To optimise this process, the **User** table should implement database indexing. This allows the database to jump directly to the relevant sections instead of iterating through the data. As shown in ==Figure 2==, indexing uses a structure, similar to B-tree, which ensures **O(log n)** time complexity for searching.

(maybe add actual example here)

But, **Rewards point** table should not use database indexing. This is due to the frequent changing in the table (more about why it changes so frequently would be explain in [[2D report#User Ranking System]]). Although B-tree is great from searching,  they slow down when operations like insert, update and delete happens. This operations adds overhead, as for each operation, the database would have to keep rebuilding and reorganising the data structure and possibly rebalancing the trees, slowing down the performance.

(Should i explain b-tree oso??)

---
# User Ranking System

The ranking system is design in a way to incentive user engagement and reward top-performing users. There are 4 tiers in this system. Bronze, Silver ,Gold and Platinum. The progression system is based on accumulated points and competitive ranking system. A user can gain points by getting likes and comments on their post and videos and would lose points by gaining dislikes and reports.

## Ranking Progression Rules
- **Bronze to Silver**
	- A user would be promoted to Silver upon obtaining 1000 points
	- A user would not be able to demote from Bronze to Silver.
- **Silver to Gold**
	- Users must be in the top 20% those who earned points during the week
	- Weekly rankings are only based on points accumulated **only** in that week.
- **Gold to Platinum**
	- Top 10% of those in the **gold** tier weekly points would be promoted to Platinum

#### Demotion Rules
To ensure user retainment and competitive fairness, Gold and Platinum players have to maintain their rankings.
- If a **gold** user is in the bottom 20% , the user would demoted to silver
- If a **platinum** user is in the bottom 10% , the user would demoted to gold.
A **silver** user is not able to demote to bronze. This allows the user to have a sense of accomplishment reinforcing a positive user experience. Furthermore, by preventing the demotion to bronze, it ensures motivation for those users that had a temporary decline in activity.

## Algorithm for sorting points
The algorithm used to sort points would be the **Red-Black Tree** algorithm. It is an modified version of the Binary Search Tree.It is also slightly faster than the AVL tree ,which is another modified version of BST, that we learned in class. This is due to the lesser amount of rotations when restructuring the tree, making things like insert and delete slightly faster. 
<div align="center">
<img alt="center" src="telegram-cloud-photo-size-5-6246945506316107709-y.jpg" width="420px" height="300px">
</div>
In a red-black tree:
- A node is can only be black or red
- The root and leaves are black
- If a node is red, then the children are black
- ALL paths from a node to its descendants should have the same number of black nodes






**References**
Figure 1: Using https://dbdiagram.io/home to create my own db diagram
Figure 2: https://builtin.com/data-science/b-tree-index
Figure 3: https://www.geeksforgeeks.org/introduction-to-red-black-tree/


