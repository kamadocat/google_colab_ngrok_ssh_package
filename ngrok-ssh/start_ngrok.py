import os
if 'COLAB_TPU_ADDR' in os.environ:
  get_ipython().system_raw('bash /drive/ngrok-ssh/run_ngrok.sh ssh tensorboard tcp8080 tpu &')
else:
  get_ipython().system_raw('bash /drive/ngrok-ssh/run_ngrok.sh ssh tensorboard tcp8080 &')
