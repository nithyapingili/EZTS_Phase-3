def tostring(list):
    return "".join(list)
def permutate(a,l,r):
    if l==r:
        print(tostring(a))
    else:
        for i in range(l,r):
            a[l],a[i]=a[i],a[l]
            permutate(a,l+1,r)
            a[l],a[i]=a[i],a[l]
string=input('')
n=len(string)
a=list(string)
permutate(a,0,n)
---------------------------------------------------------------------------------
#reversing a string using recursion 
def reverse_list(lst, index=0):
    if index == len(lst):
        return []
    else:
        return reverse_list(lst, index + 1) + [lst[index]]
lst = list(map(int, input("Enter a list of integers:").split()))
print("Reversed list:", reverse_list(lst))

#way-2:
def reverse(list,left,right):
    if left>=right:
        return list
    list[left],list[right]=list[right],list[left]
    return reverse(list,left+1,right-1)
numlist=list(map(int,input().split()))
n=len(numlist)
print(reverse(numlist,0,n-1))
------------------------------------------------------------------------------- 
#way-1:
from itertools import permutations
string = input("Enter a string: ")
perms = set("".join(p) for p in permutations(string))
for perm in perms:
    print(perm)

#way-2:
def toset(list):
    return set(list)
def permute(list,l,r):
    if l==r:
        print(toset(list))
    for i in range(l,r):
        list[l],list[i]=list[i],list[l]
        permute(list,l+1,r)
        list[l],list[i]=list[i],list[l]
data={1,2,3}
n=len(data)
permute(list(data),0,n)
-----------------------------------------------------------------------------------
'''Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:
Input: nums = [1]
Output: [[1]]
Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
cc '''
#way-2:
class Solution:
    def permutate(self, nums: list[int]) -> list[list[int]]:
        reslist = []
        def rec(l, r):
            if l == r:
                reslist.append(nums[:])  # Add a copy of the current permutation
            else:
                for i in range(l, r):
                    nums[l], nums[i] = nums[i], nums[l]  # Swap to create a new permutation
                    rec(l + 1, r)  # Recurse with the next position
                    nums[l], nums[i] = nums[i], nums[l]  # Swap back to restore the original list
        rec(0, len(nums))
        return reslist
nums = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
permutations = Solution().permutate(nums)
for permutation in permutations:
    print(permutation)
----------------------------------------------------------------------------------------------------
'''Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10 '''
def permuteUnique():
    nums = list(map(int, input("Enter space-separated integers: ").split()))
    nums.sort()
    perms = []
    def backtrack(first = 0):
        if first == len(nums):  
            perms.append(nums[:])
        for i in range(first, len(nums)):
            if nums[i] in nums[first:i]: # skip duplicates
                continue
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]
    backtrack()
    return perms
print(permuteUnique())
--------------------------------------------------------------------------------------
'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1
Output: ["()"]
Constraints:
1 <= n <= 8 '''
#way-1:
def generateParenthesis():
    n = int(input("Enter the number of pairs of parentheses: "))
    def backtrack(s = '', left = 0, right = 0):
        if len(s) == 2 * n:
            print(s)
            return
        if left < n:
            backtrack(s+'(', left+1, right)
        if right < left:
            backtrack(s+')', left, right+1)
    backtrack()
generateParenthesis()

------------------------------------------------------------------------------------------------------------------
'''Given a positive integer n, return the punishment number of n.
The punishment number of n is defined as the sum of the squares of all integers i such that:1 <= i <= n
The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.
 Example 1:
