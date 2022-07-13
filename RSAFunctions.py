#!/usr/bin/env python3
import random
import timeit

def Convert_Text(_string):
    """
    Define this function such that it takes in a simple 
    string such as "hello" and outputs the corresponding
    standard list of integers (ascii) for each letter in the word hello.
    For example:
    _string = hello
    integer_list = [104, 101, 108, 108, 111]
    """
    #Use ord function to get ASCII code for a character
    #Then use map to iterate over the string and use ord function for ascii conversion. Append the result as a list to interger list
    integer_list = list(map(ord,_string))
    return integer_list

def Convert_Num(_list):
    """
    Do the opposite of what you did in the Convert_Text
    function defined above.
    
    Define this function such that it takes in a simple 
    string such as "hello" and outputs the corresponding
    list of integers for each letter in the word hello.
    For example:
    _list = [104, 101, 108, 108, 111]
    _string = hello
    """
 #using a loop and type integer chr caused an error due to a size limitation on type int we with the map alternative below which fixed the problem
    #Use chr function to get the correspnding chr from the current ASCII integer 
    #Then use map to iterate over the string and use str function to join the string. output a string called chr_list
    chr_list = list(map(chr,_list))
    chr_list = ''.join(map(str,chr_list))
    return chr_list

def Convert_Binary_String(_int):
    """
    Here, you need to define a function that converts an integer to
    a string of it's binary expansion.
    
    For example:
    _int = 345
    bits = 101011001
    """
    #create an empty list to accumulate binary number.
    bits = []
    #use a while loop to run the process up until n = n//2 returns zero.
    while (_int > 0):
        k = _int % 2 # Determine if the current value of n returns a zero or one, this is my binary output 
        _int = _int//2 # Perform floor division to reduce the value of n.
        bits.append(k) # accumulate binary output
        bit = bits[::-1] #reverse the binary list so it is in the correct order
    return bit #return binary number 

def FME(b, n, m):
    """
    1. Using the fast modular exponentiation algorithm.
    the below function should return b**n mod m.
    As described on page 254. (however, you may input the exponent and 
    then convert it to a string - the book verison imports the binary expansion)  
    2. You should use the function defined above
    Convert_Binary_String()
    3. Use this string to test which components are used in the calculation.
    4. Yes, there are many other ways to do this. 
***UPDATE*** You may use the function you developed in your prblme set - but be sure it is your own work commented etc.. and change inputs as needed.
    """  
    # intialize result to be 1
    result = 1
    #convert the exponent to binary using Convert_Binary_String. Use this to iterate with
    bi =  Convert_Binary_String(n)
    #reverse the binary string so we start with the first bit. 
    Binaryreverse = bi[::-1] 
    #iterate over the reversed binary number 
    for i in Binaryreverse:
        #take all bits that equal one 
        if i == 1: 
            # if the bit i equals one, then multiply the base by the last result and take mod m of this product
            result = (result*b) % m
        b = (b*b) % m #square the base and use this in the next iteration of the loop
    return(result) # return the result

def Euclidean_Alg(a, b):
    """
    1. Calculate the Greatest Common Divisor (GCD) of a and b.
    
    2. Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    The function must return a single integer 'x' which is
    the gcd of a and b.
    """
#define a function to calculate the GCD. We want this because we need to calculate the GCD of two number for testing relative primality. 
    while b != 0: # stop loop once b == 0 and return a.
        #calculate a mod b and update the value for b with this result. Also updated the value of the new value for a to be the old value of b.
        (a, b) = (b, a % b) 
    return a

def Find_Public_Key_e(p, q):
    """
    Implement this function such that
    it takes 2 primes p and q.
    
    Use the gcd function that you have 
    defined before.
    
    The function should return 2 elements as follows:
    public key: n
    public key: e 
    HINT: this function will run a loop to find e such 
    that e is relatively prime to (p - 1) (q - 1) 
    and not equal to p or q.
    """
    n = p*q # calculate n 
    relative = (p-1)*(q-1) # calculate the number which is relatively prime to e
    for i in range(random.randint(102,500000),10000000): # start searching for a value which is relatively prime to the variable relative. Start this search at 100 so we test larger numbers.  
        if Euclidean_Alg(i, relative) == 1: #when we test a number that provides a GCD of 1 return this value and call it e
            return 'This is the public key e,n:' ,i,n # return the public key (e,n)
        
