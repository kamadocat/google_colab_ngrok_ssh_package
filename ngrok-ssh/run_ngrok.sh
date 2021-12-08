set -x
/ngrok start --config ~/.ngrok2/ngrok.yml --config /drive/ngrok-ssh/ssh.yml --log=stdout --config /drive/ngrok-ssh/tensorboard.yml --config /drive/ngrok-ssh/http8080.yml --config /drive/ngrok-ssh/tcp8080.yml --config /drive/ngrok-ssh/tpu.yml "$@"
