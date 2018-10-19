import paramiko
import minitest

# class SSH(object):
#     def __init__(host, username, password):

client = paramiko.SSHClient()
client.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())

# client.connect("10.160.34.152", username='root', password='fortinet')
client.connect("qa-app1", username='root', password='a')

def run_cmd(client, cmd):
    cmd.p()
    stdin, stdout, stderr = client.exec_command(cmd)
    for line in stdout:
        print '... ' + line.strip('\n')
    for line in stderr:
        print 'eee ' + line.strip('\n')

    stderr.p()

run_cmd(client, "pwd")
run_cmd(client, "cd /")
run_cmd(client, "pwd")
# run_cmd(client, "mm")


client.close()


