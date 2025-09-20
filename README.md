# 🧠 Projeto: Engenharia de Software e IA

Este projeto foi desenvolvido em **Python** e faz uso do **Ollama** (um servidor local de modelos de linguagem) para realizar interações como **chat** e **geração de texto**.

---

## 👥 Integrantes

- [Giulliano Lucas](https://github.com/giulms)
- [Gustavo Lino](https://github.com/GustavoLino728)
- [Italo Artur](https://github.com/ItaloVasconcelos05)
- [Pedro Fernandes](https://github.com/fernandes-pedro)
- [Rayanne Falcão](https://github.com/rayannefalcaoo)

---

## 🚀 Como rodar o projeto

Siga os passos abaixo para configurar o ambiente e executar a aplicação.

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

### 2️⃣ Instalar o Ollama
O Ollama é o motor de IA que executa os modelos de linguagem localmente.

Windows ou macOS:
Baixe e instale a versão compatível no site oficial: Ollama Download

Linux:
Execute no terminal:

```bash
curl -fsSL https://ollama.com/install.sh | sh

### 3️⃣ Baixar o modelo Llama 3
Após instalar o Ollama, baixe o modelo necessário:

```bash

ollama run llama3
(Esse processo pode levar alguns minutos.)

### 4️⃣ Criar e ativar o ambiente virtual
Crie o ambiente virtual:

```bash

python -m venv .venv
Ative o ambiente virtual:

Windows (PowerShell):

```bash

.venv\Scripts\Activate
Linux ou macOS:

```bash

source .venv/bin/activate
### 5️⃣ Instalar as dependências
Com o ambiente virtual ativado, instale os pacotes necessários:

```bash
pip install -r requirements.txt

### 6️⃣ Executar a aplicação
Abra um terminal e inicie o servidor do Ollama (mantenha-o aberto):

```bash

ollama serve
Em um segundo terminal, ative o ambiente virtual e rode o script principal:

```bash
Copiar código
# Ativar ambiente virtual (exemplo para Windows)
.venv\Scripts\Activate

# Executar o projeto
python main.py