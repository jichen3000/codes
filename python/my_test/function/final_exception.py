class ForceStop(Exception):
    pass

def test_final():
    try:
        raise ForceStop("force!!!")
    except ForceStop as e:
        print("ForceStop:",e)
    except Exception as e:
        print("e:",e)
    finally:
        print("in finally")


if __name__ == '__main__':
    from minitest import *

    with test(test_final):
        test_final()