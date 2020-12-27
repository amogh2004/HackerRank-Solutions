### 01: 2D Array - DS
Given a 6x6 2D Array, arr: </br>
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0 </br>
An hourglass in A is a subset of values with indices falling in this pattern in arr's graphical representation: </br>
a b c </br>
  d   </br>
e f g </br>

There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in are, then print the maximum hourglass sum. The array will always be 6x6. </br>
**Input** : </br>
1 1 1 0 0 0 </br>
0 1 0 0 0 0 </br>
1 1 1 0 0 0 </br>
0 0 2 4 4 0 </br>
0 0 0 2 0 0 </br>
0 0 1 2 4 0 </br>
**Output** : </br>
19 </br>
**The hourglass with the maximum sum(19) is:** </br>
2 4 4 </br>
  2   </br>
1 2 4 </br>

### 02: Left Rotation
A left rotation operation on an array shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2]. </br>
Given an array a of n integers and a number, d, perform d left rotations on the array. Return the updated array to be printed as a single line of space-separated integers. </br>
**Input** : </br>
5 4 </br>
1 2 3 4 5 </br>
**Output** : </br>
5 1 2 3 4 </br></br>

### 03: New Year Chaos
It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by 1 from 1 at the front of the line to n at the back. Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if n=8 and Person 5 bribes Person 4, the queue will look like this: 1,2,3,5,4,6,7,8. </br>
Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state! </br>
**Input** : </br>
2 </br>
5 </br>
2 1 5 3 4 </br>
5 </br>
2 5 1 3 4 </br>
**Output** : </br>
3 </br>
Too chaotic </br></br>

### 04: Minimum Swaps 2
You are given an unordered array consisting of consecutive integers [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order. </br>
For example, given the array arr=[7,1,3,2,4,5,6] we perform the following steps: </br>
i   arr                     swap (indices) </br>
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3) </br>
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1) </br>
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4) </br>
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5) </br>
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6) </br>
5   [1, 2, 3, 4, 5, 6, 7] </br>
It took 5 swaps to sort the array. </br>
**Input** : </br>
4 </br>
4 3 1 2 </br>
**Output** : </br>
3 </br></br>

### 05: Array Manipulation
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array. </br>
Example: n=10, queries = [[1,5,3],[4,8,7],[6,9,1]] </br>
Queries are interpreted as follows: </br>
a b k </br>
1 5 3 </br>
4 8 7 </br>
6 9 1 </br>
Add the values of k between the indices a and b inclusive: </br>
index-> 1 2 3 4 5 6 7 8 9 10 </br>
	  [0,0,0,0,0,0,0,0,0,0] </br>
	  [3,3,3,3,3,0,0,0,0,0] </br>
	  [3,3,3,10,10,7,7,7,0,0] </br>
	  [3,3,3,10,10,8,8,8,1,0] </br>
The largest value is 10 after all operations are performed. </br>
**Input** : </br>
5 3 </br>
1 2 100 </br>
2 5 100 </br>
3 4 100 </br>
**Output** : </br>
200 </br></br>
