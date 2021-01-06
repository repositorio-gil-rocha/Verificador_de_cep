

def main():
    import requests
    print('|-------------------------------------|')
    print('| ---------- Consulta CEP ----------  |')
    print('|-------------------------------------|')
    print('')



    
    cep_input = input('Digite o CEP para a consulta: ')
    print('') 

    if len(cep_input) != 8:
        print('Quantidade de digitos inválida!')
        exit()

    requests = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))
    retorno_cep = requests.json()

    if 'erro' not in retorno_cep:
        print(' * CEP Encontrado com sucesso * ')
        print('CEP: ',retorno_cep['cep'])
        print('Rua: ',retorno_cep['logradouro'])
        print('Nairro: ',retorno_cep['bairro'])
        print('Estado: ',retorno_cep['uf'])
        print('')

        #print(requests.json())
    else:
        print('CEP inválido!')

    option = int(input('Deseja realizar um nova consulta? \n 1. Sim \n 2. Não \n'))
    if option == 1:
        main()
    else:
        print('Saindo...')

if __name__ == '__main__':
    main()
        
