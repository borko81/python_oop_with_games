from struct import pack, unpack

name = 'first last'

print(pack('c', b'a'))

byte_integers = pack('ii', 1, 123)
print(byte_integers)

print(unpack('ii', byte_integers))
