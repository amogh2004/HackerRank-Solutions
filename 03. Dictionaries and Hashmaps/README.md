### 01: Hash Tables- Ransom Note
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs. </br>
Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No. </br>
For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". The magazine has all the right words, but there's a case mismatch. The answer is No. </br>
**Input** : </br>
6 4 </br>
give me one grand today night </br>
give one grand today </br>
**Output** : </br>
Yes </br>
**Explanation:** 'two' only occurs once in the magazine. </br></br>

### 02: Two Strings
Given two strings, determine if they share a common substring. A substring may be as small as one character. For example, the words "a", "and", "art" share the common substring a. The words "be" and "cat" do not share a substring. </br>
**Input** : </br>
2 </br>
hello </br>
world </br>
hi </br>
world </br>
**Output** : </br>
YES </br>
NO </br></br>

### 03: Sherlock and Anagrams
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other. </br>
For example s=mom, the list of all anagrammatic pairs is [m,m], [mo,om] at positions [[0],[2]],[[0,1],[1,2]] respectively. For each query, return the number of unordered anagrammatic pairs. </br>
**Input** : </br>
2 </br>
abba </br>
abcd </br>
**Output** : </br>
4 </br>
0 </br></br>

### 04: Count Triplets
You are given an array and you need to find number of tripets of indices (i,j,k) such that the elements at those indices are in geometric progression for a given common ratio r and i<j<k. </br>
For example, arr=[1,4,16,64]. If r=4, we have [1,4,16] and [4,16,64] at indices (0,1,2) and (1,2,3). </br>
**Input** : </br>
4 2 </br>
1 2 2 4 </br>
**Output** : </br>
2 </br>
**Explanation:** There are 2 triplets in satisfying our criteria, whose indices are (0,1,3) and (0,2,3). </br></br>

### 05: Frequency Queries
You are given q queries. Each query is of the form two integers described below: </br>
- 1x : Insert x in your data structure. </br>
- 2y : Delete one occurence of y from your data structure, if present. </br>
- 3z : Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0. </br>

The queries are given in the form of a 2-D array queries of size q where queries[I][0] contains the operation, and queries[I][1] contains the data element. For example, you are given array queries=[(1,1),(2,2),(3,2),(1,1),(1,1),(2,1),(3,2)]. The results of each operation are: </br>
Operation   Array   Output </br>
(1,1)       [1] 		    </br>
(2,2)       [1]		    </br>
(3,2)                   0  </br>
(1,1)       [1,1]		    </br>
(1,1)       [1,1,1]        </br>
(2,1)       [1,1]          </br>
(3,2)                   1  </br>
Return an array with the output: [0,1]. </br>
**Input** : </br>
8 </br>
1 5 </br>
1 6 </br>
3 2 </br>
1 10 </br>
1 10 </br>
1 6 </br>
2 5 </br>
3 2 </br>
**Output** : </br>
0 </br>
1 </br>
**Explanation:** For the first query of type 3, there is no integer whose frequency is 2 (array=[5,6]). So answer is 0. </br>
For the second query of type 3, there are two integers in array=[6,10,10,6] whose frequency is 2 (integers = 6 and 10). So, the answer is 1. </br></br>
