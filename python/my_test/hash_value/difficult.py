import hashlib

if __name__ == '__main__':
    from minitest import *

    with test("less than 1000"):
        origin_text = "I am Satoshi Nakamoto"
        input_text = origin_text + str(13)
        hash_value = hashlib.sha256(input_text).hexdigest()
        hash_value.must_equal(
                "0ebc56d59a34f5082aaef3d66b37a661696c2b618e62432727216ba9531041a5")
        pass