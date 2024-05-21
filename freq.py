def freq(s):
    dict1 = {}
    for char in s:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1
    return dict1

if __name__ == '__main__':
    str1 = input("Enter the string:")
    result = freq(str1)
    print(result)  
