🔐 Login Automa-o

Automação em Python que abre o navegador e faz login automaticamente em dois sistemas web, eliminando a tarefa manual e repetitiva de digitar credenciais todos os dias.

⚙️ O que faz
- Abre o Microsoft Edge diretamente nas páginas dos sistemas
- Preenche CPF e senha usando PyAutoGUI
- Lê as credenciais de variáveis de ambiente (.env), sem deixá-las expostas no código
- Inclui um utilitário (coordenadas.py) para descobrir as coordenadas do mouse na sua tela


🛠️ Tecnologias utilizadas
Python
PyAutoGUI
python-dotenv
subprocess (biblioteca padrão)

📁 Estrutura do projeto

login-automa-o/
├── main.py          # Script principal: abre o navegador e faz o login
├── coordenadas.py   # Utilitário para descobrir coordenadas do mouse
├── .env             
├── .env.example     # Modelo do arquivo .env
└── .gitignore


▶️ Como usar

1. Clone o repositório

bash
git clone https://github.com/miguelmiada/login-automa-o.git
cd login-automa-o

2. Instale as dependências

bash
pip install pyautogui python-dotenv

3. Configure as credenciais

Crie um arquivo .env na raiz do projeto, seguindo o modelo do .env.example:

CPF=
SENHA=
CPF_SEI=
SENHA_SEI=

4. Ajuste as coordenadas para a sua tela

As posições de clique dependem da resolução do monitor. Rode o utilitário e anote as coordenadas dos campos de login:

bash
python coordenadas.py

Depois atualize os valores de x, y no main.py.

5. Execute a automação

bash
python main.py

Para interromper a qualquer momento, leve o mouse rapidamente até o canto superior esquerdo da tela (recurso fail-safe do PyAutoGUI).

⚠️ Limitações conhecidas

Depende de coordenadas de tela fixas, então pode falhar em outra resolução ou com o navegador em outra posição
Configurado para Windows e Microsoft Edge (o caminho do executável está definido no main.py)
Usa pausas fixas (sleep) em vez de esperar o carregamento real das páginas

 
👤 Autor

Miguel Miada 
