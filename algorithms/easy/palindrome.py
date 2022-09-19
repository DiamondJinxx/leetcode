def isPalindrome(x: int):
    return str(x) == str(x)[::-1]
    

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
