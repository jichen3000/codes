def print_me(msg):
	print "msg: %s " % msg

print_me("123")


import itertools
import module1
module1.mm1()

a = ((0, 0, 0),(0, 1))

print min(a, key=lambda x: len(x))

def ormap1(fun, *iter):
	for i in zip(*iter):
		fun_result = fun(*i)
		if fun_result:
			return fun_result
	return False
def ormap(fun, iter):
	#lazy_result=(fun(i) for i in iter)
	return list(itertools.takewhile(fn(i), iter))[0]
	#return False
def l2(i):
	print i
	return i > 2
def l3(i,j):
	print i,j
	return i > 2 and j > 2
print ormap(l2, (2,3,4))
print ormap(l2, (2,1,0))
print ormap(l2, tuple())
# print ormap(l3, (2,3,4),(2,3,4))
# print ormap(l3, (2,1,0),(2,1,2))
# print ormap(l3, tuple(),tuple())

    #     import SecurityToken
    #     import Tkinter

    #     # construct eToken
    #     etok = SecurityToken.eToken_real()
        
    #     root = Tkinter.Tk()
    #     root.withdraw()
    #     pinwin = SecurityToken.getpw(root)
    #     et_pin = pinwin.pin

    #     etok.login(et_pin)
    #     token_sn = etok.info.serialNumber.strip()

    # config = ConfigParser.SafeConfigParser()
    # flash = SafeNetWrapper.getFlashChar()
    # # Read the Cesium Server Hostname from the atom.conf file in the ROM area.
    # confloc = flash + ":\\conf\\atom.conf"
    # config.read(['atom.conf', confloc])

    # if useToken:
    #     cesium_server = config.get('ATOM_Config', 'CesiumServer')
    #     print >> sys.stderr, 'cesium_server is {}'.format(cesium_server)
    #     # cesium_server = "10.140.29.48"
    # else:


    # HTTP access
    import urllib2
    req = urllib2.Request(CONNECTING_URL)
    opener = urllib2.build_opener()
    f = opener.open(req, data = request_xml)
    response_xml = f.read()
    #END
    
    # HTTPS access
    # opener = atomurllib2.build_opener(etok.ssl_ctx)
    # print "CONNECTING_URL:",CONNECTING_URL
    # try:
    #    req = atomurllib2.Request(CONNECTING_URL, data=request_xml)
    # except:
    #    print '\n***Problems sending requests to the remote server, please contact Support for assistance'
    #    print sys.exc_info()
    #    bad_response=sys.exc_info()[1]
    #    return bad_response
    # try:
    #    f = opener.open(req)
    #    response_xml = f.read()
    # except:
    #    bad_response='\n***Could not open and read the destination URL:%s'%CONNECTING_URL
    #    print bad_response
    #    print sys.exc_info()
    #    return '\n***Could not open the remote URL for reading, please contact Support for assistance' 
