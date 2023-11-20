def main():
    str = "Hello World"
    str1 = [''] * 11
    str2 = [''] * 11
    str3 = [''] * 11
    length = len(str)
    
    print("The Plain Text: ", end="")
    for i in range(length):
        print(str[i], end="")
    
    print("\nCipher text after AND Operation: ", end="")
    for i in range(length):
        str1[i] = chr(ord(str[i]) & 127)
        print(str1[i], end="")
    
    print("\nCipher text XOR Operation: ", end="")
    for i in range(length):
        str3[i] = chr(ord(str[i]) ^ 127)
        print(str3[i], end="")
    
    print("\nCipher text OR Operation: ", end="")
    for i in range(length):
        str2[i] = chr(ord(str[i]) | 127)
        print(str2[i], end="")
    
    print()

if __name__ == "__main__":
    main()
