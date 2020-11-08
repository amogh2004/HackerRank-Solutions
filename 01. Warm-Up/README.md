### 01: Sales by Match
Alex works at a clothing store. There is a large pile of socks that must be paired by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are. </br>
For example, there are n=7 socks with colors ar=[1,2,1,2,1,3,2].There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2. </br>
**Input** : </br>
9 </br>
10 20 20 10 10 30 50 10 20 </br>
**Output** : </br>
3 </br></br>

### 02: Counting Valleys
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly steps steps, for every step it was noted if it was an uphill,U , or a downhill, D step. Hikes always start and end at sea level, and each step up or down represents a 1 unit change in altitude. We define the following terms: </br>
1. A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level. </br>
2. A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level. </br>

Given the sequence of up and down steps during a hike, find and print the number of valleys walked through. </br>
**Input** : </br>
8 </br>
UDDDUDUU </br>
**Output** : </br>
1 </br></br>

### 03: Jumping on the Clouds
Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game. </br>
For each game, Emma will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided. For example, c=[0,1,0,0,0,1,0] indexed from 0...6. The number on each cloud is its index in the list so she must avoid the clouds at indexes 1 and 5. She could follow the following two paths: 0->2->4->6 or 0->2->3->4->6. The first path takes 3 jumps while the second takes 4. </br>
**Input** : </br>
7 </br>
0 0 1 0 0 1 0 </br>
**Output** : </br>
4 </br></br>

### 04: Repeated String
Lilah has a string, s, of lowercase English letters that she repeated infinitely many times. </br>
Given an integer, n, find and print the number of letter a's in the first n letters of Lilah's infinite string. </br>
For example, if the string s='aback' and a=10, the substring we consider is abcacabcac, the first 10 characters of her infinite string. There are 4 occurrences of a in the substring. </br>
**Input** : </br>
aba </br>
10 </br>
**Output** : </br>
7 </br></br>