#this is the extended euclidian algorithm 
def Extended_Eucliean_Algorithm(m,n):
    """
    This is the the Extended Eucliean Algorithm
    
    """
    (s1,t1) = (1,0)
    (s2,t2) = (0,1)
    #use a while loop to run the process up until n = n//2 returns zero.  
    while (n > 0):
        k = m % n # take m % n to reduce the value of  k which is n and eventually exit the loop.
        q = m//n # Perform floor division to update the quotient q which is used to calculate the new values for s2 and t2 
        #update m to be the current value of n and update n to be the current value of k 
        m = n
        n = k 
        #update the values of s1,t1 to be the old values of s2,t2 and update s2,t2 be the newly computed result from s1-(q*s2),t1-(q*t2)
        (s1_hat,t1_hat) = (s2,t2)
        (s2_hat,t2_hat) = (s1-(q*s2),t1-(q*t2))
        (s1,t1) = (s1_hat,t1_hat)
        (s2,t2) = (s2_hat,t2_hat)    
    return s1,t1 #outputs the Bezout's coefficients

def Find_Private_Key_d(e, p, q):
    """
    Implement this method
    to find the decryption exponent d such that
    d is the modular inverse of e. 
    
    This will use the Extended Eucliean Algorithm
    
    This function should return the following:
    d: the decryption component.
    """
    # to find d we need to find a number which is relatively prime to e, which I do here
    relatively_prime_to_e = (p-1)*(q-1) 
    #then using the value just found, which is relatively prime to e, we can use the Extended_Eucliean_Algorithm to find the private key d. 
    result = Extended_Eucliean_Algorithm(relatively_prime_to_e,e)
    # the value of d is the last index output from result, so I will only work with it
    d = result[-1]
    # d sometimes comes back as negative, which satisfies the results but not the encryption and decryption schemes. To make d poitive all the times it is computed
    # I created a conditional to take the product of (p-1)*(q-1) and added the negaive d to it to obtain a poitive d which worked and satisified the encryption.
    if d < 0:
        d = (p-1)*(q-1) + d 
    return d

def Encode(n, e, message):
    """
    Here, the message will be a string of characters.
    Use the function Convert_Text from 
    Second tool set and get a list of numbers.
    
    Encode each of those numbers using n and e and
    return the encoded cipher_text.
    """
    cipher_text = [] # assuming this is for storage
    cipher_nums = Convert_Text(message) # the message is converted to a list of standard of ascii integers for each letter
    for i in cipher_nums:
        #use fast modular exponentiation to compute the ciphertext. Using standard modular aritmatic is to slow and not useful here. 
        C = FME(i, e, n) 
        cipher_text.append(C) #accumulate results
    return cipher_text #return list containg the converted ciphertext

def Decode(n, d, cipher_text):
    """
    Here, the cipher_text will be a list of integers.
    First, you will decrypt each of those integers using 
    n and d.
    Later, you will need to use the function that converts the integers to a string 
    defined in second toolset
    to recover the original message as a string. 
    
    """
    message = ''# for storage
    message_nums = []
    for i in cipher_text:
        M = FME(i, d, n)
        message_nums.append(M)    
    message = Convert_Num(message_nums)
    return message

#Brute force method of finding factors.
def factorize(n):
# n is a number, return the smallest factor of n
    for i in range(2,n-1): # start iterations at 2 and end at the maximum in the list -1
        if n % i == 0: # if n is divisible by the current integer (i) return i becuase this is a factor
            return i
    return False # if n is not divisible by any of the integers return FALSE

def bruteForceFactor(n):
    timeit.default_timer()
    resultfact = factorize(n) 
    print("p = ",resultfact,'q = ', n//resultfact)
    print("Time neededto factor number: ",timeit.default_timer() )