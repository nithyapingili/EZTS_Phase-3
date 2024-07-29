numList=[1,2,3,4,5,0]
for i in numList:
    numList.remove(i)
print(numList)
-----------------------------------------------
for i in range(6):
    print(i)
    i+=2
-----------------------------------------------------------------------
'''Given an array prices[] of length N, representing the prices of the stocks on different days, the task is to find the maximum profit possible by buying and
selling the stocks on different days when at most one transaction is allowed.
Note: Stock must be bought before being sold.

Examples:
Input: prices[] = {7, 1, 5, 3, 6, 4}
Output: 5
Explanation:
The lowest price of the stock is on the 2nd day, i.e. price = 1. Starting from the 2nd day, the highest price of the stock is witnessed on the 5th day, i.e. price = 6. 
Therefore, maximum possible profit = 6 – 1 = 5. 

Input: prices[] = {7, 6, 4, 3, 1} 
Output: 0
Explanation: Since the array is in decreasing order, no possible way exists to solve the problem.'''
def maxProfit(prices, n):
    buy = prices[0] #2. initializes the minimum buy price with the first element of the list.
    max_profit = 0
    for i in range(1, n):
        if (buy > prices[i]): #checking for lower buy value
            buy = prices[i]
        elif (prices[i] - buy > max_profit): #checking for higher buy value
            max_profit = prices[i] - buy
    return max_profit
if __name__ == '__main__':

    prices = list(map(int,input().split()))
    n = len(prices)
    max_profit = maxProfit(prices, n)
    print(max_profit)
-----------------------------------------------------------------------------------
#sum of all the elements in array using recursion 
list=list(map(int,input().split()))
def total(i):
    if i>=len(list):
        return 0
    return list[i]+total(i+1)
print(total(0))

--------------------------------------------------------------------------------------
#whether a number is palindrome or not using recursion
IN:1221     OUT:True
IN:12210    OUT:False
def rev(n, temp):  
	if (n == 0): 
		return temp
	temp = (temp * 10) + (n % 10)
	return rev(n // 10, temp) 
n =int(input())
temp = rev(n, 0); 
if (temp == n):
    print("yes")
else:
    print("no")
#display the largest palindrome from the given number
IN:120021   OUT:120021
IN:12210    OUT:1221 
#way-1:
def largest_palindrome(n):
    num_str = str(n)
    for i in range(len(num_str), 0, -1):
        for substr in (num_str[j:i] for j in range(len(num_str) - i + 1)):
            if substr == substr[::-1]:
                
                return int(substr)
    return None
n=int(input())
print(largest_palindrome(n)) 
#way-2:
data=input()
def isPalindrome(s):
    return s == s[::-1]
def largestPal():
    maxlen=0
    larPal=''
    for i in range(len(data)):
        for j in range(i+1,len(data)+1):
            substr=data[i:j]
            if isPalindrome(substr):
                if len(substr)>maxlen:
                    maxlen=len(substr)
                    larPal=substr
    return larPal
print(largestPal())
-----------------------------------------------------------------------------------------
Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.
Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
def numIdenticalPairs():
    nums = input("Enter the numbers separated by space: ").split()
    nums = [int(num) for num in nums]
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    good_pairs = 0
    for freq in count.values():
        good_pairs += freq * (freq - 1) // 2
    print("Number of good pairs:", good_pairs)
numIdenticalPairs()
-------------------------------------------------------------------------------------------
#prime number or not using recursion
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for deno in range(2, int(num**0.5) + 1):
        if num % deno == 0:
            return False
    return True
num = int(input("Enter a number: "))
print("Prime" if is_prime(num) else "Not Prime")
-----------------------------------------------------------------------------------
 #check whether a number can be  expressed as sum of two prime numbers using recursion
#way-1:
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for deno in range(2, int(n**0.5) + 1):
        if n % deno == 0:
            return False
    return True
def find_prime_sum(n, i=2):
    if i >= n:
        return None
    if is_prime(i) and is_prime(n - i):
        return (i, n - i)
    return find_prime_sum(n, i + 1)
num = int(input("Enter a number: "))
result = find_prime_sum(num)
if result:
    print(f"{num} can be expressed as the sum of two prime numbers: {result[0]} and {result[1]}")
else:
    print(f"{num} cannot be expressed as the sum of two prime numbers") 
#way-2:
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input())
plist = [i for i in range(2, num + 1) if is_prime(i)]
flag = False

for i in range(len(plist)):
    for j in range(i, len(plist)):
        if plist[i] + plist[j] == num:
            flag = True
            break
    if flag:
        break
if flag:
    print('Yes')
else:
    print('No')

--------------------------------------------------------------------------------------------
#find the GCD of two numbers using recursion
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = gcd(num1, num2)
print("GCD of", num1, "and", num2, "is:", result)
------------------------------------------------------------------------------------------------
#check whether two numbers are co-prime or not using recursion
def is_coprime(a, b):
    if b == 0:
        return a == 1
    else:
        return is_coprime(b, a % b)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = is_coprime(num1, num2)
print("Numbers are co-prime" if result else "Numbers are not co-prime")
----------------------------------------------------------------------------------------------------------
#find the GCD of a number using recursion
def gcd(n, i=2):
    if n == 1:
        return 1
    if n % i == 0:
        return i
    else:
        return gcd(n, i + 1)
num = int(input("Enter a number: "))
result = gcd(num)
print("GCD of", num, "is:", result)
-----------------------------------------------------------------------------------------
'''Input:20
Output:3
Expalanation:
N=20
If we list the numbers that divide 20,they are
1,2,4,5,10,20
1 is not a square free number,4 is a perfect square,and 20 is divisible by 4,a perfect square 2 and 5,being prime are square free,
and 10 is divisible by 1,2,5 and 10,none of which are perfect squares.Hence the square free numbers that divide 20 are 2,5,10.Hence the result is 3 '''
num = int(input("Enter a number: "))
count = 0
for i in range(2, num + 1):  
    if num % i == 0:
        sqrt_i = int(i ** 0.5)
        is_square_free = True
        for j in range(2, sqrt_i + 1):
            if i % (j ** 2) == 0:
                is_square_free = False
                break
        if is_square_free:
            count += 1
print("Number of square-free divisors:", count)
