### 01: Balanced Brackets
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ]. Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and (). </br>
A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ]. </br>
By this logic, we say a sequence of brackets is balanced if the following conditions are met: </br>
It contains no unmatched brackets. </br>
The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets. </br>
Given n strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO. </br>
**Input** : </br>
3 </br>
{[()]} </br>
{[(])} </br>
{{[[(())]]}} </br>
**Output** : </br>
YES </br>
NO </br>
YES </br>
**Explanation:**  </br>
The string {[()]} meets both criteria for being a balanced string, so we print YES on a new line. </br>
The string {[(])} is not balanced because the brackets enclosed by the matched pair { and } are not balanced: [(]). </br>
The string {{[[(())]]}} meets both criteria for being a balanced string, so we print YES on a new line. </br></br>

### 02: Queues: A Tale of Two Stacks
A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed. </br>
A basic queue has the following operations: </br>
Enqueue: add a new element to the end of the queue. </br>
Dequeue: remove the element from the front of the queue and return it. </br>
In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following  types: </br>
1 x: Enqueue element  into the end of the queue. </br>
2: Dequeue the element at the front of the queue. </br>
3: Print the element at the front of the queue. </br>
**Input** : </br>
10 </br>
1 42 </br>
2 </br>
1 14 </br>
3 </br>
1 28 </br>
3 </br>
1 60 </br>
1 78 </br>
2 </br>
2 </br>
**Output** : </br>
14 </br>
14 </br></br>

### 03: Largest Rectangle
Skyline Real Estate Developers is planning to demolish a number of old, unoccupied buildings and construct a shopping mall in their place. Your task is to find the largest solid area in which the mall can be constructed. </br>
There are a number of buildings in a certain two-dimensional landscape. Each building has a height, given by h[i] where I belongs to [1,n]. If you join k adjacent buildings, they will form a solid rectangle of area k x min(h[i],h[i+1],...,h[i+k-1]]. </br>
For example, the heights array h=[3,2,3]. A rectangle of height h=2 and length k=3 can be constructed within the boundaries. The area formed is h.k = 2.3 = 6. </br>
**Input** : </br>
5
1 2 3 4 5 </br>
**Output** : </br>
9 </br>
**[Explanation:](https://www.hackerrank.com/challenges/largest-rectangle/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen)** </br></br>


### 04: Castle on the Grid
You are given a square grid with some cells open (.) and some blocked (X). Your playing piece can move along any row or column until it reaches the edge of the grid or a blocked cell. Given a grid, a start and an end position, determine the number of moves it will take to get to the end position. </br>
For example, you are given a grid with sides n=3 described as follows: </br>
... </br>
.X. </br>
... </br>
Your starting position (startX, startY) = (0,0) so you start in the top left corner. The ending position is (goalX, goalY) = (1,2). The path is (0,0) -> (0,2) -> (1,2). It takes 2 moves to get to the goal. </br>
**Input** : </br>
3 </br>
.X. </br>
.X. </br>
... </br>
0 0 0 2 </br>
**Output** : </br>
3 </br></br>
