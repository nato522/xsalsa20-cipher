from salsa20 import XSalsa20_xor
import os, binascii
from os import urandom
import distance
import xlsxwriter
import itertools

IV = urandom(24) # lenght must be 24. Return a string of n random bytes suitable for cryptographic use.
KEY_1 = b'00000000000000000000000000000000' # lenght must be 32
KEY_2 = b'11111111111111111111111111111111' # lenght must be 32

workbook = xlsxwriter.Workbook('results.xlsx') # create new excel sheet
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 20) # make column A wider
worksheet.set_column('B:B', 20) # make column B wider
worksheet.write(0, 0, "Distancia de Hamming") # title of column A
worksheet.write(0, 1, "Efecto Avalancha") # title of column B

# plaintext = b'cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.' # message to encode, will be random
plaintext = []
for i in range(0,10000):
  plaintext.append(binascii.b2a_hex(urandom(16))) # insert randomly generated plaintext (in hexadecimal)
  # cipher_1 = (AES.new(orig_key, AES.MODE_CFB, iv, segment_size=128).encrypt(plaintext[i]).encode("hex") ) # encrypt the plaintext with the key
  cipher_1 = XSalsa20_xor(plaintext[i].encode("hex"), IV, KEY_1)
  length = (len(cipher_1)) # returns the length of the cipher
  # cipher_2 = (AES.new(modified_key, AES.MODE_CFB, iv, segment_size=128).encrypt(plaintext[i]).encode("hex")) # encrypt the plaintext with the modified key
  cipher_2 = XSalsa20_xor(plaintext[i].encode("hex"), IV, KEY_2)
  hamming = distance.hamming(cipher_1, cipher_2)
  # print(hamming) # calculate Hamming's distance
  aval_effect = float(hamming)/length
  # print(aval_effect) # calculate the avalanche effect
    # print(dist)
    # print(aval_effect)
  worksheet.write(i+1, 0, hamming) # add the result of the distance to the excel sheet
  worksheet.write(i+1, 1, aval_effect) # add the result of the avalanche effect to the excel sheet

workbook.close() # close excel file


# ciphertext = XSalsa20_xor(b"IT'S A YELLOW SUBMARINE", IV, KEY_1)
# print(XSalsa20_xor(ciphertext, IV, KEY_1).decode())

# from salsa20 import XSalsa_xor
# import os, binascii
# from os import urandom
# import distance # to obtain hamming distance
# import xlsxwriter # to export the result into a table
# import itertools # to randomly generate binary strings
#
# IV = urandom(24)
# KEY_1 = "generate_original_key"
# # modified only one bit in the original key
# KEY_2 = "generate_modified_key"
#
# unhexlify = binascii.unhexlify
#
# iv = unhexlify(IV) # initialization vector / not changed
#
# orig_key = unhexlify(KEY_1) # original key
# modified_key = unhexlify(KEY_2) # modified key
#
# workbook = xlsxwriter.Workbook('results.xlsx') # create new excel sheet
# worksheet = workbook.add_worksheet()
# worksheet.set_column('A:A', 20) # make column A wider
# worksheet.set_column('B:B', 20) # make column B wider
# worksheet.write(0, 0, "Distancia de Hamming") # title of column A
# worksheet.write(0, 1, "Efecto Avalancha") # title of column B
#
# plaintext = [] # create an array
# for i in range(0,1000):
#   plaintext.append(binascii.b2a_hex(urandom(16))) # insert randomly generated plaintext (in hexadecimal)
#   # cipher_1 = (AES.new(orig_key, AES.MODE_CFB, iv, segment_size=128).encrypt(plaintext[i]).encode("hex") ) # encrypt the plaintext with the key
#   cipher_1 = XSalsa20_xor(plaintext[i].encode("hex"), IV, KEY_1)
#   length = (len(cipher_1)) # returns the length of the cipher
#   # cipher_2 = (AES.new(modified_key, AES.MODE_CFB, iv, segment_size=128).encrypt(plaintext[i]).encode("hex")) # encrypt the plaintext with the modified key
#   cipher_2 = XSalsa20_xor(plaintext[i].encode("hex"), IV, KEY_2)
#
#   distancia = (distance.hamming(cipher_1, cipher_2)) # calculate Hamming's distance
#   aval_effect = float(distancia) / length # calculate the avalance effect
#   worksheet.write(i+1, 0, distancia) # add the result of the distance to the excel sheet
#   worksheet.write(i+1, 1, aval_effect) # add the result of the avalanche effect to the excel sheet
# workbook.close() # close excel file
#
#
