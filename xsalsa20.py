from salsa20 import XSalsa20_xor
import os, binascii
from os import urandom
import distance
import xlsxwriter
import itertools

IV = urandom(24) # lenght must be 24. Return a string of n random bytes suitable for cryptographic use.

KEY_1 = b'dae389bc99c9ca9ab23000cde242411f'
KEY_2 = b'efd471cb87c2ca90b24b00ade253367d' # lenght must be 32

workbook = xlsxwriter.Workbook('results.xlsx') # create new excel sheet
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 20) # increase width column A
worksheet.set_column('B:B', 20) # increase width column B
worksheet.set_column('C:C', 20) # increase width column C
worksheet.set_column('D:D', 20) # increase width column D
worksheet.set_column('E:E', 20) # increase width column E
worksheet.write(0, 0, "Distancia de Hamming") # title of column A
worksheet.write(0, 1, "Efecto Avalancha") # title of column B
worksheet.write(0, 3, "Distancia de Hamming") # title of column D
worksheet.write(0, 4, "Efecto Avalancha") # title of column E

plaintext_1 = b'eea6a7251c1e72916d11c2cb214d3c252539121d8e234e652d651fa4c8cff880309e645a74e9e0a60d8243acd9177ab51a1beb8d5a2f5d700c093c5e5585579625337bd3ab619d615760d8c5b224a85b1d0efe0eb8a7ee163abb0376529fcc09bab506c618e13ce777d82c3ae9d1a6f972d4160287cbfe60bf2130fc0a6ff6049d0a5c8a82f429231f0080'

plaintext_2 = b'eea6a7251c1e72916d11c2cb214d3c252539121d8e234e652d651fa4c8cff880309e645a74e9e0a60d8243acd9177ab51a1beb8d5a2f5d700c093c5e5585579625337bd3ab619d615760d8c5b224a85b1d0efe0eb8a7ee163abb0376529fcc09bab506c618e13ce777d82c3ae9d1a6f972d4160287cbfe60bf2130fc0a6ff6049d0a5c8a82f429231f0081'

for i in range(0,10000):
  cipher_key_1 = XSalsa20_xor(plaintext_1, IV, KEY_1)
  length_key = (len(cipher_key_1)) # returns the length of the cipher
  cipher_key_2 = XSalsa20_xor(plaintext_1, IV, KEY_2)

  cipher_text_1 = XSalsa20_xor(plaintext_1, IV, KEY_1)
  length_text = (len(cipher_text_1)) # returns the length of the cipher
  cipher_text_2 = XSalsa20_xor(plaintext_2, IV, KEY_1)

  hamming_key = distance.hamming(cipher_key_1, cipher_key_2)
  aval_effect_key = (float(hamming_key))/length_key

  hamming_text = distance.hamming(cipher_text_1, cipher_text_2)
  aval_effect_text = (float(hamming_text))/length_text

  worksheet.write(i+1, 0, hamming_key) # add the result of the distance to the excel sheet
  worksheet.write(i+1, 1, aval_effect_key) # add the result of the avalanche effect to the excel sheet

  worksheet.write(i+1, 3, hamming_text) # add the result of the distance to the excel sheet
  worksheet.write(i+1, 4, aval_effect_text) # add the result of the avalanche effect to the excel sheet

workbook.close() # close excel file
