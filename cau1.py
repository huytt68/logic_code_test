def isPalindrome(s):
    cleanString = ''.join(char for char in s if char.isalnum()).replace(" ","").lower()
    reverseString = ''.join(reversed(cleanString))
    if(cleanString==reverseString):
        return True
    else:
        return False
        
s=input()
print(isPalindrome(s))