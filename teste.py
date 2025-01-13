import json

    
def criar_credenciais():    
    with open("credenciais.json","w") as file:
        file.writelines()
    
usua = input()
palavra = input()

a = {
    "User": f"{usua}",
    "Password": f"{palavra}"
}

with open("credenciais.json","w") as file:
    json.dumps(file)

file = a

print(a)


