import threading

def send_request():
    import requests
    print threading.current_thread().name
    url = 'http://localhost:9999/hello/' + threading.current_thread().name
    response=requests.get(url)

    print response.content

def start_threads(count):
    def create_new(index):
        cur_thread = threading.Thread(target=send_request, args=())
        cur_thread.setDaemon(True)
        return cur_thread

    threads = map(create_new, range(count))
    map(threading.Thread.start, threads)
    return map(threading.Thread.join, threads)


if __name__ == '__main__':
    import sys
    import requests
    print "DEFAULT_RETRIES",requests.adapters.DEFAULT_RETRIES
    requests.adapters.DEFAULT_RETRIES = 5
    print "after DEFAULT_RETRIES",requests.adapters.DEFAULT_RETRIES
    count = 10
    if len(sys.argv) > 1:
        count = int(sys.argv[1])
    print "It will start %d threads." % count
    start_threads(count)
    print "ok"

