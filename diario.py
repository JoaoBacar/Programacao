#Acrescentar duas linhas no arquivo sem apagar o está escrito
with open('diario.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('Dia 4: aprendi a acrescentar linhas\n')
    arquivo.write('Dia 5: conclui o desafio da aula\n')
   