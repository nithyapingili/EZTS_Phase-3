'''consider two list find the total sum of two list by adding list1 and reverse of list2
list1=6 5 2 7 9 3
list2=2 4 9 6 7 4
res=[10,12,8,16,13,5]
list1=12 3 6
list2=4 13 9 7 0
res=[12,10,15,13,4] '''
#way-1:
List1 = list(map(int, input("Enter elements of List1 (space-separated): ").split()))
List2 = list(map(int, input("Enter elements of List2 (space-separated): ").split()))
List2 = List2[::-1]
res = [a + b for a, b in zip(List1, List2)]
print(res)

#way-2:
List1 = list(map(int,input().split()))
List2 = list(map(int,input().split()))
res=[]
def recSum(left,right):
  if left==len(List1) and right!=-1:
      res.extend(List2[right::-1])
      right=-1
  if left!=len(List1) and right==-1:
      res.extend(List1[left:])
      left=0
      return
  if left==len(List1) and right==-1:
      return   
  res.append(List1[left]+List2[right])
  recSum(left+1,right-1)
recSum(0,len(List2)-1)
print(res) 
-----------------------------------------------------------------------------
'''list->even indexed elements
list2->odd indexed elements
res=[10->6+4 ,8 ->2+6 ,13->9+4] res2=[25->12+13,13->6+7 ,77->None+77] 
def even_index_elements(lst):
    return [lst[i] for i in range(len(lst)) if i % 2 == 0]
def odd_index_elements(lst):
    return [lst[i] for i in range(len(lst)) if i % 2 != 0]
List1 = list(map(int, input("Enter elements of List1 (space-separated): ").split()))
List2 = list(map(int, input("Enter elements of List2 (space-separated): ").split()))
even_List1 = even_index_elements(List1)
odd_List2 = odd_index_elements(List2)
res = []
res2 = [] '''
#way-1:
def sum_even_odd(index):
    if index >= len(even_List1) or index >= len(odd_List2):
        return
    res.append(even_List1[index] + odd_List2[index])
    sum_even_odd(index + 1)
def sum_odd_elements(index):
    if index >= len(List1) and index >= len(List2):
        return
    left = List1[index] if index < len(List1) else 0
    right = List2[index] if index < len(List2) else 0
    res2.append(left + right)
    sum_odd_elements(index + 2)
sum_even_odd(0)
sum_odd_elements(1)
print("res =", res)
print("res2 =", res2) 
#way-2:
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
res=[]
def evenoddsum(i):
    if i>=len(list1) and i+1>=len(list2):
        return
    if i>=len(list1) and i+1<=lwen(list2):
        res.extend(list2[i+1::2])
        return
    if i<=len(list1) and i+1>=len(list2):
        res.extend(list1[i::2])
        return
    res.append(list1[i]+list2[i+1])
    evenoddsum(i+2)
evenoddsum(0)
print(res)
----------------------------------------------------------------
'''for the given two list.Find the result list that contains all the possible sum of even elements of first list with odd elemets of second list ''' 


#way-1: using recursion
def even_elements(lst):
    return [x for x in lst if x % 2 == 0]
def odd_elements(lst):
    return [x for x in lst if x % 2 != 0]
def compute_sums(even_lst, odd_lst, res, even_index, odd_index):
    if even_index >= len(even_lst):
        return res
    if odd_index >= len(odd_lst):
        return compute_sums(even_lst, odd_lst, res, even_index + 1, 0)
    res.append(even_lst[even_index] + odd_lst[odd_index])
    return compute_sums(even_lst, odd_lst, res, even_index, odd_index + 1)
List1 = list(map(int, input().split()))
List2 = list(map(int, input().split()))
even_List1 = even_elements(List1)
odd_List2 = odd_elements(List2)
res = compute_sums(even_List1, odd_List2, [], 0, 0)
print("res =", res)

