from ngrok_api import *

for name, tunnel in get_ngrok_tunnels():
    local_url = get_ngrok_url(name, local=True)
    public_url = get_ngrok_url(name, local=False)
    print('{:12s} {} <-> {}'.format(name, public_url, local_url))