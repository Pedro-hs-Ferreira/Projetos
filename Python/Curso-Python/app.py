import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True}, 
                {'nome':'Cantina', 'categoria':'Italiana', 'ativo':False}]

 
def exibir_nome_programa():
    print(''' 

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
''')
def exibir_opçoes():
    '''Essa função é responsável pela escolha das opções'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar Estado Do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função é responsável por finalizar o programa'''
    exbibir_subtitulo('Finalizando app')


def voltar_ao_menu_principal():
    input('\n Digite uma tecla para voltar ao menu principal ')
    main()

def exbibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def opçao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()
    
def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs: ('Digite o nome do restaurante que deseja cadastrar:')
            (f'Diite o nome da categoria do restaurante {nome_restaurante}:')
    
    Outputs: Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exbibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    
    voltar_ao_menu_principal()


def listar_restaurantes():
    '''Essa função é responsável por fazer uma lista de todos os restaurantes e falar os nomes, categorias e status deles'''
    exbibir_subtitulo ('Listando restaurantes')
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado' 
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    '''Essa função é responsável por alternar os estado do restaurante entre ativo e desativado
 
    Outputs: Exibe mensagem indicando o sucesso da operção 
    
    '''
    exbibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante ['ativo'] = not restaurante ['ativo']
            mensagem = f'O {nome_restaurante} foi ativado com sucesso!' if restaurante ['ativo'] else f'O restaurante {'nome_do_restaurante'} foi desativado com sucesso!'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O resturante não foi encontrado')
    
    
    
    voltar_ao_menu_principal()


def escolher_opçao():
    try:
        opçao_escolhida = int (input('Escolha uma opção:'))
        # opçao_escolhida = int(opçao_escolhida)

        if opçao_escolhida == 1:
            cadastrar_novo_restaurante()    
        elif opçao_escolhida == 2:
            listar_restaurantes()
        elif opçao_escolhida == 3:
            alternar_estado_restaurante()
        elif opçao_escolhida == 4:
            finalizar_app()        
        else:
            opçao_invalida()
    except:
        opçao_invalida()



    
def main():
    os.system('cls')
    exibir_nome_programa()    
    exibir_opçoes()    
    escolher_opçao()    
        
if __name__ == '__main__':
        main()
        