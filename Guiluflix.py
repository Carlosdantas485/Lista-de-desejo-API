import requests,json, time, os
from funçoes import Funcionalidades

def My_program(): 

    os.system('clear') 
    funcao = Funcionalidades()
    
    funcao.printa_menu()

    option_menu = (input("| →: "))

    funcao.barra()
    funcao.linhas()
    

    if option_menu == '1':

        flag = True
        while flag:
            
            os.system('clear') 
            
            funcao.printa_escolher_add()
            
            title_movie = (input("| →: \t DIGITE O NOME DO FILME: ")).upper().strip()

            conteudo = requests.get("http://www.omdbapi.com/?apikey=2a3afc&t={}".format(title_movie)).json() 

            if conteudo['Response'] == 'False':
                
                funcao.printa_filme_inexistente()    

                flag = True 
                while flag:
                    

                    option_voltar = (input("| →: "))

                    if option_voltar == '1':

                        flag = False

                    elif option_voltar == '0':

                        My_program()
            
                    else:
                        funcao.printa_opcao_invalida()
                        flag = True
        
            else:

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
                dicionario['Status'] = '        [ EM AGUARDO ]'
                
                lista.append(dicionario)

                os.system('clear') 
                funcao.linhas()
                
                print("|")
                print("|\t\t\t\tINFORMACOES SOBRE O FILME [ {} ]". format(conteudo['Title']).upper())
                print("|")
                print('| Titulo: ',conteudo['Title'])
                print('| Ano: ',conteudo['Year'])
                print('| Tempo De Filme: ',conteudo['Runtime'])
                print('| Origem: ',conteudo['Country'])
                print('| Genero: ',conteudo['Genre'])
                print('| Idioma:', conteudo['Language'])
                print("|")
                print("|")
                
                flag = True
        
                while flag:
                
                    funcao.printa_menu_ou_add()
        
                    option_menu_ou_add = (input("| →: "))
                    funcao.barra()
        
                    if option_menu_ou_add == '1':
                    
                        try:
                        
                            with open ("testa.json") as file:
                                data = json.load(file) 

                                for percorre in data:

                                    if dicionario["Titulo"] == percorre["Titulo"]:
                                        
                                        os.system('clear') 
                                        
                                        funcao.printa_ja_esta_na_lista()
                                    
                                        #essa flag volta para onde o usuario digita o nome do filme 
                                        flag = True
                                        while flag:
                                            
                                            funcao.print_voltar_menu()

                                            option_voltar = (input("| →: "))

                                            if option_voltar == '1':
                                                
                                                My_program()

                                            else:
                                                
                                                funcao.printa_opcao_invalida()
                                                My_program()

                                    else:

                                        data.append(dicionario) #apenda no json o dicionario
        
                                        with open("testa.json", "w") as file:
                                            json.dump(data, file, indent=4) 

                                            os.system('clear') 

                                            funcao.printa_adicionado()
                                        
                                        flag = False    
                                        os.system('clear') 
                                        My_program()
            
                        except FileNotFoundError:
                            
                            flag = True
                            while flag:
                                    
                                if option_menu_ou_add == '1':
                                
                                    with open("testa.json", "w") as file:
                                        json.dump(lista, file, indent=4) 

                                    os.system('clear') 
                                    
                                    funcao.printa_adicionado()

                                    os.system('clear') 
                                    My_program()
        
                                elif option_menu_ou_add == '0':
                                
                                    My_program()
        
                                else:
                                
                                    funcao.printa_opcao_invalida()
                                    flag = True
        
                    elif option_menu_ou_add == '0':
                        
                        os.system('clear') 
                        My_program()
        
                        flag = False
        
                    else:
                        
                        os.system('clear') 
                        funcao.linhas()
                        funcao.barra()
                        funcao.printa_opcao_invalida()
                        flag = True
    
    elif option_menu == '2':
        os.system('clear') 
        try:
            
            with open ('testa.json') as file:
                data = json.load(file)
            funcao.printa_carregando()

            funcao.printa_menu_lista_desejos()

            funcao.lista_de_desejos()

        except EnvironmentError:

            os.system('clear') 

            print("nao tem nada ")
            time.sleep(4)

            os.system('clear') 

        flag = True
        while flag:

            funcao.barra()
            funcao.barra()
            funcao.print_voltar_menu()

            sair = (input("| →: "))

            if sair == '1':

                os.system('clear') 
            
                My_program()
            else:

                funcao.printa_opcao_invalida()
                
                flag = True
        
    elif option_menu == '3':
        
        os.system('clear') 
        
        funcao.printa_altera_status()
        
        funcao.Status()

        os.system('clear')      
        My_program()

    elif option_menu == '4':
    
        funcao.printa_menu_lista_desejos()
        funcao.deleta_filme()

        os.system('clear')  
        My_program()
    
    elif option_menu == '0':
        
        funcao.agradecimento()
        exit()

    else:
        os.system('clear') 

        funcao.linhas()
        funcao.printa_opcao_invalida()
        funcao.linhas()
        time.sleep(3)

        os.system('clear') 
        My_program()

My_program()