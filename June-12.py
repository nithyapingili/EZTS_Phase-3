'''Bhojon is a restaurant company and has started a new wing in a city. They have every type of cook except the meatball artist.
They had fired their last cook because the sale of meatballs in their restaurant is really great, and
they can’t afford to make meatballs again and again every time their stock gets empty.
They have arranged a hiring program, where you can apply with their meatball.
They will add the meatball in their seekh (a queue) and everytime they cut the meatball they take it and cut it on the day’s quantity
and then re-add the meatball in the seekh. You are the hiring manager there and you are going to say who is gonna be hired.
Day’s quantity means, on that very day the company sells only that kg of meatballs to every packet.
If someone has less than a day’s quantity, it will be counted as a sell.
Function Description:
Complete the function with the following parameters:
Parameters:
Name	Type	        Description
N	Integer	        How many people are participating in the hiring process.
D	Integer	        Day’s quantity, how many grams of meatball is being sold    to every packet.
Array[ ]Integer array	Array of integers, the weight of meatballs everyone came with.
Return:
The ith person whose meat is served at last.
 Constraints:
1 <= N <= 10^3
1 <= D <= 10^3
1 <= Array[i] <= 10^3
Input Format:
First line contains N.
Second line contains D.
After that N lines contain The ith person’s meatball weight.
Output Format:
The 1 based index of the man whose meatball is served at the last.
Sample Input 1:
4
2
[7 8 9 3]
Sample Output 1:
3
Explanation:
The seekh or meatball queue has [7 8 9 3] this distribution. At the first serving they will cut 2 kgs of meatball from the first meatball and
add it to the last of the seekh, so after 1st time it is:
[8 9 3 5]
Then, it is: [9 3 5 6],  [3 5 6 7], [5 6 7 1], [6 7 1 3], [7 1 3 4], [1 3 4 5], [3 4 5], [4 5 1], [5 1 2], [1 2 3], [2 3], [3], [1], [0]
So the last served meatball belongs to the 3rd person. '''
#way-1: using functions

def last_served(N, D, arr):
    from collections import deque
    queue = deque([(arr[i], i + 1) for i in range(N)])
    while len(queue) > 1:
        weight, index = queue.popleft()
        if weight > D:
            queue.append((weight - D, index))
    _, last_index = queue[0]
    return last_index
N = int(input())
D = int(input())
arr = list(map(int,input().split()))
print(last_served(N, D, arr))
#way-2: without using functions
from collections import deque
N = int(input())
D = int(input())
arr = list(map(int, input().split()))
queue = deque([(arr[i], i + 1) for i in range(N)])
while len(queue) > 1:
    weight, index = queue.popleft()
    if weight > D:
        queue.append((weight - D, index))
    _, last_index = queue[0]
