# O comando para criação deste ambiente isolado é python3 -m venv .venv, sendo
# que .venv é o nome do ambiente isolado. Este comando deve ser
# executado na raiz do projeto.

'python3 -m venv .venv'

# Caso o venv não esteja instalado, utilize o comando:

'sudo apt install python3-venv'

# comando para ativar o ambiente virtual:

'source .venv/bin/activate'

# Você pode conferir se o comando de ativação do ambiente virtual
# deu certo com o seguinte comando:

'which python3'

# O resultado será o caminho para a pasta onde você criou seu
# ambiente virtual (pwd), acrescido de .venv/bin/python3
