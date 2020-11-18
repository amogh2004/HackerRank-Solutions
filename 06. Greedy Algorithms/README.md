### 01: Minimum Absolute Difference in an Array
Consider an array of integers, arr=[arr[0], arr[1],...,arr[n-1]]. We define the absolute difference between two elements, a[i] and a[j] (where i≠j), to be the absolute value of a[i]-a[j]. </br>
Given an array of integers, find and print the minimum absolute difference between any two elements in the array. For example, given the array arr=[-2,2,4] we can create 3 pairs of numbers: [-2,2], [-2,4] and [2,4]. The absolute differences for these pairs are |(-2)-2|=4, |(-2)-4|=6 and |2-4|=2. The minimum absolute difference is 2. </br>
**Input** : </br>
10 </br>
-59 -36 -13 1 -53 -92 -2 -96 -54 75 </br>
**Output** : </br>
1 </br>
**Explanation:** The smallest absolute difference is |-54-(-53|=1. </br></br>

### 02: Luck Balance
Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests. Initially, her luck balance is 0. She believes in "saving luck", and wants to check her theory. Each contest is described by two integers, L[i] and T[i]: </br>
L[i] is the amount of luck associated with a contest. If Lena wins the contest, her luck balance will decrease by L[i]; if she loses it, her luck balance will increase by L[i]. </br>
T[i] denotes the contest's importance rating. It's equal to 1 if the contest is important, and it's equal to 0 if it's unimportant. </br>
If Lena loses no more than k important contests, what is the maximum amount of luck she can have after competing in all the preliminary contests? This value may be negative. </br>
For example,  and: </br>
Contest		L[i]	T[i] </br>
1		5	1 </br>
2		1	1 </br>
3		4	0 </br>
If Lena loses all of the contests, her will be 5+1+4=10. Since she is allowed to lose 2 important contests, and there are only 2 important contests. She can lose all three contests to maximize her luck at 10. If k=1, she has to win at least 1 of the 2 important contests. She would choose to win the lowest value important contest worth . Her final luck will be 5-1+4=8. </br>
**Input** : </br>
5 </br>
AAAA </br>
BBBBB </br>
ABABABAB </br>
BABABA </br>
AAABBB </br>
**Output** : </br>
3 </br>
4 </br>
0 </br>
0 </br>
4 </br></br>

### 03: Greedy Florist
A group of friends want to buy a bouquet of flowers. The florist wants to maximize his number of new customers and the money he makes. To do this, he decides he'll multiply the price of each flower by the number of that customer's previously purchased flowers plus 1. The first flower will be original price, (0+1)original price, the next will be (1+1)original price and so on.
Given the size of the group of friends, the number of flowers they want to purchase and the original prices of the flowers, determine the minimum cost to purchase all of the flowers.
For example, if there are k=3 friends that want to buy n=4 flowers that cost c=[1,2,3,4] each will buy one of the flowers priced [2,3,4] at the original price. Having each purchased x=1 flower, the first flower in the list, c[0], will now cost (current purchase+previous purchases)xc[0]=(1+1)x1=2. The total cost will be 2+3+4+2=11. </br>
**Input** : </br>
3 2
2 5 6 </br>
**Output** : </br>
15 </br></br>


### 04: Max Min
You will be given a list of integers, arr, and a single integer k. You must create an array of length k from elements of arr such that its unfairness is minimized. Call that array subarr. Unfairness of an array is calculated as max(subarr)-min(subarr). Where: </br>
- max denotes the largest integer in subarr </br>
- min denotes the smallest integer in subarr </br>
As an example, consider the array [1,4,7,2] with a k of 2. Pick any two elements, test subarr=[4,7]. </br>
Unfairness = max(4,7) - min(4,7) = 7-4 = 3 </br>
Testing for all pairs, the solution [1,2] provides the minimum unfairness. </br>
Note: Integers in arr may not be unique. </br>
**Input** : </br>
7 </br>
3 </br>
10 </br>
100 </br>
300 </br>
200 </br>
1000 </br>
20 </br>
30 </br>
**Output** : </br>
20 </br>
**Explanation: ** Here, k=3; selecting the 3 integers 10,20,30, unfairness equals: max(10,20,30) - min(10,20,30) = 30 - 10 = 20 </br></br>

### 05: Reverse Shuffle Merge
Given a string, A, we define some operations on the string as follows: </br>
a. reverse(A) denotes the string obtained by reversing string A. Example: reverse("abc")="cba" </br>
b. shuffle(A) denotes any string that's a permutation of string A. Example: shuffle("god") = ['god','gdo','ogd','odg','dgo','dog'] </br>
c. merge(A1,A2) denotes any string that's obtained by interspersing the two strings A1 & A2, maintaining the order of characters in both. For example, A1="abc" & A2="def", one possible result of merge(A1,A2) could be "abcdef", another could be "abdecf", another could be "adbecf" and so on. </br>
Given a string s such that s=merge(reverse(A), shuffle(A)) for some string A, find the lexicographically smallest A. </br>
For example, s=abab. We can split it into two strings of ab. The reverse is ba and we need to find a string to shuffle in to get abab. The middle two characters match our reverse string, leaving the a and b at the ends. Our shuffle string needs to be ab. Lexicographically ab<ba, so our answer is ab. </br>
**Input** : </br>
abcdefgabcdefg </br>
**Output** : </br>
agfedcb </br></br>
