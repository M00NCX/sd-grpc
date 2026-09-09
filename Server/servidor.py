import grpc
import uuid
from concurrent import futures
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tarefas_pb2
import tarefas_pb2_grpc
MAX_WORKERS = 10

tarefas = {}

class TarefaService(tarefas_pb2_grpc.TarefaServiceServicer):

    def Criar(self, request, context):
        id = str(uuid.uuid4())
        tarefa = tarefas_pb2.Tarefa(
            id=id,
            nome=request.nome,
            descricao=request.descricao,
            status=request.status,
            data_limite=request.data_limite,
            responsavel=request.responsavel,
            memoria=request.memoria,
            cpu=request.cpu,
        )
        tarefas[id] = tarefa
        return tarefa

    def Listar(self, request, context):
        return tarefas_pb2.Lista(tarefas=list(tarefas.values()))

    def Atualizar(self, request, context):
        if request.id not in tarefas:
            return tarefas_pb2.Tarefa()
        tarefa = tarefas_pb2.Tarefa(
            id=request.id,
            nome=request.nome,
            descricao=request.descricao,
            status=request.status,
            data_limite=request.data_limite,
            responsavel=request.responsavel,
            memoria=request.memoria,
            cpu=request.cpu,
        )
        tarefas[request.id] = tarefa
        return tarefa

    def Deletar(self, request, context):
        if request.id in tarefas:
            del tarefas[request.id]
            return tarefas_pb2.Delete(deletado=True, mensagem="Tarefa deletada com sucesso")
        return tarefas_pb2.Delete(deletado=False, mensagem="Tarefa nao encontrada")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
    tarefas_pb2_grpc.add_TarefaServiceServicer_to_server(TarefaService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC na porta 50051.")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()