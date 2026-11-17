from crud import *
def exibir_menu():
    print("\n" + "=" * 30)
    print("       SISTEMA DE CADASTRO")
    print("=" * 30)
    print("1 - Cadastrar Pessoa")
    print("2 - Listar Pessoas")
    print("3 - Atualizar Pessoa")
    print("4 - Excluir Pessoa")
    print("5 - Buscar por nome")
    print("0 - Sair")
    print("=" * 30)

def main():
    
    # cadastro_em_massa() # Execute apenas uma vez.
    
    if not criar_banco():
        print("Algum problema aconteceu ")
        raise SystemExit
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()
        
        match opcao:
            case "1":   # cadastrar pessoa
                if not Cadastrar_Pessoa():
                    print("\n[ERRO] nao foi possivel cadastrar pessoa..")
            
            case "2":   # listar pessoa
                if not Listar_Pessoas():
                    print("\n[ERRO] nao foi possivel fazer a listagem..")
            
            case "3":   # atualizar pessoa
                if not Atualizar_Pessoa():
                    print("\n[ERRO] nao foi possivel atualizar..")
            
            case "4":   # excluir pesssoa
                if not Excluir_Pessoa():
                    print("\n[ERRO] nao foi possivel concluir a exclusao..")
            
            case "5":   # buscar nome
                if not Buscar_por_nome():
                    print("\n[ERRO] nao foi possivel fazer a busca...")
                    
            case "0":   # sair
                print("\n Encerrando sistema..")
                break
                    
            
            case _:
                print("![ERROR]! opcao invalida, escolha uma opcao valida.")    
        input("pressione [ENTER] para continuar...")   

if __name__ == "__main__":
    main()