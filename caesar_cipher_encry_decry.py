print("1. Encrypt password")
print("2. Decrypt password")
print("Enter your option: ")
value = int(input())

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


def encrypt(a):
    temp = ""
    for i in a:
        if i in alpha:
            new_index = (alpha.index(i)+3) % len(alpha)
            temp = temp + alpha[new_index]
        else:
            print("Invalid character")
            return

    print("Ciphertext: ",temp)


def decrypt(a):
    temp = ""
    for i in a:
        if i in alpha:
            new_index = (alpha.index(i)-3) % len(alpha)
            temp = temp + alpha[new_index]
        else:
            print("Invalid Character")
            return

    print("Plaintext: ", temp)


def switch_case(value):
    if value == 1:
        print("Enter your password for encryption: ")
        a = str(input())
        encrypt(a)
    elif value == 2:
        print("Enter your ciphertext for decryption: ")
        a = str(input())
        decrypt(a)
    else:
        print("Invalid number")
        

switch_case(value)