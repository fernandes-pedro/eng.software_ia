import ollama

print("--- Exemplo 1: Modo de Chat ---")

client = ollama.Client(host='http://localhost:11434') 

model_name = 'llama3.2'

try:
    client.list()
    print(f"Modelo '{model_name}' está disponível localmente. Preparando para o chat...")
except Exception as e:
    print(f"Erro ao conectar ao Ollama ou modelo não disponível. Certifique-se de que o Ollama está rodando e que o modelo '{model_name}' foi baixado.")
    print(f"Para baixar, execute no terminal: 'ollama run {model_name}'")
    exit()

response = client.chat(model=model_name, messages=[
    {'role': 'user', 'content': 'Qual a capital do Brasil?'},
])

print("Resposta do Llama 3:")
print(response['message']['content'])

print("\n--- Exemplo 2: Modo de Geração ---")

prompt_de_geracao = "Crie um cenário de apocalipse causado por plantas tomando conta do mundo."

response_gen = client.generate(model=model_name, prompt=prompt_de_geracao)

print("História gerada:")
print(response_gen['response'])