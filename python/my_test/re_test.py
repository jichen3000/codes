import re

src = "     <LogFilePath>C:\\</LogFilePath>\n"
complex_src = "     <LogFilePath mm='123'>C:\\</LogFilePath>\n"
re_pattern = "(\<LogFilePath.*\>).+(\<\/LogFilePath\>)"
replace_str = r"\1/usr/colin/\2"

print re.search('\s+\.*','  sss')
print re.search(re_pattern,src).group(1)

print "src:", src
dst = re.sub(re_pattern,replace_str,src)
print "dst:",dst
dst = re.sub(re_pattern,replace_str,complex_src)
print "dst:",dst
dst = re.sub(re_pattern,replace_str,"<123>ddd</123>")
print "dst:",dst


src = '  DownloadFileDestination="c:\DOWNLOAD FILE_DIR"'
re_pattern = "(\s*DownloadFileDestination\s*=\s*).+"
replace_str = r'\1"/usr/ini/"'
print "src:", src
dst = re.sub(re_pattern,replace_str,src)
print "dst:",dst
