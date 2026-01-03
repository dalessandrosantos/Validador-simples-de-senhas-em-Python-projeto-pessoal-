def main():
    # Somando tentativas de senha inválida e válida
    tot_senha_inv = tot_senha_val = 0

    while True:
        # Entrada do usuário
        senha_usu = input('Digite sua senha: ').replace(' ', '')

        # Validando se senha tem menos de 6 caracteres
        if len(senha_usu) < 6:
            print(f'A senha {senha_usu} deve possuir no mínimo 6 caracteres')
            tot_senha_inv += 1
        else:
            print(f'A senha {senha_usu} é válida')
            tot_senha_val += 1

        # Perguntando se deseja continuar (valida S/N)
        while True:
            resp = input('Deseja continuar? [S/N]').strip().upper()
            if resp in ('S', 'N'):
                break
            print('Opção inválida. Digite apenas S ou N.')

        if resp == 'N':
            break

    print('Programa encerrado!')
    print(f'Senhas válidas: {tot_senha_val}')
    print(f'Senhas inválidas: {tot_senha_inv}')

if __name__ == '__main__':
    main()
