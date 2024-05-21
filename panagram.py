def is_panagram(s):
    s = s.lower()
    alphabets = set('abcdefghijklmnopqrstuvwxyz')
    for char in alphabets:
        if char not in s:
            return False
    return True

if __name__ == '__main__':
    string = "the quick brown fox jumps over the lazy dog"
    print(is_panagram(string))
