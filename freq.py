def freq(s):
    dictionary = {}
    for char in s:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary

if __name__ == '__main__':
    string = input("Enter the string:")
    result = freq(string)
    print(result)  
