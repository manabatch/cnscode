def main():
    str = "Hello World"
    str1 = [''] * 11
    length = len(str)
    
    print("The Plain Text: ", end="")
    for i in range(length):
        print(str[i], end="")
    
    print("\nThe Cipher Text: ", end="")
    for i in range(length):
        str1[i] = chr(ord(str[i]) ^ 0)
        print(str1[i], end="")
    
    print()

if __name__ == "__main__":
    main()
