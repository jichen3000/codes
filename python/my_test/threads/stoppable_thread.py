from threading import Thread, current_thread

from time import sleep

def func_with_check_stop(n, result, check_func):
    assert len(result) > 0, "the result must a list with one element"
    assert callable(check_func), "the check_func must be cllable"
    for i in range(n):
        if check_func():
            result[0] = "force stop"
            return
        print("i: ", i)
        sleep(0.5)
    result[0] = "finish"
    print("finish")

def func_with_check_stop2(n, result):
    '''
        using need_stop to let thread stop
    '''
    assert len(result) > 0, "the result must a list with one element"
    for i in range(n):
        if hasattr(current_thread(),"need_stop") and current_thread().need_stop:
            result[0] = "force stop"
            return
        print("i: ", i)
        sleep(0.5)
    result[0] = "finish"
    print("finish")


if __name__ == '__main__':
    from minitest import *




    # with test(func_with_check_stop):
    #     res = [""]
    #     stop_flag = {}
    #     thread_name = "thread1"
    #     def check_stop():
    #         return stop_flag.get(thread_name, False)
    #     st = Thread(name=thread_name, target=func_with_check_stop, args=(10, res, check_stop))
    #     st.start()
    #     sleep(1)
    #     stop_flag[thread_name] = True
    #     st.join()
    #     res.p()
    #     "ok".p()

    with test(func_with_check_stop2):
        res = [""]
        stop_flag = {}
        thread_name = "thread1"
        st = Thread(name=thread_name, target=func_with_check_stop2, args=(10, res))
        # st.need_stop = False
        st.start()
        sleep(1)
        st.need_stop = True
        st.join()
        res.p()
        "ok".p()

#     with test():
# def foo(bar, baz):
#   print('hello {0}'.format(bar))
#   return 'foo' + baz

# from multiprocessing.pool import ThreadPool
# pool = ThreadPool(processes=1)

# async_result = pool.apply_async(foo, ('world', 'foo'))        
