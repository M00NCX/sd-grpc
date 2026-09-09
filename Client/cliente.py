import grpc
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# não estava reconhecendo o pacote, então adicionei o caminho do diretório pai ao sys.path
import tarefas_pb2
import tarefas_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = tarefas_pb2_grpc.TarefaServiceStub(channel)

def criarTarefa(stub):
    nome = input("Digite o nome da tarefa: ")
    descricao = input("Digite a descrição: ")
    status = tarefas_pb2.STATUS.AGUARDANDO
    data_limite = input("Digite a data limite: ")
    responsavel = input("Digite o responsável: ")
    memoria = int(input("Digite a quantidade de memória necessária (em MB): "))
    cpu = int(input("Digite a quantidade de CPU necessária (em núcleos): "))

    request = tarefas_pb2.Request_Criar(
        nome=nome,
        descricao=descricao,
        status=status,
        data_limite=data_limite,
        responsavel=responsavel,
        memoria=memoria,
        cpu=cpu
    )

    response = stub.Criar(request)
    print(f"Tarefa criada com ID: {response.id}")
    
def listarTarefas(stub):
    request = tarefas_pb2.Request_Listar()
    response = stub.Listar(request)
    
    if not response.tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    
    print("Lista de Tarefas:")
    for tarefa in response.tarefas:
        print(f"ID: {tarefa.id}, Nome: {tarefa.nome}, Status: {tarefa.status.name(tarefa.status)}, Data Limite: {tarefa.data_limite}, Responsável: {tarefa.responsavel}, Memória: {tarefa.memoria}MB, CPU: {tarefa.cpu} núcleos")
        
def atualizarTarefa(stub):
    tarefaID = input("Digite o ID da tarefa que deseja atualizar: ")
    nome = input("Digite o novo nome da tarefa: ")
    descricao = input("Digite a nova descrição da tarefa: ")
    status = int(input("Digite o novo status da tarefa (0: AGUARDANDO, 1: PROCESSANDO, 2: FINALIZADA): "))
    data_limite = input("Digite a nova data limite: ")
    responsavel = input("Digite o novo responsável pela tarefa: ")
    memoria = int(input("Digite a nova quantidade de memória necessária (em MB): "))
    cpu = int(input("Digite a nova quantidade de CPU necessária (em núcleos): "))

    request = tarefas_pb2.Request_Atualizar(
        id=tarefaID,
        nome=nome,
        descricao=descricao,
        status=status,
        data_limite=data_limite,
        responsavel=responsavel,
        memoria=memoria,
        cpu=cpu
    )

    response = stub.Atualizar(request)
    
    if response.id:
        print(f"Tarefa atualizada com sucesso: {response.id}")
    else:
        print("Erro ao atualizar a tarefa. Verifique se o ID está correto.")
        
def deletarTarefa(stub):
    tarefaID = input("Digite o ID da tarefa que deseja deletar: ")
    
    request = tarefas_pb2.Request_Deletar(id=tarefaID)
    response = stub.Deletar(request)
    
    if response.id:
        print(f"Tarefa deletada com sucesso: {response.id}")
    else:
        print("Erro ao deletar a tarefa.")
        
def main():
        
    while True:
        print("\nEscolha uma opção:")
        print("1. Criar Tarefa")
        print("2. Listar Tarefas")
        print("3. Atualizar Tarefa")
        print("4. Deletar Tarefa")
        print("5. Sair")
        
        escolha = input("Digite o número da opção desejada: ")
        
        if escolha == '1':
            criarTarefa(stub)
        elif escolha == '2':
            listarTarefas(stub)
        elif escolha == '3':
            atualizarTarefa(stub)
        elif escolha == '4':
            deletarTarefa(stub)
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")
                
if __name__ == '__main__':
    main()