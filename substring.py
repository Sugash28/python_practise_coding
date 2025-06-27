def lengthOfLongestSubstring(s):
    b = []  # List to store current substring
    max_len = 0

    for char in s:
        if char in b:
            # Remove characters until duplicate is gone
            while char in b:
                b.pop(0)
        b.append(char)
        max_len = max(max_len, len(b))
    
    return max_len

# Test
a = "abcabcbb"
print(lengthOfLongestSubstring(a))  # Output: 3
