import os
if 'COLAB_TPU_ADDR' in os.environ:
  with open('/drive/ngrok-ssh/tpu.yml', 'w') as f:
    f.write("""
tunnels:
  tpu:
    proto: tcp
    addr: {}
""".format(os.environ['COLAB_TPU_ADDR']).strip())
  print('Wrote /drive/ngrok-ssh/tpu.yml')
