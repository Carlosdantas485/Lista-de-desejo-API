import requests, json,time,os

class Funcionalidades():

    def Status(self):
        
        funcao = Funcionalidades()
        funcao.lista_de_desejos()

        with open ("testa.json") as file:
            data = json.load(file)
        
        funcao.barra()
        funcao.barra()
        print("|\t\t\t\t\t DESEJA ALTERAR O STATUS DE QUAL FILME ?      \t\t\t\t\t       |")
        funcao.barra()
        funcao.barra()
        funcao.linhas()
        funcao.barra()
        funcao.barra()
        
        title_movie = str(input("|\t[ NOME DO FILME ]: ")).upper()
        
        funcao.barra()
        funcao.barra()
        
        flag = False
        for percorre in data:

            if title_movie == percorre['Titulo']:
                flag = True
                break
            else:
                pass
            
        if flag == True:

            conteudo = requests.get("http://www.omdbapi.com/?apikey=2a3afc&t={}".format(title_movie)).json()

            lista = []
            dicionario = {
            
                    'Titulo': conteudo['Title'].upper(),
                    'Ano': conteudo['Year'],
                    'Tempo De Filme': conteudo['Runtime'],
                    'Origem': conteudo['Country'],
                    'Genero': conteudo['Genre'],
                    'Idioma': conteudo['Language'],
                    'Status': ''
    
            }
    
            conteudo['Status'] = '        [ EM AGUARDO ]'
            
            lista.append(dicionario)

            funcao.linhas()
            
            os.system('clear') or None
            funcao.linhas()
            funcao.barra()
            funcao.barra()
            print("|\t\t\t\tINFORMACOES SOBRE O FILME [ {} ]". format(conteudo['Title']).upper())
            funcao.barra()
            funcao.barra()
            funcao.linhas()
            funcao.barra()
            funcao.barra()

            print('| Titulo: ',conteudo['Title'])
            print('| Ano: ',conteudo['Year'])
            print('| Tempo De Filme: ',conteudo['Runtime'])
            print('| Origem: ',conteudo['Country'])
            print('| Genero: ',conteudo['Genre'])
            print('| Idioma:', conteudo['Language'])
            print("|\t\t\tStatus: ", conteudo["Status"])
            funcao.barra()
            funcao.barra()

            funcao.printa_altera_status()

            funcao.barra()
            funcao.barra()
            print("| DIGITE [ 1 ] PARA MARCAR COMO [ ASSISTIDO ]")
            print("| DIGITE [ 2 ] PARA MARCAR COMO [ NÂO ASSISTIDO ]")
            print("| DIGITE [ 3 ] PARA MARCAR COMO [ ASSISTIR MAIS TARDE ]")
            print("| DIGITE [ 4 ] PARA MARCAR COMO [ CONTINUAR ASSISTINDO ]")
            funcao.barra()
            funcao.barra()
            funcao.linhas()
            
            Status_Optio = int(input("| →: "))

            if Status_Optio == 1:

                percorre['Status'] = '        ASSISTIDO        '
                    
                with open ("testa.json",'w') as file:
                    json.dump(data,file, indent=4)

                print(percorre['Status'])

            elif Status_Optio == 2:
                
                funcao.printa_carregando()

                funcao.linhas()
                funcao.barra()
                funcao.barra()
                print("| ")

                percorre['Status'] = '        NAO ASSISTIDO        '
                   
                with open ("testa.json",'w') as file:
                    json.dump(data,file, indent=4)

                print(percorre['Status'])

            elif Status_Optio == 3:

                percorre['Status'] = '        ASSISTIR MAIS TARDE        '
                   
                with open ("testa.json",'w') as file:
                    json.dump(data,file, indent=4)

                print(percorre['Status'])

            elif Status_Optio == 4:

                percorre['Status'] = '        CONTINUAR ASSISTINDO        '
                   
                with open ("testa.json",'w') as file:
                    json.dump(data,file, indent=4)

                print(percorre['Status'])
        else:
            pass

    def lista_de_desejos(self):
        funcao = Funcionalidades()
        with open("testa.json") as file:
            lista = json.load(file)

            for contador in  lista:

                funcao.barra()    
                funcao.barra()    
                print('|\t\t\tTitulo: ',contador['Titulo'])
                print('|\t\t\tAno: ',contador['Ano'])
                print('|\t\t\tTempo De Filme: ',contador['Tempo De Filme'])
                print('|\t\t\tOrigem: ',contador['Origem'])
                print('|\t\t\tGenero: ',contador['Genero'])
                print('|\t\t\tIdioma:', contador['Idioma'])
                print("|\t\t\tStatus: ", contador["Status"])
                funcao.barra()
                funcao.barra()
                funcao.linhas()
        
    def barra(self):
        
        print("|                                                                                                                              |")

    def linhas(self):

        print("|IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII|")

    def deleta_filme(self):
        funcao = Funcionalidades()
        
        funcao.lista_de_desejos()

        funcao.barra()
        funcao.barra()
        title_movie = str(input("| →: \t\tDIGITE O NOME DO FILME: ")).upper().strip()

        with open('testa.json') as file:
            data = json.load(file)

        flag = True
        lista = []

        for percorre in data:

            if title_movie == percorre['Titulo']:
                flag = False
                print("COMPAROU")
            else:
                print("NAO COMPAROU")
                pass
            
        if flag == False:
            for percorre in data:
                if title_movie != percorre['Titulo']:

                    lista.append(percorre)

            with open('testa.json','w') as file:
                json.dump(lista, file, indent=4)

                funcao.printa_carregando()

                os.system('clear') or None
                funcao.linhas()
                funcao.barra()    
                funcao.barra()  
                print("|\t\t\t\tFILME DELETADO")
                funcao.barra()
                funcao.barra()
                funcao.linhas()
                time.sleep(4)

        else:
            pass
    
    def printa_opcao_invalida(self):
        funcao = Funcionalidades()

        funcao.barra()
        funcao.barra()
        print("|\t\t\t\t\t[ OPÇÂO INVALIDA TENTE NOVAMENTE ]           \t\t\t\t\t       |")
        funcao.barra()
        funcao.barra()

    def printa_menu(self):
        funcao = Funcionalidades()
        
        funcao.linhas()
        funcao.barra()
        print("| \t\t\t\t\t\t\t[ MENU ]\t\t\t\t\t\t\t       |")
        funcao.barra()
        funcao.linhas()
        funcao.barra()
        funcao.barra()
        print("| Digite [ 1 ] PARA ADICIONAR UM FILME NA LISTA DE DESEJOS       \t\t\t\t\t\t\t       |")
        print("| Digite [ 2 ] MOSTRAR SUA LISTA DE DESEJOS                      \t\t\t\t\t\t\t       |")
        print("| Digite [ 3 ] PARA ALTERAR O STATUS DE UM FILME DA SUA LISTA    \t\t\t\t\t\t\t       |")
        print("| Digite [ 4 ] PARA DELETAR UM FILME DA LISTA DE DESEJOS         \t\t\t\t\t\t\t       |") 
        print("| Digite [ 0 ] [ SAIR ]                                          \t\t\t\t\t\t\t       |")
        funcao.barra()
        funcao.barra()
        funcao.linhas()
        funcao.barra()

    def printa_escolher_add(self):
        funcao = Funcionalidades()

        funcao.linhas()
        funcao.barra()
        print("|\t\t\t\t\t[ VOCÊ ESCOLHEU A OPÇÂO ADICIONAR FILME ]              \t\t\t\t       |")
        funcao.barra()
        funcao.linhas()
        funcao.barra()
        funcao.barra()

    def printa_filme_inexistente(self):

        funcao = Funcionalidades()

        funcao.linhas()
        funcao.barra()
        funcao.barra()
        print("|\t\t\t\t\t\tESTE FILME NAO EXISTE       \t\t\t\t\t\t       |")
        funcao.barra()
        funcao.barra()
        funcao.linhas()
        funcao.barra() 
        funcao.barra()
    
    def printa_ja_esta_na_lista(self):
        funcao = Funcionalidades()

        funcao.linhas()
        funcao.barra()
        funcao.barra()
        print('|\t\t\t\t\t[ ESTE FILME JA ESTA EM SUA LISTA DE DESEJOS  ]      \t\t\t               |')
        funcao.barra()
        funcao.barra()
    
    def printa_menu_outro_filme(self):
        funcao = Funcionalidades()

        print("| [ 1 ] - PARA BUSCAR OUTRO FILME")
        print("| [ 0 ] - PARA VOLTAR AO MENU")
        funcao.barra()
        funcao.barra()
        funcao.linhas()
        funcao.barra()
        funcao.barra()

    def printa_menu_ou_add(self):
        funcao = Funcionalidades()
        
        funcao.linhas()
        funcao.barra()
        funcao.barra()
        print("| DIGITE [ 1 ] - PARA ADICIONAR ESTE FILME NA SUA LISTA DE DESEJOS  \t\t\t\t\t\t\t       |")
        print("| DIGITE [ 0 ] - PARA VOLTAR AO MENU PRINCIPAL                      \t\t\t\t\t\t\t       |")
        funcao.barra()
        funcao.barra()
        funcao.linhas()
        funcao.barra()
        funcao.barra()

    def printa_menu_lista_desejos(self):
        funcao = Funcionalidades()
        
        funcao.linhas()
        funcao.barra()
        print("|\t\t\t\t\t[ SUA LISTA DE DESEJO ]              \t\t\t\t\t\t       |")
        funcao.barra()
        funcao.linhas()
        funcao.barra()

    def print_voltar_menu(self):
        funcao = Funcionalidades()

        funcao.linhas()
        funcao.barra()
        funcao.barra()
        print("| [ 1 ] - PARA VOLTAR AO MENU     \t\t\t\t\t\t\t\t\t\t\t       |")
        funcao.barra()
        funcao.barra()
        funcao.linhas()
        funcao.barra()
        funcao.barra()

    def printa_adicionado(self):
        funcao = Funcionalidades()

        funcao.printa_carregando()

        os.system('clear') or None
        funcao.linhas()
        funcao.barra()
        funcao.barra()
        print('|\t\t\t\t\t\t   [ ADICIONANDO ]     \t\t\t\t\t\t\t       |')
        funcao.barra()
        funcao.barra()
        funcao.linhas()
        time.sleep(3)

    def printa_altera_status(self):
        funcao = Funcionalidades()

        funcao.linhas()
        funcao.barra()
        funcao.barra()
        print("|\t\t\t\t\t\t PARA QUAL STATUS ?      \t\t\t\t\t       |")
        funcao.barra()
        funcao.barra()
        funcao.linhas()
        
    def printa_carregando(self):
        funcao = Funcionalidades()

        os.system('clear') or None
        funcao.linhas()
        funcao.barra()
        funcao.barra()
        print("| \t\t\t\t\t\t[ Loading... █▒▒▒▒▒▒▒▒▒ 0%]")
        funcao.barra()
        funcao.barra()
        funcao.linhas()
        time.sleep(0.5)
        
        os.system('clear') or None
        funcao.linhas()
        funcao.barra()
        funcao.barra()
        print("| \t\t\t\t\t\t[ Loading... ███▒▒▒▒▒▒▒ 10%] *")
        funcao.barra()
        funcao.barra()
        funcao.linhas()
        time.sleep(0.5)
        
        os.system('clear') or None
        funcao.linhas()
        funcao.barra()
        funcao.barra()
        print("| \t\t\t\t\t\t[ Loading... █████▒▒▒▒▒ 30%] * *")
        funcao.barra()
        funcao.barra()
        funcao.linhas()
        time.sleep(0.5)
        
        os.system('clear') or None
        funcao.linhas()
        funcao.barra()
        funcao.barra()
        print("| \t\t\t\t\t\t[ Loading... ███████▒▒▒ 60%] * * *")
        funcao.barra()
        funcao.barra()
        funcao.linhas()
        time.sleep(0.5)
        
        os.system('clear') or None
        funcao.linhas()
        funcao.barra()
        funcao.barra()
        print("| \t\t\t\t\t\t[ Loading... ██████████ 100%] * * *")
        funcao.barra()
        funcao.barra()
        funcao.linhas() 
        os.system('clear') or None  
    
    def agradecimento(self):
        funcao = Funcionalidades()
        for i in range (0,3):    
            
            os.system('clear') or None
            funcao.linhas()
            funcao.barra()
            funcao.barra()
            print("| \t\t\t\t\t****[ GUILUFLIX AGRADECE PELO TEU ACESSO ]****")
            funcao.barra()
            funcao.barra()
            funcao.linhas()
            time.sleep(0.1)

            os.system('clear') or None
            funcao.linhas()
            funcao.barra()
            funcao.barra()
            print("| \t\t\t\t\t ***[ GUILUFLIX AGRADECE PELO TEU ACESSO ]***")
            funcao.barra()
            funcao.barra()
            funcao.linhas()
            time.sleep(0.1)

            os.system('clear') or None
            funcao.linhas()
            funcao.barra()
            funcao.barra()
            print("| \t\t\t\t\t  **[ GUILUFLIX AGRADECE PELO TEU ACESSO ]**")
            funcao.barra()
            funcao.barra()
            funcao.linhas()
            time.sleep(0.1)

            os.system('clear') or None
            funcao.linhas()
            funcao.barra()
            funcao.barra()
            print("| \t\t\t\t\t   *[ GUILUFLIX AGRADECE PELO TEU ACESSO ]*")
            funcao.barra()
            funcao.barra()
            funcao.linhas()
            time.sleep(0.1)


            os.system('clear') or None
            funcao.linhas()
            funcao.barra()
            funcao.barra()
            print("| \t\t\t\t\t    [ GUILUFLIX AGRADECE PELO TEU ACESSO ]")
            funcao.barra()
            funcao.barra()
            funcao.linhas()
            time.sleep(0.1)







