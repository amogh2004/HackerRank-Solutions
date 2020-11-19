### 01: Hash Tables- Ice Cream Parlor
Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money to buy ice cream. On any given day, the parlor offers a line of flavors. Each flavor has a cost associated with it. </br>
Given the value of money and the cost of each flavor for t trips to the Ice Cream Parlor, help Sunny and Johnny choose two distinct flavors such that they spend their entire pool of money during each visit. ID numbers are the 1- based index number associated with a cost. For each trip to the parlor, print the ID numbers for the two types of ice cream that Sunny and Johnny purchase as two space-separated integers on a new line. You must print the smaller ID first and the larger ID second. </br>
For example, there are n=5 flavors having cost=[2,1,3,5,6]. Together they have money=5 to spend. They would purchase flavor ID's 1 and 3 for a cost of 2+3=5. Use 1 based indexing for your response. </br>
Note: </br>
- Two ice creams having unique IDs i and j may have the same cost (i.e., cost[i]=cost[j]). </br>
- There will always be a unique solution. </br>
**Input** : </br>
2 </br>
4 </br>
5 </br>
1 4 5 3 2 </br>
4 </br>
4 </br>
2 2 4 3 </br>
**Output** : </br>
1 4 </br>
1 2 </br>
**Explanation:** 
Sunny and Johnny make the following two trips to the parlor: </br>
The first time, they pool together money=4 dollars. There are five flavors available that day and flavors 1 and 4 have a total cost of 1+3=4. </br>
The second time, they pool together money=4 dollars. There are four flavors available that day and flavors 1 and 2 have a total cost of 2+2=4. </br></br>

### 02: Swap Nodes [Algo]
A binary tree is a tree which is characterized by one of the following properties: </br>
It can be empty (null). </br>
It contains a root node only. </br>
It contains a root node with a left subtree, a right subtree, or both. These subtrees are also binary trees. </br>
In-order traversal is performed as </br>
Traverse the left subtree. </br>
Visit root. </br>
Traverse the right subtree. </br>
For this in-order traversal, start from the left child of the root node and keep exploring the left subtree until you reach a leaf. When you reach a leaf, back up to its parent, check for a right child and visit it if there is one. If there is not a child, you've explored its left and right subtrees fully. If there is a right child, traverse its left subtree then its right in the same manner. Keep doing this until you have traversed the entire tree. You will only store the values of a node as you visit when one of the following is true: </br>
it is the first node visited, the first time visited </br>
it is a leaf, should only be visited once </br>
all of its subtrees have been explored, should only be visited once while this is true </br>
it is the root of the tree, the first time visited </br>
Swapping: Swapping subtrees of a node means that if initially node has left subtree L and right subtree R, then after swapping, the left subtree will be R and the right subtree, L. </br>
For example, in the following tree, we swap children of node 1. </br>
                                Depth </br>
    1               1            [1] </br>
   / \             / \ </br>
  2   3     ->    3   2          [2] </br>
   \   \           \   \ </br>
    4   5           5   4        [3] </br>
In-order traversal of left tree is 2 4 1 3 5 and of right tree is 3 5 1 2 4. </br>
Swap operation: </br>
We define depth of a node as follows: </br>
The root node is at depth 1. </br>
If the depth of the parent node is d, then the depth of current node will be d+1. </br>
Given a tree and an integer, k, in one operation, we need to swap the subtrees of all the nodes at each depth h, where h ∈ [k, 2k, 3k,...]. In other words, if h is a multiple of k, swap the left and right subtrees of that level. </br>
You are given a tree of n nodes where nodes are indexed from [1..n] and it is rooted at 1. You have to perform t swap operations on it, and after each swap operation print the in-order traversal of the current state of the tree. </br>
**Input** : </br>
3 </br>
2 3 </br>
-1 -1 </br>
-1 -1 </br>
2 </br>
1 </br>
1 </br>
**Output** : </br>
3 1 2 </br>
2 1 3 </br></br>

### 03: Pairs
You will be given an array of integers and a target value. Determine the number of pairs of array elements that have a difference equal to a target value. </br>
For example, given an array of [1, 2, 3, 4] and a target value of 1, we have three values meeting the condition: 2-1=1, 3-2=1, and 4-3=1. </br>
**Input** : </br>
5 2 </br>
1 5 3 4 2 </br>
**Output** : </br>
3 </br>
**Explanation:** There are 3 pairs of integers in the set with a difference of 2: [5,3], [4,2] and [3,1]. </br></br>


### 04: Triple sum
Given 3 arrays a,b,c of different sizes, find the number of distinct triplets (p,q,r) where p is an element of a, written as p belongs to a, q belongs to b, and r belongs to c, satisfying the criteria: p ≤ q and q ≥ r. </br>
For example, given a=[3,5,7], b=[3,6] and c=[4,6,9], we find four distinct triplets: (3,6,4),(3,6,6),(5,6,4),(5,6,6). </br>
**Input** : </br>
3 2 3 </br>
1 3 5 </br>
2 3 </br>
1 2 3 </br>
**Output** : </br>
8 </br>
**Explanation: ** The special triplets are (1,2,1),(1,2,2),(1,3,1),(1,3,2),(1,3,3),(3,3,1),(3,3,2),(3,3,3). </br></br>

### 05: Minimum Time Required
You are planning production for an order. You have a number of machines that each have a fixed number of days to produce an item. Given that all the machines operate simultaneously, determine the minimum number of days to produce the required order. </br>
For example, you have to produce goal=10 items. You have three machines that take machines=[2,3,2] days to produce an item. The following is a schedule of items produced: </br>
Day Production  Count </br>
2   2               2 </br>
3   1               3 </br>
4   2               5 </br>
6   3               8 </br>
8   2              10 </br>
It takes 8 days to produce 10 items using these machines. </br>
**Input** : </br>
3 10 </br>
1 3 4 </br>
**Output** : </br>
7 </br></br>
