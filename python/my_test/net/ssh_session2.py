import paramiko
import minitest
from paramiko_expect import SSHClientInteraction

client = paramiko.SSHClient()
client.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())

# client.connect("10.160.19.40", username='root', password='fortinet')
client.connect("qa-app1", username='root', password='a')
prompt = '\S+#\s+'
interact = SSHClientInteraction(client, timeout=10, display=False)
# interact.expect(prompt)

interact.send('pwd')
interact.current_output.p()
interact.expect(prompt, timeout=1)
cmd_output = interact.current_output_clean
cmd_output.p()

interact.send('cd /')
interact.expect(prompt)
cmd_output = interact.current_output_clean
cmd_output.p()

interact.send('pwd')
interact.expect(prompt)
cmd_output = interact.current_output_clean
cmd_output.p()

interact.send('ls')
interact.expect(prompt)
cmd_output = interact.current_output_clean
cmd_output.p()
