- Instalação e ativação do ambiente virtual Python3
```sh
sudo apt update
sudo apt install python3 virtualenv
virtualenv -p /usr/bin/python3 .venv
. .venv/bin/activate
```

- [Instalação errbot](http://errbot.io/en/latest/user_guide/setup.html#installation):

-Configuração para o errbot subir com o 'systemd'
sudo vi /etc/systemd/system/errbot.service
sudo systemctl daemon-reload
sudo systemctl restart errbot

- [Criar bot no Telegram](https://core.telegram.org/bots#3-how-do-i-create-a-bot):

- Alterações nos arquivos de configuração
Arquivo config.py
BOT_ADMINS ('@CHANGE_ME",) para BOT_ADMINS = ()
BANKEND = 'TEXT' para BACKEND = 'Telegram'
BOT_IDENTITY = {'TOKEN DO BOT'}
