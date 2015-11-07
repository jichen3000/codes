class NormalConnection(object):
    def __init__(self):
        self.state = 'CLOSED'
    def read(self):
        if self.state != 'OPEN':
            raise RuntimeError('Not open') 
        return 'reading'
    
    def write(self, data):
        if self.state != 'OPEN':
            raise RuntimeError('Not open') 
        return 'writing'
    
    def open(self):
        if self.state == 'OPEN':
            raise RuntimeError('Already open') 
        self.state = 'OPEN'

    def close(self):
        if self.state == 'CLOSED':
            raise RuntimeError('Already closed') 
        self.state = 'CLOSED'


class ComplexConnection(object):
    def __init__(self):
        self.new_state(ClosedConnectionState) 
    def new_state(self, newstate):
        self._state = newstate

    # Delegate to the state class
    def read(self):
        return self._state.read(self)
    def write(self, data):
        return self._state.write(self, data)
    def open(self):
        return self._state.open(self)
    def close(self):
        return self._state.close(self)

# Connection state base class
class ConnectionState(object):
    @staticmethod
    def read(conn):
        raise NotImplementedError()
    @staticmethod
    def write(conn, data):
        raise NotImplementedError()
    @staticmethod
    def open(conn):
        raise NotImplementedError()
    @staticmethod
    def close(conn):
        raise NotImplementedError()

# Implementation of different states
class ClosedConnectionState(ConnectionState): 
    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')
    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not open')
    @staticmethod
    def open(conn): 
        conn.new_state(OpenConnectionState)
    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')

class OpenConnectionState(ConnectionState): 
    @staticmethod
    def read(conn): 
        print('reading')
    @staticmethod
    def write(conn, data): 
        print('writing')
    @staticmethod
    def open(conn):
        raise RuntimeError('Already open')
    @staticmethod
    def close(conn): 
        conn.new_state(ClosedConnectionState)  

class Connection(object):
    def __init__(self):
        self.new_state(ClosedConnection) 
    def new_state(self, newstate):
        self.__class__ = newstate 
    def read(self):
        raise NotImplementedError() 
    def write(self, data):
        raise NotImplementedError() 
    def open(self):
        raise NotImplementedError() 
    def close(self):
        raise NotImplementedError()

class ClosedConnection(Connection): 
    def read(self):
        raise RuntimeError('Not open') 
    def write(self, data):
        raise RuntimeError('Not open') 
    def open(self):
        self.new_state(OpenConnection) 
    def close(self):
        raise RuntimeError('Already closed')

class OpenConnection(Connection): 
    def read(self):
        print('reading') 
    def write(self, data):
        print('writing') 
    def open(self):
        raise RuntimeError('Already open') 
    def close(self):
        self.new_state(ClosedConnection)

if __name__ == '__main__':
    from minitest import *

    with test(ComplexConnection):
        cc = ComplexConnection()
        # cc._state.pp()
        (lambda : cc.read()).must_raise(RuntimeError, "Not open")

    with test(Connection):
        c = Connection()
        (lambda : c.read()).must_raise(RuntimeError, "Not open")
        c.open()
        c.read()
        str(c.__class__).must_equal("<class '__main__.OpenConnection'>")
