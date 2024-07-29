'''Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.
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
text1 and text2 consist of only lowercase English characters.'''
#way-1:
class Solution:
    def longcommonsubsequence(self, text1: str, text2: str) -> int:
        def LCS(str1, str2, n, m):
            if n == 0 or m == 0:
                return 0
            if str1[n-1] == str2[m-1]:
                return 1 + LCS(str1, str2, n-1, m-1)
            else:
                return max(LCS(str1, str2, n-1, m), LCS(str1, str2, n, m-1))
        
        return LCS(text1, text2, len(text1), len(text2))
solution = Solution()
text1 = input("Enter the first string: ")
text2 = input("Enter the second string: ")
print("Length of Longest Common Subsequence:", solution.longcommonsubsequence(text1, text2)) 

#way-2:with less time complexity
class Solution:
    def longcommonsubsequence(self, text1: str, text2: str) -> int:
        def LCS(str1, str2, n, m):
            dp = [[0] * (m + 1) for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if str1[i - 1] == str2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            return dp[n][m]
        
        return LCS(text1, text2, len(text1), len(text2))
solution = Solution()
text1 = input("Enter the first string: ")
text2 = input("Enter the second string: ")
print("Length of Longest Common Subsequence:", solution.longcommonsubsequence(text1, text2))
---------------------------------------------------------------------------------------------------------------------
'''Given an array of strings words and a string s, determine if s is an acronym of words.
The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order.
For example, "ab" can be formed from ["apple", "banana"], but it can't be formed from ["bear", "aardvark"].
Return true if s is an acronym of words, and false otherwise.
Example 1:
Input: words = ["alice","bob","charlie"], s = "abc"
Output: true
Explanation: The first character in the words "alice", "bob", and "charlie" are 'a', 'b', and 'c', respectively. Hence, s = "abc" is the acronym. 
Example 2:
Input: words = ["an","apple"], s = "a"
Output: false
Explanation: The first character in the words "an" and "apple" are 'a' and 'a', respectively. 
The acronym formed by concatenating these characters is "aa". 
Hence, s = "a" is not the acronym.
Example 3:
Input: words = ["never","gonna","give","up","on","you"], s = "ngguoy"
Output: true
Explanation: By concatenating the first character of the words in the array, we get the string "ngguoy". 
Hence, s = "ngguoy" is the acronym.
Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 10
1 <= s.length <= 100  '''

def is_acronym(words, s):
    acronym = ''.join(word[0] for word in words)
    return acronym == s
words = input().split()
s = input()
print(is_acronym(words, s))
---------------------------------------------------------------------------------------
'''Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100 '''
#way-1:
def spiralOrder():
    matrix = []
    rows = int(input())
    cols = int(input())
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)    
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    print(result)
spiralOrder()
#way-2:
class Solution:
    def spiralnumber(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []        
        m, n = len(matrix), len(matrix[0])
        seen = [[False for _ in range(n)] for _ in range(m)]
        result = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0        
        for i in range(m * n):
            result.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < m and 0 <= cc < n and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]        
        return result
def read_matrix():
    rows = int(input())
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix
solution = Solution()
matrix = read_matrix()
print("Spiral Order:", solution.spiralnumber(matrix))

---------------------------------------------------------------------------------------------------
'''Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:
Input: n = 2
Output: false
Constraints:
1 <= n <= 231 - 1 '''
def isHappy():
    n = int(input())
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        sum = 0
        while n > 0:
            digit = n % 10
            sum = sum + digit * digit
            n = n // 10
        n = sum
    return n == 1
print(isHappy())
#way-2:
class Solution:
    def ishappy(self, n: int) -> bool:
        hashset = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in hashset:
                return False
            hashset.add(n)
        return True
solution = Solution()
n = int(input())
print( solution.ishappy(n))
                    
-----------------------------------------------------------------------------------
'''Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104 '''
def merge():
    intervals = []
    n = int(input( ))    
    for i in range(n):
        start = int(input())
        end = int(input())
        intervals.append([start, end])    
    if not intervals:
        return []    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]    
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)    
    print(merged)
merge() 



