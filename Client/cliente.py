import json
import grpc
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# não estava reconhecendo o pacote, então adicionei o caminho do diretório pai ao sys.path
import tarefas_pb2
import tarefas_pb2_grpc
# essa parte abaixo coloquei direto no main, como no exemplo, mas deixei comentada aqui para referência da documentação
# channel = grpc.insecure_channel('localhost:50051')
# stub = tarefas_pb2_grpc.TarefaServiceStub(channel)

TAREFAS = os.path.join(os.path.dirname(__file__), 'Tarefas')
os.makedirs(TAREFAS, exist_ok=True)

def salvarTarefaLocal(tarefaID: str, tarefa: dict) -> str:
    caminho = os.path.join(TAREFAS, f"{tarefaID}.json")
    with open(caminho, 'w', encoding='utf-8') as arquvivo:
        json.dump(tarefa, arquvivo, ensure_ascii=False, indent=4)


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
    tarefa = {
        "id": response.id,
        "nome": nome,
        "descricao": descricao,
        "status": status,
        "data_limite": data_limite,
        "responsavel": responsavel,
        "memoria": memoria,
        "cpu": cpu
    }
    caminho = salvarTarefaLocal(response.id, tarefa)
    print(f"Tarefa criada com ID: {response.id}")
     
        
def listarTarefas(stub):
    request = tarefas_pb2.Request_Listar()
    response = stub.Listar(request)
    
    if not response.tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    
    print("\nLista de Tarefas:")
    for tarefa in response.tarefas:
        print(f"\nID: {tarefa.id} \n Nome: {tarefa.nome}\n Status: {tarefa.status}\n Data Limite: {tarefa.data_limite}\n Responsável: {tarefa.responsavel}\n Memória: {tarefa.memoria}MB\n CPU: {tarefa.cpu} núcleos")
        
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
        print("Erro ao atualizar a tarefa.")
        
def deletarTarefa(stub):
    tarefaID = input("Digite o ID da tarefa que deseja deletar: ")
    caminho = os.path.join(TAREFAS, f"{tarefaID}.json")
    os.remove(caminho) if os.path.exists(caminho) else None
    request = tarefas_pb2.Request_Deletar(id=tarefaID)
    response = stub.Deletar(request)
    
    if response.deletado:
        print(f"{response.mensagem}")
    else:
        print("Erro ao deletar a tarefa.")
        
def main():
    host = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
    port = sys.argv[2] if len(sys.argv) > 2 else '50051'

    with grpc.insecure_channel(f'{host}:{port}') as channel:
        stub = tarefas_pb2_grpc.TarefaServiceStub(channel)
        
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