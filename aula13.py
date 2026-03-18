nome="Paulo Pelisser"     #F strings é uma maneira de busca a facilitar 
altura=1.80               # f'{} coloque a informção q vc quer 
peso=95 
imc=peso/(altura**2)

linha_1=f'{nome} tem {altura:.2f} de altura' #formata as casas decimais usando :. quatas casas vc quer f
linha_2=f"{peso} quilos"
linha_3=f"{peso/(altura**2)} é o imc do Paulo"

print(linha_1)
print(linha_2)
print(linha_3)