print(last_index)
#way-3:
N=int(input())
D=int(input())
arr=list(map(int,input().split()))
soldqty=[(i-1)//D for i in arr]
print(soldqty.index(max(soldqty))+1)
----------------------------------------------------------------------------------------------------
'''Abhijeet is one of those students who tries to get his own money by part time jobs in various places to fill up the expenses for buying books.
He is not placed in one place, so what he does, he tries to allocate how much the book he needs will cost, and then work to earn that much money only.
He works and then buys the book respectively. Sometimes he gets more money than he needs so the money is saved for the next book.
Sometimes he doesn’t. In that time, if he has stored money from previous books, he can afford it, otherwise he needs money from his parents.
Now His parents go to work and he can’t contact them amid a day.
You are his friend, and you have to find how much money minimum he can borrow from his parents so that he can buy all the books.
He can Buy the book in any order.
Function Description:
Complete the function with the following parameters:
Name	        Type	          Description
N	        Integer	        How many Books he has to buy that day.
EarnArray[ ]	Integer array	Array of his earnings for the ith book
CostArray[ ]	Integer array	Array of the actual cost of the ith book.
Constraints:
1 <= N <= 10^3
1 <= EarnArray[i] <= 10^3
1 <=  CostArray[i] <= 10^3
Input Format:
First line contains N.
Second N lines contain The ith earning for the ith book.
After that N lines contain The cost of the ith book.
Output Format:
The minimum money he needs to cover the total expense.
Sample Input 1:
3
[3 4 2]
[5 3 4]
Sample Output 1:
3
Explanation:
At first he buys the 2nd book, which costs 3 rupees, so he saves 1 rupee. Then he buys the 1st book, that takes 2 rupees more.
So he spends his stored 1 rupee and hence he needs 1 rupee more. Then he buys the last book.'''
#way-1:using functions

def min_borrow(N, EarnArray, CostArray):
    earn = 0
    borrow = 0
    for i in range(N):
        earn += EarnArray[i]
        cost = CostArray[i]
        if earn < cost:
            borrow += cost - earn
            earn = 0
        else:
            earn -= cost
    return borrow
N = int(input())
EarnArray = list(map(int,input().split()))
CostArray = list(map(int,input().split()))
print(min_borrow(N, EarnArray, CostArray))
#way-2:without usig functions
N = int(input())
EarnArray = list(map(int, input().split()))
CostArray = list(map(int, input().split()))
earn = 0
borrow = 0
for i in range(N):
    earn += EarnArray[i]
    cost = CostArray[i]
    if earn < cost:
        borrow += cost - earn
        earn = 0
    else:
        earn -= cost
print(borrow)
#way-3:
N = int(input())
EarnArray = list(map(int,input().split()))
CostArray = list(map(int,input().split()))
costing=sum(EarnArray)-sum(CostArray)
if costing<0:
    print(abs(costing))
else:
    print("0")
----------------------------------------------------------------------------------------------------------
'''Nobel Prize-winning Austrian-Irish physicist Erwin Schrödinger developed a machine and brought as many Christopher Columbus from as many parallel universes he could.
Actually he was quite amused by the fact that Columbus tried to find India and got America. He planned to dig it further.
Though totally for research purposes, he made a grid of size n X m, and planted some people of America in a position (x,y) [in 1 based indexing of the grid],
and then planted you with some of your friends in the (n,m) position of the grid. Now he gathered all the Columbus in 1,1 positions and started a race.
Given the values for n, m, x, y, you have to tell how many different Columbus(s) together will explore you as India for the first time.
Remember, the Columbus who will reach to the people of America, will be thinking that as India and hence wont come further.
Function Description:
Complete the mark game function in the editor below. It has the following parameter(s):
Parameters:
Name	Type	       Description
n	Integer	    The number of rows in the grid.
m	Integer	    The number of columns in the grid.
x	Integer	    The American cell’s Row.
y	Integer	    The American cell’s Column.
Constraints:
1 <= n <= 10^2
1 <= m <= 10^2
1 <= x <= n
1 <= y <= m
Input Format:
The first line contains an integer, n, denoting the number of rows in the grid.
The next line contains an integer m, denoting the number of columns in the grid.
The next line contains an integer, x, denoting the American cell’s row.
The next line contains an integer, y, denoting the American cell’s column.
Sample Cases
Sample Input 1
2
2
2
1
Sample Output 1
1
Explanation
The only way possible is (1,1) ->(2,1) -> (2,2), so the answer is 1.'''
#way-1:
n = int(input())
m = int(input())
x = int(input())
y = int(input())
def mark_game(n, m, x, y):
    return max(n - x, 0) + max(m - y, 0)
print(mark_game(n, m, x, y))
#way-2:
import math
n = int(input())-1
m = int(input())-1
x = int(input())-1
y = int(input())-1
def validpath():
    total_path=math.factorial(n+m)//(math.factorial(n)*math.factorial(m))
    path_to_xy=math.factorial(x+y)//(math.factorial(x)*math.factorial(y))
    xy_to_mn=math.factorial(n-x+m-y)//(math.factorial(n-x)*math.factorial(m-y))
    return total_path-(path_to_xy*xy_to_mn)
print(validpath())
-------------------------------------------------------------------------------------------
'''You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length '''
#way-1:using functions
def canPlaceFlowers(flowerbed, n):
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            count += 1
    return count >= n
flowerbed = list(map(int, input("Enter the flowerbed: ").split()))
n = int(input("Enter the number of flowers: "))
print(canPlaceFlowers(flowerbed, n))
#way-2:without using functions
flowerbed = list(map(int, input("Enter the flowerbed: ").split()))
n = int(input("Enter the number of flowers: "))
count = 0
for i in range(len(flowerbed)):
    if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
        flowerbed[i] = 1
        count += 1
print(count >= n)
#way-3:
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        size = len(flowerbed)
        flowers = flowerbed.count(1)
        total_flower = flowers + n
        if size % 2 != 0:
            if total_flower <= size // 2 + 1:
                return True
        else:
            if total_flower <= size // 2:
                return True
        return False
flowerbed = list(map(int,input().split()))
n = int(input())
sol = Solution()
print(sol.canPlaceFlowers(flowerbed, n))
----------------------------------------------------------------------------------
'''We have n chips, where the position of the ith chip is position[i].
We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:
position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same position.
Example 1:
Input: position = [1,2,3]
Output: 1
Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.
Example 2:
Input: position = [2,2,2,3,3]
Output: 2
Explanation: We can move the two chips at position  3 to position 2. Each move has cost = 1. The total cost = 2.
Example 3:
Input: position = [1,1000000000]
Output: 1
Constraints:
1 <= position.length <= 100
1 <= position[i] <= 10^9 '''
#way-1:using functions
def minCostToMoveChips(position):
    even_count = 0
    odd_count = 0
    for pos in position:
        if pos % 2 == 0:
            even_count += 1
        else:
            odd_count += 1   
    return min(even_count, odd_count)
position = list(map(int, input("Enter the positions (space-separated): ").split()))
print("Minimum cost to move all chips to the same position:", minCostToMoveChips(position))
----------------------------------------------------------------------------------------------------
'''Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence. 
If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions,
return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array. 
Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.
Example 1:
Input: nums = [4,3,10,9,8]
Output: [10,9] 
Explanation: The subsequences [10,9] and [10,8] are minimal such that the sum of their elements is strictly greater than the sum of elements not included.
However, the subsequence [10,9] has the maximum total sum of its elements. 
Example 2:
Input: nums = [4,4,7,6,7]
Output: [7,7,6] 
Explanation: The subsequence [7,7] has the sum of its elements equal to 14 which is not strictly greater than the sum of elements not included (14 = 4 + 4 + 6).
Therefore, the subsequence [7,6,7] is the minimal satisfying the conditions. Note the subsequence has to be returned in non-increasing order.  
Constraints:
1 <= nums.length <= 500
1 <= nums[i] <= 100 '''
def maxSubsequence():
    nums = list(map(int, input("Enter the numbers (space-separated): ").split()))
    nums.sort(reverse=True)
    total_sum = sum(nums)
    subsequence_sum = 0
    subsequence = []
    for num in nums:
        subsequence_sum += num
        subsequence.append(num)
        if subsequence_sum > total_sum - subsequence_sum:
            break
    return subsequence
print(maxSubsequence())
#way-2:
class Solution:
    def minsubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        n = len(nums)
        if n == 1:
            return nums
        for i in range(1, n + 1):
            if sum(nums[:i]) > sum(nums[i:]):
                return nums[:i]
        return nums
nums = list(map(int, input("Enter the numbers (space-separated): ").split()))
sol = Solution()
print("Minimum subsequence:", sol.minsubsequence(nums))

-----------------------------------------------------------------------------------------------------
'''There are n seats and n students in a room. You are given an array seats of length n, where seats[i] is the position of the ith seat.
You are also given the array students of length n, where students[j] is the position of the jth student.
You may perform the following move any number of times:
Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1)
Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.
Note that there may be multiple seats or students in the same position at the beginning.
Example 1:
Input: seats = [3,1,5], students = [2,7,4]
Output: 4
Explanation: The students are moved as follows:
- The first student is moved from from position 2 to position 1 using 1 move.

- The second student is moved from from position 7 to position 5 using 2 moves.
- The third student is moved from from position 4 to position 3 using 1 move.
In total, 1 + 2 + 1 = 4 moves were used.'''
def minMovesToSeat(seats, students):
    seats.sort()
    students.sort()
    moves = 0
    for i in range(len(seats)):
        moves += abs(seats[i] - students[i])
    return moves
seats = list(map(int, input("Enter the seat positions (space-separated): ").split()))
students = list(map(int, input("Enter the student positions (space-separated): ").split()))
print("Minimum moves to seat all students:", minMovesToSeat(seats, students))
