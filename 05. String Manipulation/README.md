### 01: Strings- Making Anagrams
Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not. </br>
Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number? </br>
Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings. </br>
For example, if a=cde and b=dcf, we can delete e from string a and f from string b so that both remaining strings are cd and dc which are anagrams. </br>
**Input** : </br>
cde </br>
abc </br>
**Output** : </br>
4 </br></br>

### 02: Alternating Characters
You are given a string containing characters A and B only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string. Your task is to find the minimum number of required deletions. </br>
For example, given the string s=AABAAB, remove an A at positions 0 and 3 to make s=ABAB in 2 deletions. </br>
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

### 03: Sherlock and the Valid String
Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just 1 character at   1 index in the string, and the remaining characters will occur the same number of times. Given a string s, determine if it is valid. If so, return YES, otherwise return NO.
For example, if s=abc, it is a valid string because frequencies are {a:1, b:1, c:1}. So is a=abcc because we can remove one c and have 1 of each character in the remaining string. If s=abccc however, the string is not valid as we can only remove 1 occurrence of c. That would leave character frequencies of {a:1, b:1, c:2}. </br>
**Input** : </br>
aabbcd </br>
**Output** : </br>
NO </br>
**Input** : </br>
abcdefghhgfedecba </br>
**Output** : </br>
YES </br></br>


### 04: Special String Again
A string is said to be a special string if either of two conditions is met: </br>
1. All of the characters are the same, e.g. aaa. </br>
2. All characters except the middle one are the same, e.g. aadaa. </br>

A special substring is any substring of a string which meets one of those criteria. Given a string, determine how many special substrings can be formed from it. For example, given the string s=mnonopoo, we have the following special substrings: </br>
{m, n, o, n, p, o, o, non, ono, opo, oo}. </br>
**Input** : </br>
7 </br>
abcbaba </br>
**Output** : </br>
10 </br>/br>

### 05: Common Child
A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string. Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?
For example, ABCD and ABDC have two children with maximum length 3, ABC and ABD. They can be formed by eliminating either the D or C from both strings. Note that we will not consider ABCD as a common child because we can't rearrange characters and ABCD  ABDC. </br>
**Input** : </br>
HARRY </br>
SALLY </br>
**Output** : </br>
2 </br><
**Explanation: ** The longest string that can be formed by deleting zero or more characters from HARRY and SALLY is AY, whose length is 2. </br>/br>
