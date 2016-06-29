from salsa20 import XSalsa20_xor
import os, binascii
from os import urandom
import distance
import itertools

IV = urandom(24) # lenght must be 24. Return a string of n random bytes suitable for cryptographic use.

KEY_1 = b'80000000000000000000000000000000'
KEY_2 = b'80000000000000000000000000000001' # lenght must be 32

plaintext_1 = b'eea6a7251c1e72916d11c2cb214d3c252539121d8e234e652d651fa4c8cff880309e645a74e9e0a60d8243acd9177ab51a1beb8d5a2f5d700c093c5e5585579625337bd3ab619d615760d8c5b224a85b1d0efe0eb8a7ee163abb0376529fcc09bab506c618e13ce777d82c3ae9d1a6f972d4160287cbfe60bf2130fc0a6ff6049d0a5c8a82f429231f0080'

# for i in range(0,9999):
cipher_key_1 = XSalsa20_xor(plaintext_1, IV, KEY_1)
length_key = (len(cipher_key_1)) # returns the length of the cipher
cipher_key_2 = XSalsa20_xor(plaintext_1, IV, KEY_2)

hamming_key = distance.hamming(cipher_key_1, cipher_key_2)
aval_effect_key = (float(hamming_key))/length_key

print(hamming_key, aval_effect_key)
