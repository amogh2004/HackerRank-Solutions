### 01: Max Array Sum
Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset. </br>
For example, given an array arr=[-1,1,3,-4,5] we have the following possible subsets: </br>
Subset      Sum </br>
[-2, 3, 5]   6 </br>
[-2, 3]      1 </br>
[-2, -4]    -6 </br>
[-2, 5]      3 </br>
[1, -4]     -3 </br>
[1, 5]       6 </br>
[3, 5]       8 </br>
Our maximum subset sum is 8.
**Input** : </br>
5 </br>
3 7 4 6 5 </br>
**Output** : </br>
13 </br>
**Explanation: ** Our possible subsets are [3,4,5],[3,4],[3,6],[3,5],[7,6],[7,5] and [4,5]. The largest subset sum is 13 from subset [7,6]. </br></br>

### 02: Abbreviation
You can perform the following operations on the string, a: </br>
Capitalize zero or more of a's lowercase letters. </br>
Delete all of the remaining lowercase letters in a. </br>
Given two strings, a and b, determine if it's possible to make a equal to b as described. If so, print YES on a new line. Otherwise, print NO. </br>
For example, given a=AbcDE and b=ABDE, in a we can convert b and delete c to match b. If a=AbcDE and b=AFDE, matching is not possible because letters may only be capitalized or discarded, not changed. </br>
**Input** : </br>
1 </br>
daBcd </br>
ABC </br>
**Output** : </br>
YES </br></br>

### 03: Candies
Alice is a kindergarten teacher. She wants to give some candies to the children in her class.  All the children sit in a line and each of them has a rating score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must get more candies. Alice wants to minimize the total number of candies she must buy.
For example, assume her students' ratings are [4, 6, 4, 5, 6, 2]. She gives the students candy in the following minimal amounts: [1, 2, 1, 2, 3, 1]. She must buy a minimum of 10 candies.
Complete the candies function. It must return the minimum number of candies Alice must buy.
candies has the following parameter(s):
n: an integer, the number of children in the class
arr: an array of integers representing the ratings of each student </br>
**Input** : </br>
3
1
2
2 </br>
**Output** : </br>
4 </br>
**Explanation: ** Here 1, 2, 2 is the rating. Note that when two children have equal rating, they are allowed to have different number of candies. Hence optimal distribution will be 1, 2, 1. </br></br>

### 04: Decibinary Numbers
[Click here for problem statement.](https://www.hackerrank.com/challenges/decibinary-numbers/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming). </br>
**Input** : </br>
5
1
2
3
4
10 </br>
**Output** : </br>
0
1
2
10
100 </br>
**Explanation: ** For each x, we print the xth decibinary number on a new line. See the figure in the problem statement. </br></br>