Input: n = 10
Output: 182
Explanation: There are exactly 3 integers i that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1.
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0.
Hence, the punishment number of 10 is 1 + 81 + 100 = 182 '''
#way-1:
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def check(s: str, i: int, x: int) -> bool:
            m = len(s)
            if i >= m:
                return x == 0
            y = 0
            for j in range(i, m):
                y = y * 10 + int(s[j])
                if y > x:
                    break
                if check(s, j + 1, x - y):
                    return True
            return False
        ans = 0
        for i in range(1, n + 1):
            x = i * i
            if check(str(x), 0, i):
                ans += x
        return ans
n = int(input("Enter a positive integer: "))
print(Solution().punishmentNumber(n))
#way-2:
class Solution:
    def punishment_number(self, n: int) -> int:
        def is_punish_no(l, total, sno, n):
            if l >= len(sno):
                return total == n
            for i in range(l + 1, len(sno) + 1):
                if is_punish_no(i, total + int(sno[l:i]), sno, n):
                    return True
            return False
        res = 0
        for i in range(1, n + 1):
            sq = i ** 2
            if is_punish_no(0, 0, str(sq), i):
                res += sq
        return res
n = int(input("Enter a positive integer: "))
print(Solution().punishment_number(n))
------------------------------------------------------------------------------------------
'''You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where
boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck.
You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
Return the maximum total number of units that can be put on the truck.
Test Cases

Example 1:
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

Example 2:
Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91
Constraints
1 <= boxTypes.length <= 1000
1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
1 <= truckSize <= 10^6 '''
#way-1:
def maximumUnits():
    n = int(input("Enter the number of box types: "))
    boxTypes = []
    for _ in range(n):
        num_boxes, units_per_box = map(int, input(f"Enter numberOfBoxes and numberOfUnitsPerBox: ").split())
        boxTypes.append((num_boxes, units_per_box))
        
    truckSize = int(input("Enter the truck size: "))
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    total_units = 0
    for num_boxes, units_per_box in boxTypes:
        if truckSize == 0:
            break
        boxes_to_take = min(num_boxes, truckSize)
        total_units += boxes_to_take * units_per_box
        truckSize -= boxes_to_take
    print(total_units)
maximumUnits()

#way-2:
class Solution:
    def max_units(self, boxtypes: list[list[int]], trucksize: int) -> int:
        boxtypes.sort(key=lambda x: x[-1], reverse=True)
        res = 0
        for num_boxes, units_per_box in boxtypes:
            if trucksize >= num_boxes:
                res += num_boxes * units_per_box
                trucksize -= num_boxes
            else:
                res += trucksize * units_per_box
                break
        return res
n = int(input("Enter the number of box types: "))
boxtypes = []
for _ in range(n):
    num_boxes, units_per_box = map(int, input("Enter numberOfBoxes and numberOfUnitsPerBox: ").split())
    boxtypes.append([num_boxes, units_per_box])
trucksize = int(input("Enter the truck size: "))
solution = Solution()
max_units = solution.max_units(boxtypes, trucksize)
print(f"Maximum units that can be loaded: {max_units}")

-------------------------------------------------------------------------------------------
'''You are given a string time in the form of  hh:mm, where some of the digits in the string are hidden (represented by ?).
The valid times are those inclusively between 00:00 and 23:59.
Return the latest valid time you can get from time by replacing the hidden digits.
Example 1:
Input: time = "2?:?0"
Output: "23:50"
Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.'''
def maximumTime(time: str) -> str:
    time = list(time)
    for i in range(5):
        if time[i] == '?':
            if i == 0:
                time[i] = '2' if time[1] != '?' and int(time[1]) < 4 else '1'
            elif i == 1:
                time[i] = '3' if time[0] == '2' else '9'
            elif i == 3:
                time[i] = '5'
            else:
                time[i] = '9'
    if int(''.join(time[:2])) > 23:
        time[0] = '1'
        time[1] = '9'
    return ''.join(time)

time = input("Enter a time in the format hh:mm: ")
print(maximumTime(time))
--------------------------------------------------------------------------------------
'''You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y).
You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi).
A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.
Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location.
If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.
The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).
Example 1:
Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
Output: 2
Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid.
Of the valid points, [2,4] and [4,4] have the smallest Manhattan distance from your current location, with a distance of 1.
[2,4] has the smallest index, so return 2.'''
def nearest_valid_point(x, y, points):
    min_distance = float('inf')
    min_index = -1
    for index, (ai, bi) in enumerate(points):
        if ai == x or bi == y:
            distance = abs(ai - x) + abs(bi - y)
            if distance < min_distance:
                min_distance = distance
                min_index = index
    return min_index
x = int(input())
y = int(input())
points = list(map(int,input().split()))
print(nearest_valid_point(x, y, points))  # Output: 2



