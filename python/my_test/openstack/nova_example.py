
# pip install python-novaclient
from novaclient.v2 import client
from novaclient.v2 import networks

def get_client():
    tenant_name="demo"
    username="demo"
    password="vagrant"
    auth_url="http://controller:5000/v2.0"
    return client.Client(username, password, 
            tenant_name, auth_url, service_type="compute")

def get_server(nova_client, server_name):
    return [server for server in nova_client.servers.list() if server.name==server_name][0]

if __name__ == '__main__':
    from minitest import *

    nova_client = get_client()
    with test(get_client):
        nova_client.servers.list().pp()

    with test(get_server):
        d1 = get_server(nova_client, "d1")
        d1.p()
        # d1.stop()
        # d1.start()

    with test("create a server"):
        name = "d2"
        image = nova_client.images.list()[0]
        flavor = nova_client.flavors.list()[0]
        security_group = nova_client.security_groups.list()[0]
        demo1_network = nova_client.networks.list()[-1]
        demo_key = nova_client.keypairs.list()[0]
        d2 = nova_client.servers.create(name, image, flavor, 
                security_groups=[security_group.name],
                key_name=demo_key.name,
                nics=[{'net-id': demo1_network.id}])
        # d2.add_fixed_ip(demo1_network.id)



