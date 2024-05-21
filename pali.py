def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

if __name__ == '__main__':
     s=input("Enter a string:")
     is_palindrome(s)
     print(is_palindrome(s))