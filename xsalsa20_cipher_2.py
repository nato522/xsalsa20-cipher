from salsa20 import XSalsa20_xor
import os, binascii
from os import urandom
import distance
import xlsxwriter
import itertools

IV = urandom(24) # lenght must be 24. Return a string of n random bytes suitable for cryptographic use.
# KEY_1 = b'00000000000000000000000000000000' # lenght must be 32
KEY_1 = b'dae389bc99c9ca9ab23000cde242411f'
KEY_2 = b'eae389bc99c9ca9ab23000cde242411f' # lenght must be 32
# KEY_1 = binascii.unhexlify(("00000001").encode('hex'))
# KEY_2 = binascii.unhexlify(("00000002").encode('hex'))

workbook = xlsxwriter.Workbook('results2.xlsx') # create new excel sheet
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 20) # make column A wider
worksheet.set_column('B:B', 20) # make column B wider
worksheet.write(0, 0, "Distancia de Hamming") # title of column A
worksheet.write(0, 1, "Efecto Avalancha") # title of column B
worksheet.write(3, 5, "100000 iteraciones") # title of column B

plaintext = b'Mensaje a cifrar'
# plaintext.append(binascii.b2a_hex(urandom(16))) # insert randomly generated plaintext (in hexadecimal)
for i in range(0,100000):
  # plaintext.append(binascii.b2a_hex(urandom(256))) # insert randomly generated plaintext (in hexadecimal)
  # print(plaintext)
  cipher_1 = XSalsa20_xor(plaintext, IV, KEY_1)
  length = (len(cipher_1)) # returns the length of the cipher
  cipher_2 = XSalsa20_xor(plaintext, IV, KEY_2)
  hamming = distance.hamming(cipher_1, cipher_2)
  aval_effect = (float(hamming))/length
  worksheet.write(i+1, 0, hamming) # add the result of the distance to the excel sheet
  worksheet.write(i+1, 1, aval_effect) # add the result of the avalanche effect to the excel sheet

workbook.close() # close excel file
