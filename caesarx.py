# how to access the command line argument
import sys
import cs50

#validating length of command line arguments
if not len(sys.argv)== 2:
  print("Usage: python caesar.py key")
  exit(1)

#getting plaintext from the user
plaintext = cs50.get_string("plaintext: ")
print("ciphertext: ", end='')

# initializing the argument into a variable and casting it as a number
key = int(sys.argv[1]) % 26

for i in range(0, len(plaintext),1):
  encrypt = key + plaintext[i]

    #if there is a space print space
if plaintext[i].isalpha() == False:
        print(plaintext[i], end='')

    # handling lowercase
if plaintext[i].islower():
        if encrypt < 122:
            print(key + plaintext[i])
        elif encrypt > 122:
            print( plaintext[i] - (26 - key))

    #handling uppercase
if plaintext[i].isupper():
        if encrypt < 90:
            print(key + plaintext[i])
        elif encrypt > 90:
            print(plaintext[i] - (26 - key))

print()
