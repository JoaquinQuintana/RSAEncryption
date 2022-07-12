#!/usr/bin/env python3
import RSAFunctions

#main function
#Get user inputs to find public keys, private keys, encode messages and decode messages, 
def main():
    userInput = input('Enter 1 to find public keys\nEnter 2 to find private key\nEnter 3 to encode a message\nEnter 4 to decode a message \nEnter any other key to exit script: ', )       
    if userInput == '1':
        p = int(input('Enter p: '))
        q = int(input('Enter q: '))
        print(RSAFunctions.Find_Public_Key_e(p, q))
    elif userInput == '2':
        e = int(input('Enter e: '))
        p = int(input('Enter p: '))
        q = int(input('Enter q: '))
        print("d = ",RSAFunctions.Find_Private_Key_d(e, p, q))
    elif userInput == '3':
        n = int(input('Enter n: '))
        e = int(input('Enter e: '))
        message = input("Enter the message to encode: ")        
        print(RSAFunctions.Encode(n, e, message))
    elif userInput == '4':
        n = int(input('Enter n: '))
        d = int(input('Enter d: '))
        cipher_in = input("Enter the message to decode: ")
        cipher_strip = cipher_in.strip("[]")
        cipher = list(map(int, cipher_strip.split(',')))
        print(RSAFunctions.Decode(n, d, cipher))   
    else:
        print("Exited script or one needs to read instructions closer, i.e., please enter type integer between 1-4")

if __name__ == "__main__":
    """"
    Implement a main function such that:
    
    1. Asks the user to Get Keys, Encode or Decode.
    2. If Getting keys, it will need to ask for p and q. 
    3. If Encoding, it will need the message and public keys.
    4. If Decoding it will need the coded message, and public and private keys.
    
    You may implement this differently if you want, add more functions, 
    include a list of useful primes etc... 
    Just implement in a way that makes sense to you.
    And explain why.

    """
    main()