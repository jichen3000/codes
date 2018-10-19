import paramiko
import minitest

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())

# ssh.connect("10.160.13.107", username='admin', password='')
ssh.connect("qa-app1", username='root', password='a')

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

channel = ssh.invoke_shell()
stdin = channel.makefile('wb')
stdout = channel.makefile('rb')
stdin.write("cd / \n exit \n")
print stdout.read()

stdin.write("pwd \n")
print stdout.read()

# chan=ssh.get_transport().open_session()
# chan.get_pty()
# chan=ssh.invoke_shell()
# # f = chan.makefile()
# result_int = chan.send('cd /\n')
# output = chan.read(2048)
# output.p()
# result_int = chan.send('pwd /\n')
# output = chan.read(2048)
# output.p()

# print f.read()
# chan.exec_command("show")
# print f.read()
# chan.send("password\n")

ssh.close()


