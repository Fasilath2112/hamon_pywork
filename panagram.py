def is_panagram(s):
    s = s.lower()
    a = set('abcdefghijklmnopqrstuvwxyz')
    for char in a:
        if char not in s:
            return False
    return True

if __name__ == '__main__':
    str1 = "the quick brown fox jumps over the lazy dog"
    print(is_panagram(str1))