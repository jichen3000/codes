import paramiko
import minitest

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())

ssh.connect("10.160.13.107", username='admin', password='')

def run_cmd(ssh, cmd):
    cmd.p()
    stdin, stdout, stderr = ssh.exec_command(cmd)
    for line in stdout:
        print '... ' + line.strip('\n')
    for line in stderr:
        print 'eee ' + line.strip('\n')

    stderr.p()


# run_cmd(ssh, "ls")
# run_cmd(ssh, "mm")


# chan=ssh.get_transport().open_session()
# chan.get_pty()
chan=ssh.invoke_shell()
# f = chan.makefile()
result_int = chan.send('config sys global\n')
output = chan.read(2048)

# print f.read()
chan.exec_command("show")
# print f.read()
# chan.send("password\n")

ssh.close()


