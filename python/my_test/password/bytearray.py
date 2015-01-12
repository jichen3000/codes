import array

def decode_bytestrings(the_value):
    if isinstance(the_value, bytearray):
        return ''.join('{:02x}'.format(x) for x in the_value)
    return the_value

def int_list_to_bytearray(int_list):
    return array.array('B', int_list)

if __name__ == '__main__':
    from minitest import *

    with test(""):
        byte_arr = bytearray('\xb9\xbd\xc5\xccXr\x83&)\x0b\xa9\xd8W\xe1')
        for a_byte in byte_arr:
            a_byte.pp()
        byte_arr = int_list_to_bytearray( 
            [185, 66, 137, 153, 112, 247, 127, 54, 231, 181, 145])
        for a_byte in byte_arr:
            a_byte.pp()
        # a.pp()
