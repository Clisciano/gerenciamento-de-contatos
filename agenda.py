
# módulo para trabalhar com expressões regulares  
import re 

# função para validar o email
# Esta é uma expressão regular simples para um email.
def validar_email(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+$', email))

# função para validar o telefone
# Esta é uma expressão regular simples para um telefone.
def validar_telefone(telefone):
    return bool(re.match(r'^\d{2}-\d{5}-\d{4}$', telefone))

# função para criar um contato
def criar_contato(name, phone, email, favorite=False):
    return {
        'name': name,
        'phone': phone,
        'email': email,
        'favorite': favorite
    }
# função para adicionar um contato
def adicionar_contato(agenda, contato):
    agenda.append(contato)
    return agenda
# função para visualizar os contatos
def visualizar_contatos(agenda):
    for i, contato in enumerate(agenda, start=1 ):
       status = '✓' if contato['favorite'] else ' '
       print('Mostrando contatos cadastrados')
       print(f'\n{i}- Nome: {contato["name"]}\nTelefone: {contato["phone"]}\nEmail: {contato["email"]}\nFavorito: [{status}]')

# função para editar um contato
def editar_contato(agenda, nome):
    for contato in agenda:
        if contato['name'] == nome:
            novo_nome = input('Digite o novo nome (ou pressione Enter para manter o mesmo): ').upper()
            if novo_nome:
                contato['name'] = novo_nome.upper()
            
            novo_telefone = input('Digite o novo telefone (ou pressione Enter para manter o mesmo): ')
            if novo_telefone:
                while novo_telefone and not validar_telefone(novo_telefone):
                    print('Telefone inválido. O formato deve ser XX-XXXXX-XXXX.')
                    novo_telefone = input('Digite o novo telefone: ')
                if novo_telefone:
                    contato['phone'] = novo_telefone
            
            novo_email = input('Digite o novo email (ou pressione Enter para manter o mesmo): ')
            if novo_email:
                while novo_email and not validar_email(novo_email):
                    print('Email inválido. O formato deve ser contato@exemplo.com')
                    novo_email = input('Digite o novo email: ')
                if novo_email:
                    contato['email'] = novo_email
            print(f'Contato {nome} editado com sucesso!')
            return agenda
    print('Contato não encontrado')

# função para marcar/desmarcar um contato como favorito
def marcar_favorito(agenda, nome):
    for contato in agenda:
        if contato['name'] == nome:
            contato['favorite'] = not contato['favorite']
            print(f'Contato {nome} marcado como favorito!')
            return agenda
    print('Contato não encontrado')

# função visualizar contatos favoritos
def visualizar_favoritos(agenda):
    contador_favoritos = 1
    for contato in agenda:
        if contato['favorite']:
            print(f'\n{contador_favoritos}- Nome: {contato["name"]}\nTelefone: {contato["phone"]}\nEmail: {contato["email"]}\nFavorito: [✓]')
            contador_favoritos += 1
    if contador_favoritos == 1:
        print('Nenhum contato favorito encontrado')
    else:
        print(f'\nTotal de contatos favoritos: {contador_favoritos - 1}')
# função para apagar um contato
def apagar_contato(agenda, nome):
    for contato in agenda:
        if contato['name'] == nome:
            agenda.remove(contato)
            print(f'Contato {nome} removido com sucesso!')
            return agenda
    print('Contato não encontrado')
# criar menu de opções para o usuário
def main():
    agenda = []
    while True:
        print('\nBem-vindo a sua agenda de contatos')
        print('        Escolha uma opção:')
        print('1 - Adicionar contato')
        print('2 - Ver contatos cadastrados')
        print('3 - Editar contato')
        print('4 - Marcar/Desmarcar contato como favorito')
        print('5 - Ver lista de favoritos')
        print('6 - Apagar contato')
        print('7 - Sair')
        option = input('Escolha uma opção: ')

        if option == '1':
            name = input('Digite o nome do contato: ').upper()
            phone = input('Digite o Telefone do contato: ')
            while not validar_telefone(phone):
                print('Telefone inválido. O formato deve ser XX-XXXXX-XXXX.')
                phone = input('Digite o Telefone do contato: ')
            email = input('Digite o Email do contato: ')
            while not validar_email(email):
                print('Email inválido. O formato deve ser contato@exemplo.com.')
                email = input('Digite o Email do contato: ')
            contato = criar_contato(name, phone, email)
            adicionar_contato(agenda, contato)
        elif option == '2':
            visualizar_contatos(agenda)
        elif option == '3':
            nome = input('Digite o nome do contato que deseja editar: ').upper()
            editar_contato(agenda, nome)  
        elif option == '4':
            visualizar_contatos(agenda)
            nome = input('Digite o nome do contato que deseja marcar/desmarcar como favorito: ').upper()
            marcar_favorito(agenda, nome)
        elif option == '5':
            visualizar_favoritos(agenda)
        elif option == '6':
            visualizar_contatos(agenda)
            nome = input('Digite o nome do contato que deseja apagar: ').upper()
            apagar_contato(agenda, nome)
        elif option == '7':
            print('Até logo!')
            break

if __name__ == '__main__':
    main()