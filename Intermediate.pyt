'''Module 3: Individual Programming Assignment 1
Thinking Like a Programmer
This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.
    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "
    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 
    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

letter = str(input("Enter Letter Here"))
shift = int(input("Enter Number Here"))
encryption = "" #encryption does not have a string value at the start
 
for c in letter:

    # check if character is an uppercase letter
    if c.isupper():

        # find the position in 0-25 in ASCII stuff 
        c_unicode = ord(c) #find the ASCII value of the letter
        c_index = ord(c) - ord("A") #find it in terms of 0-25, since A is 65 and other numbers go higher?

        # perform shift
        new_index = (c_index + shift) % 26 #shift, while the %26 loops it back, not sure how though

        # convert to new character
        new_unicode = new_index + ord("A") #get ASCII value for new letter
        new_character = chr(new_unicode) #get the letter from the ASCIII
        encryption = encryption + new_character #gives the blank encryption a value

    else: #if its not uppercase, leave it as is
        encryption += c

print("Plain text:",letter)
print ("Values to move by:",new_index)
print("Encrypted text:",encryption)

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

message = str(input("Enter Message Here"))
shift = int(input("Enter Number Here"))
encryption = "" #encryption does not have a string value at the start
 
for c in message:

    # check if character is an uppercase letter
    if c.isupper():

        # find the position in 0-25 in ASCII stuff 
        c_unicode = ord(c) #find the ASCII value of the letter
        c_index = ord(c) - ord("A") #find it in terms of 0-25, since A is 65 and other numbers go higher?

        # perform shift
        new_index = (c_index + shift) % 26 #shift, while the %26 loops it back, not sure how though

        # convert to new character
        new_unicode = new_index + ord("A") #get ASCII value for new letter
        new_character = chr(new_unicode) #get the letter from the ASCIII
        encryption = encryption + new_character #gives the blank encryption a value

    else: #if its not uppercase, leave it as is
        encryption += c
        
print("Plain text:",message)
print ("Values to move by:",new_index)
print("Encrypted text:",encryption)

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.
    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.
    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

letter = str(input("Enter Letter Here"))
print ("Enter Character")
letter_shift =  str(input("")) #i cant fill it with text idk why
lettershiftval = ord(letter_shift) - ord("A")
print ("Value to move letter by:", lettershiftval)
encryption = "" #encryption does not have a string value at the start

for c in letter:

    # check if character is an uppercase letter
    if c.isupper():

        # find the position in 0-25 in ASCII stuff 
        c_unicode = ord(c) #find the ASCII value of the letter
        c_index = ord(c) - ord("A") #find it in terms of 0-25, since A is 65 and other numbers go higher?

        # perform shift with the lettershiftvalue
        new_index = (c_index + lettershiftval) % 26 #shift, while the %26 loops it back, not sure how though

        # convert to new character
        new_unicode = new_index + ord("A") #get ASCII value for new letter
        new_character = chr(new_unicode) #get the letter from the ASCIII
        encryption = encryption + new_character #gives the blank encryption a value

    else: #if its not uppercase, leave it as is
        encryption += c
        
print("Plain text:",letter)
print("Encrypted text:",encryption)

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.
    Example:
    vigenere_cipher("A C", "KEY") -> "K A"
    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

def generateKey(string, key): #generate the key
  key = list(key) #makes it a list so that the indiv letters in the mssg can get a value
  if len(string) == len(key): #if the message length is equal to key length
    return(key) 
  else:                             # if its not equal, it repeats
    for i in range(len(string) -len(key)): 
      key.append(key[i % len(key)]) 
  return("" . join(key)) 
  
def encryption(string, key): #gets values of the letters typed in the message
  encrypt_text = [] 
  for i in range(len(string)): 
    x = (ord(string[i]) +ord(key[i])) % 26
    x += ord('A') 
    encrypt_text.append(chr(x)) 
  return("" . join(encrypt_text)) 
def decryption(encrypt_text, key): #gets values of letters typed in key?
  orig_text = [] 
  for i in range(len(encrypt_text)): 
    x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
    x += ord('A') 
    orig_text.append(chr(x)) 
  return("" . join(orig_text)) 
if __name__ == "__main__": #puts everything back together
  message = input("Enter the message: ")
  keyword = input("Enter the keyword: ")
  key = generateKey(message, keyword) 
  encrypt_text = encryption(message,key) 
  print("Encrypted message:", encrypt_text) 
  print("Decrypted message:", decryption(encrypt_text, key)) 