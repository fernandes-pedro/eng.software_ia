# Projeto: Engenharia de Software e IA

Este projeto foi desenvolvido em **Python** e faz uso do **Ollama** (um servidor local de modelos de linguagem) para realizar interações como **chat** e **geração de texto**.

---

## 👥 Integrantes

- [Giulliano Lucas](https://github.com/GiullianoLucas)
- [Gustavo Lino](https://github.com/GustavoLino)
- [Italo Artur](https://github.com/ItaloArtur)
- [Pedro Fernandes](https://github.com/PedroFernandes)
- [Rayanne Falcão](https://github.com/RayanneFalcao)

---

## 🚀 Como rodar o projeto (passo a passo)

Para executar o projeto, siga estes passos para configurar o ambiente e as dependências necessárias.

### 1. Clonar o repositório

Abra seu terminal e clone este projeto para sua máquina:

```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio
2. Instalar o Ollama
O Ollama é o motor de IA que executa os modelos de linguagem localmente. Baixe e instale a versão compatível com seu sistema operacional no site oficial.

Windows ou macOS: Acesse o site oficial do Ollama para baixar o instalador: https://ollama.com/download

Linux: Use o terminal para instalar o Ollama com o seguinte comando:

Bash

curl -fsSL [https://ollama.com/install.sh](https://ollama.com/install.sh) | sh
3. Baixar o modelo Llama 3
Depois de instalar o Ollama, você precisa baixar o modelo de linguagem que o projeto utiliza. Abra um novo terminal e execute o comando abaixo. Este processo pode levar alguns minutos.

Bash

ollama run llama3
4. Criar e ativar o ambiente virtual
Para evitar conflitos entre as dependências, é uma boa prática usar um ambiente virtual para o projeto.

Criar o ambiente virtual:

Bash

python -m venv .venv
Ativar o ambiente virtual:

Windows (PowerShell):

Bash

.venv\Scripts\Activate
Linux ou macOS:

Bash

source .venv/bin/activate
5. Instalar as dependências do Python
Com o ambiente virtual ativado, instale as bibliotecas necessárias para o projeto.

Bash

pip install -r requirements.txt
6. Executar a aplicação
Para rodar o projeto, você precisa iniciar o servidor do Ollama em uma porta disponível e, em seguida, executar o script principal.

Abra um terminal e inicie o servidor do Ollama. Mantenha este terminal aberto durante a execução.

Bash

ollama serve
Abra um segundo terminal, ative o ambiente virtual novamente e execute o script Python do projeto.

Bash

# Ative o ambiente (exemplo para Windows)
.venv\Scripts\Activate

# Execute o script
python main.py
O resultado da execução, com as interações de chat e geração de texto, será exibido diretamente no seu terminal.