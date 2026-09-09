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
        
    def Listar(self, request, context):
    
    def Atualizar(self, request, context):
    
    def Deletar(self, request, context):

    def serve():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
        tarefas_pb2_grpc.add_TarefaServiceServicer_to_server(TarefaService(), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        print("Servidor gRPC na port 50051.")
        server.wait_for_termination()