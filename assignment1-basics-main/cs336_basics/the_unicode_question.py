# what unicode character does chr(0) return ?
# it just reutnr nothing, see below
# chr(0) just return NULL character
print(chr(0))
print(chr(0) is None)
print(chr(0) == '')

# it is literally nothing 

# How does this character’s string representation (__repr__()) differ from its printed representation?
print(chr(0).__repr__())
#this does not print anything, bc chr(0) is null character
print('this is a test' + chr(0) + 'string')
test_string = 'this is a test string, 我是cs336n'
encoded = test_string.encode('utf-8')
print(encoded)

print(type(encoded))

print(list(encoded))
print(len(encoded))
encoded_16 = test_string.encode('utf-16')

print(list(encoded_16))
print(len(encoded_16))
encoded_32 = test_string.encode('utf-32')
print(list(encoded_32))
print(len(encoded_32))
# compara above length for each 8,16, 32, you will see differents between 8, 16 and 32.

# Consider the following (incorrect) function, which is intended to decode a UTF-8 byte string into
# a Unicode string. Why is this function incorrect? Provide an example of an input byte string
# that yields incorrect results.

def decode_utf8_bytes_to_str_wrong(bytestring: bytes):
    return "".join([bytes([b]).decode("utf-8") for b in bytestring])

encoded_example = "你好，hi there".encode("utf-8")
print(decode_utf8_bytes_to_str_wrong("hello world".encode("utf-8")))
print(decode_utf8_bytes_to_str_wrong(encoded_example))
# the above coding will split each words/characters like this: [你，好，h，i，t，h，e，r，e]
# the code will do bytes([your encode values for each words/characters]).decode() -> wrong


#Give a two byte sequence that does not decode to any Unicode character(s)
#to answer this question, we have to know utf 8 rules
# Rule: All continuation bytes must begin with 10xxxxxx (0x80–0xBF).They must follow a valid leading byte.
#       overlong encoding also will cuase some problems
#0x80 and 0xC0 are exmaples that we couldn't decode 



