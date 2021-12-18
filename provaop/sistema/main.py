from controladores.controlador_producao import Controladorproducao

def main():

    controladorproducao = Controladorproducao()
    controladorproducao.cadastrar_producao("22", "Roupa", "129")
    controladorproducao.atualizar_producao(1, "25", "utensílios")
    controladorproducao.excluir_producao(1)
    todos = controladorproducao.buscar_todos_producao()
    print(todos)
    producao = controladorproducao.buscar_producao_por_cod("22")
    print(producao)
    controladorproducao.verificar_producao_preco("129")

main()
