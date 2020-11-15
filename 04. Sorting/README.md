### 01: Sorting-Bubble Sort
Consider the following version of Bubble Sort: </br>
for (int i = 0; i < n; i++) { </br>   
    for (int j = 0; j < n - 1; j++) { </br>
        // Swap adjacent elements if they are in decreasing order </br>
        if (a[j] > a[j + 1]) { </br>
            swap(a[j], a[j + 1]); </br>
        } </br>
    } </br>  
} </br>
Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines: </br>
Array is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place. </br>
First Element: firstElement, where firstElement is the first element in the sorted array. </br>
Last Element: lastElement, where lastElement is the last element in the sorted array. </br>
Hint: To complete this challenge, you must add a variable that keeps a running tally of all swaps that occur during execution. </br>
For example, given a worst-case but small array to sort: a=[6,4,1] we go through the following steps: </br>
swap    a </br>      
0       [6,4,1] </br>
1       [4,6,1] </br>
2       [4,1,6] </br>
3       [1,4,6] </br>
It took 3 swaps to sort the array. Output would be: </br>
Array is sorted in 3 swaps. </br>  
First Element: 1 </br>
Last Element: 6 </br>
**Input** : </br>
3 </br>
3 2 1 </br>
**Output** : </br>
Array is sorted in 3 swaps. </br>
First Element: 1 </br>
Last Element: 3 </br>

### 02: Mark and Toys
Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money. </br>
Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy? For example, if prices=[1,2,3,4] and Mark has k=7 to spend, he can buy items [1,2,3] for 6, or [3,4] for 7 units of currency. He would choose the first group of  items. </br>
**Input** : </br>
7 50 </br>
1 12 5 111 200 1000 10 </br>
**Output** : </br>
4 </br></br>

### 03: Sorting-Comparator
Comparators are used to compare two objects. In this challenge, you'll create a comparator and use it to sort an array. The Player class is provided in the editor below. It has two fields: </br>
1. name: a string. </br>
2. score: an integer. </br>
Given an array of n Player objects, write a comparator that sorts them in order of decreasing score. If 2 or more players have the same score, sort those players alphabetically ascending by name. To do this, you must create a Checker class that implements the Comparator interface, then write an int compare(Player a, Player b) method implementing the Comparator.compare(T o1, T o2) method. In short, when sorting in ascending order, a comparator function returns -1 if a<b, 0 if a=b, and 1 if a>b. </br>
For example, given n=3 Player objects with Player.name, Player.score values of Data = [[Smith,20], [Jones,15], [Jones,20]], we want to sort the list as Data-Sorted = [[Jones,20], [Smith,20], [Jones,15]]. </br>
**Input** : </br>
5 </br>
amy 100 </br>
david 100 </br>
heraldo 50 </br>
aakansha 75 </br>
aleksa 150 </br>
**Output** : </br>
aleksa 150 </br>
amy 100 </br>
david 100 </br>
aakansha 75 </br>
heraldo 50 </br>
**Explanation:** As you can see, the players are first sorted by decreasing score and then sorted alphabetically by name. </br></br>

### 04: Fraudulent Activity Notifications
HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to 2x the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data. </br>
Given the number of trailing days d and a client's total daily expenditures for a period of n days, find and print the number of times the client will receive a notification over all n days. </br>
For example, d=3 and expenditures=[10,20,30,40,50]. On the first three days, they just collect spending data. At day 4, we have trailing expenditures of [10,20,30]. The median is 20 and the day's expenditure is 40. Because 40>=2x20, there will be a notice. The next day, our trailing expenditures are [20,30,40] and the expenditures are 50. This is less than 2x30 so no notice will be sent. Over the period, there was one notice sent. </br>
**Note:** The median of a list of numbers can be found by arranging all the numbers from smallest to greatest. If there is an odd number of numbers, the middle one is picked. If there is an even number of numbers, median is then defined to be the average of the two middle values. </br>
**Input** : </br>
9 5 </br>
2 3 4 2 3 6 8 4 5 </br>
**Output** : </br>
2 </br>

### 05: Merge Sort- Counting Inversions
In an array, are, the elements at indices i and j (where i<j) form an inversion if arr[i]>arr[j]. In other words, inverted elements arr[i] and arr[j] are considered to be "out of order". To correct an inversion, we can swap adjacent elements. </br>
For example, consider the dataset arr=[2,4,1]. It has two inversions:(4,1) and (2,1). To sort the array, we must perform the following two swaps to correct the inversions. </br>
Given d datasets, print the number of inversions that must be swapped to sort each dataset on a new line. </br>
**Input** : </br>
2 </br>
5 </br> 
1 1 1 2 2 </br> 
5 </br>
2 1 3 1 2 </br>
**Output** : </br>
0 </br>
4 </br>
