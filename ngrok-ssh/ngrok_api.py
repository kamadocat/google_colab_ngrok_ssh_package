import requests
import urllib.parse

def get_ngrok_info():
  return requests.get('http://localhost:4040/api/tunnels').json()

def get_ngrok_tunnels():
  for tunnel in get_ngrok_info()['tunnels']:
    name = tunnel['name']
    yield name, tunnel

def get_ngrok_tunnel(name):
  for name1, tunnel in get_ngrok_tunnels():
    if name == name1:
      return tunnel

def get_ngrok_url(name, local=False):
  if local:
    return get_ngrok_tunnel(name)['config']['addr']
  else:
    return get_ngrok_tunnel(name)['public_url']