#way-2:without using recursion
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
res=[]
i=0
while i<len(list1):
    if list1[i]%2!=0:
        i+=1
        continue
    j=0
    while j<len(list2):
        if list2[j]%2!=0:
            res.append(list1[i]+list2[j])
            j+=1
            continue
        j+=1
    i+=1
print(res)
#way-3:
def allEvenOddSum(L1,L2,i=0,j=0,result=None):
    if result == None:
        result = []
    if i >= len(L1):
        return result
    if L1[i] % 2 != 0:
        return allEvenOddSum(L1,L2,i+1,j,result)
    if j < len(L2):
        if L2[j] % 2 != 0:
            result.append(L1[i] +L2[j])
        return allEvenOddSum(L1,L2,i,j+1,result)
    else:
        return allEvenOddSum(L1,L2,i+1,0,result)
List1 = list(map(int,input().split()))
List2 = list(map(int,input().split()))
print(allEvenOddSum(List1,List2))
------------------------------------------------------------------------------------------------------
#[15,13,11,9]----->[15+13=28 ,11+9=20]---->[28,20] 
def allEvenOddSum(L1, L2, i=0, j=0, result=None):
    if result is None:
        result = []
    if i >= len(L1):
        return result
    if L1[i] % 2 != 0:
        return allEvenOddSum(L1, L2, i + 1, j, result)
    if j < len(L2):
        if L2[j] % 2 != 0:
            result.append(L1[i] + L2[j])
        return allEvenOddSum(L1, L2, i, j + 1, result)
    else:
        return allEvenOddSum(L1, L2, i + 1, 0, result)
def pairwise_sums(lst):
    result = []
    for k in range(0, len(lst), 2):
        if k + 1 < len(lst):
            result.append(lst[k] + lst[k + 1])
    return result
List1 = list(map(int, input("Enter elements of List1 (space-separated): ").split()))
List2 = list(map(int, input("Enter elements of List2 (space-separated): ").split()))
sums = allEvenOddSum(List1, List2)
final_result = pairwise_sums(sums)
print("sums =", sums)
print("final_result =", final_result)
        
-------------------------------------------------------------------------------------------------------------------
Memorization :
->top-down approach
->caches the results of function calls
->recursive implementation
->well suited for problems with a relatively small set of inputs used when the subproblems have overlapping subproblems

Tabulation:-
->bottom-up approach
->stores the results of subproblems in a table
->iterative implementation
->well suited for problems with a large set of inputs used when the subproblems do not overlap
--------------------------------------------------------------------------------------------------------
def finonacci(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    table=[0]*(n+1)
    table[0]=0
    table[1]=1
    for i in range(2,n+1):
      table[i]=table[i-1]+table[i-2]
    return table[n]
-------------------------------------------------------------------------------------------------------
'''You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps '''
def climbStairs():
    n = int(input("Enter the number of stairs: "))
    if n == 1:
        return 1
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])
climbStairs()
#way-2:
class Solution:
    def climb_stairs(self):
        n = int(input("Enter the number of stairs: "))
        if n==0 and n==1:
            return 1
        step1,step2=1,1
        for i in range(2,n+1):
            res=step1+step2
            step2=step1
            step1=res
        return res
solution = Solution()
print(solution.climb_stairs())
--------------------------------------------------------------------------------------------
'''Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1s in the binary representation of i.
Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10 '''
def countBits(n):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans
n = int(input("Enter an integer n: "))
result = countBits(n)
print("Output:", result)
#way-2:
class Solution:
    def countBits(self, n: int) -> list[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res
n = int(input("Enter an integer n: "))
solution = Solution()
result = solution.countBits(n)
print("Output:", result)
-------------------------------------------------------------------------
'''Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none)
deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of on
ly lowercase English characters.'''
def longestCommonSubsequence():
    text1 = input("Enter the first string: ")
    text2 = input("Enter the second string: ")
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp[m][n])
longestCommonSubsequence()
