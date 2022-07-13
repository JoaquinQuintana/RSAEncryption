# RSA Encryption 

## High level overview of a simple implementation of [Ron Rivest, Adi Shamir, and Leonard Adleman (RSA) encryption](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#:~:text=RSA%20involves%20a%20public%20key,by%20using%20the%20private%20key.).

RSA cryptography is one method of encrypting and decrypting messages and it is used widely in our daily lives. The package below contains the basic functions used in RSA and is in a lay format which is designed for someone with minimal knowledge of RSA to encrypt and decrypt messages. 

A few basic things the user must know. If encrypting messages users must pick two prime numbers that are large and relatively prime to one another, this is they have a greatest common divisor equal to one. The two numbers chosen by the user can be checked to see if they are relatively prime to one another by using the function ```Euclidean_Alg(a, b)``` which will return one if the two numbers are relatively prime. However, with this implementation there is no need to check this as the encode function will handle this for the user. They simply need to provide two large prime numbers, $p$ and $q$, and the message to be encrypt. 

### Running the main function

To get started, change the permission of ```the main.py``` file by typing ```chmod +x main.py``` (assuming the user is on a linux or unix machine). Next run the main function by typing ```./main.py```. This main function will ask the user if they would like to find public keys, find private keys, encode a message, decode a message or exit the function. 

The flow for encoding and decoding a message follows the structure below but is hidden from the user. To see the functions used please look at the file ```RSAFunctions.py```. For a more in depth look at the content and the idea behind this implementation of RSA see ```chapter 4 - Number Theory and Cryptography``` of the textbook ```Discrete Mathematics and Its Applications``` by ```Rosen, Kenneth``` [1].

### Encoding

Encoding is completely handled by the main function and only requires the user to input two large prime numbers and the message to be encoded. 

Behind the scene we create a ```key(n,e)```, which we will use to translate a message into a sequence of ciphertext blocks. Note that we will use the equation for encryption $$C = M^{e*mod(n)}$$ $C$ is the output ciphertext and $M$ is a single element in the message which will be converted to ciphertext. Here are the steps we take to achieve this.

1. Identify two distinct large prime numbers, $p$ and $q$ (the product of these two numbers is $n = pq$)
2. Use the function ```Find_Public_Key_e(p, q)`` to compute $n$ and $e$. This algorithm uses the [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor) to achieve this.
3. The message is the converted into a standard list of ascii integers 
4. Once converted to ascii we use $C = M^{e*mod(n)}$ to encrypt the ascii text to what is known as ciphertext.
5. Finally - accumulate and return the encrypted message.

### Decoding

Create a key $d$ using the function ```Find_Private_Key_d(e, p, q)```

The equation for decryption is $$M = C^{d*mod(n)}$$ $M$ is the output decoded message and $C$ is a single element in the ciphertext which will be converted to a piece of the message. To decrypt a message we need an encrypted message and the private key, $d$, to decrypt the ciphertext. If we do not know the private key we can find it if we are provided e, p and q by using the function ```Find_Private_Key_d(e, p, q)``` which returns $d$. Overall the decryption function takes each block of the ciphertext and converts it to a message $M$ by using the private key and finally the message is converted from ascii integers back into their respective characters.

**Reference**
1. Rosen, Kenneth H. “4/ Number Theory and Cryptography .” Discrete Mathematics and Its Applications, McGraw-Hill, New York, 2019. 
