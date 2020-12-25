### 01: Recursion- Fibonacci Numbers
The Fibonacci Sequence appears in nature all around us, in the arrangement of seeds in a sunflower and the spiral of a nautilus, for example. Return the nth element in the Fibonacci sequence. </br>
**Input** : </br>
3  </br>
**Output** : </br>
2  </br></br>

### 02: Recursion- Davis' Staircase
Davis has a number of staircases in his house and he likes to climb each staircase 1, 2, or 3 steps at a time. Being a very precocious child, he wonders how many ways there are to reach the top of the staircase. </br>
Given the respective heights for each of the s staircases in his house, find and print the number of ways he can climb each staircase, module 10^10+7 on a new line. </br>
For example, there is s=1 staircase in the house that is n=5 steps high. Davis can step on the following sequences of steps: </br>
1 1 1 1 1 </br>
1 1 1 2 </br>
1 1 2 1 </br>
1 2 1 1 </br>
2 1 1 1 </br>
1 2 2 </br>
2 2 1 </br>
2 1 2 </br>
1 1 3 </br>
1 3 1 </br>
3 1 1 </br>
2 3 </br>
3 2 </br>
There are 13 possible ways he can take these 5 steps. </br>
**Input** : </br>
3 </br>
1 </br>
3 </br>
7 </br>
**Output** : </br>
1 </br>
4 </br>
44 </br></br>

### 03: Crossword Puzzle
A 10x10 Crossword grid is provided to you, along with a set of words (or names of places) which need to be filled into the grid. Cells are marked either + or -. Cells marked with a - are to be filled with the word list. </br>
The following shows an example crossword from the input crossword grid and the list of words to fit, words=[POLAND, LHAASA, SPAIN, INDIA]: </br>
Input 	   	Output </br>
++++++++++ 		++++++++++ </br>
+------+++ 		+POLAND+++ </br>
+++-++++++ 		+++H++++++ </br>
+++-++++++ 		+++A++++++ </br>
+++-----++ 		+++SPAIN++ </br>
+++-++-+++ 		+++A++N+++ </br>
++++++-+++ 		++++++D+++ </br>
++++++-+++ 		++++++I+++ </br>
++++++-+++ 		++++++A+++ </br>
++++++++++ 		++++++++++ </br>
POLAND;LHASA;SPAIN;INDIA </br>
**Input** : </br>
+-++++++++ </br>
+-++++++++ </br>
+-++++++++ </br>
+-----++++ </br>
+-+++-++++ </br>
+-+++-++++ </br>
+++++-++++ </br>
++------++ </br>
+++++-++++ </br>
+++++-++++ </br>
LONDON;DELHI;ICELAND;ANKARA </br>
**Output** : </br>
+L++++++++ </br>
+O++++++++ </br>
+N++++++++ </br>
+DELHI++++ </br>
+O+++C++++ </br>
+N+++E++++ </br>
+++++L++++ </br>
++ANKARA++ </br>
+++++N++++ </br>
+++++D++++ </br></br>

### 04: Recursive Digit Sum
We define super digit of an integer x using the following rules: </br>
1. Given an integer, we need to find the super digit of the integer. </br>
2. If x has only 1 digit, then its super digit is x. </br>
3. Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x. </br>

For example, the super digit of 9875 will be calculated as: </br>
	super_digit(9875)   	9+8+7+5 = 29 </br>
	super_digit(29) 		2 + 9 = 11 </br>
	super_digit(11)		1 + 1 = 2 </br>
	super_digit(2)		= 2 </br>
You are given two numbers n and k. The number p is created by concatenating the string n k times. Continuing the above example where n=9875, assume your value k=4. Your initial p = 9875 9875 9875 9875 (spaces added for clarity). </br>
    superDigit(p) = superDigit(9875987598759875) </br>
                  5+7+8+9+5+7+8+9+5+7+8+9+5+7+8+9 = 116 </br>
    superDigit(p) = superDigit(116) </br>
                  1+1+6 = 8 </br>
    superDigit(p) = superDigit(8) </br>
All of the digits of p sum to 116. The digits of 116 sum to 8. 8 is only one digit, so it's the super digit. </br>
**Input** : </br>
aba </br>
10 </br>
**Output** : </br>
7 </br></br>
