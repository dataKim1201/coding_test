import sys
input = sys.stdin.readline

def is_palindrome(text):
    return all([True if text[i] == text[-(i+1)] else False for i in range(len(text) // 2)])

text = input().strip()
print(int(is_palindrome(text)))