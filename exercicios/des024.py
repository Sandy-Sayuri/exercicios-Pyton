#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cid= str(input('em que cidade você naceu? ')).strip()
print(cid[:5].upper()=='SANTO')