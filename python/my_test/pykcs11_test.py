import PyKCS11

pkcs11 = PyKCS11.PyKCS11Lib()
#rom = SafeNetWrapper.getRomChar()
#flash = SafeNetWrapper.getFlashChar()
etoken_dll = 'etpkcs11.dll'
#engpath = rom + ":\\atom_daemon_dist\\"
#print "Flash Drive is - %s" %flash
pkcs11.load("C:/Windows/System32/" + etoken_dll)
# for slot in range(0,10):
info = pkcs11.getTokenInfo(2)
if info.model.strip() == "eToken":
    print "slot:",2
    print "token info:",info
    # break
# print "info",pkcs11.getAttributeValue()
