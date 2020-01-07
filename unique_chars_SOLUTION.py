# Solution 1
def unique_chars(string):
    counts = {}
    for char in string:
        if char in counts:
            return False
        else:
            counts[char] = 1

    return True

# Solution 2
def uni_char(s):
    u = set()
    for c in s:
        if c in u:
            return False
        else:
            u.add(c)
    return True

# Solution 3
def uni_char2(s):
    return len(set(s)) == len(s)

