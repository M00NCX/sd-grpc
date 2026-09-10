# Projeto gRPC – Gerenciador de Tarefas com Vagrant e VirtualBox

Criar um sistema de gerenciamento de tarefas simples, com um serviço central (servidor gRPC) e uma aplicação cliente que o consome.

| Máquina  | IP            | Função                             | Comando principal                     |
| -------- | ------------- | ---------------------------------- | ------------------------------------- |
| servidor | 192.168.56.10 | Servidor gRPC e estado das tarefas | python3 server.py                     |
| cliente1 | 192.168.56.11 | Cliente gRPC                       | python3 client.py 192.168.56.10 50051 |
| cliente2 | 192.168.56.12 | Cliente gRPC                       | python3 client.py 192.168.56.10 50051 |

# Pré-requisitos

- VirtualBox instalado e funcionando;
- Vagrant instalado e disponível no terminal (comando vagrant);
- Projeto grpc-tarefas com o Vagrantfile na raiz;
- Conexão com a Internet durante a criação/provisionamento das VMs;
- Espaço livre suficiente no disco usado pelo Vagrant e pelo VirtualBox.

# Inicialização das VMs

No terminal do Windows, entre na pasta raiz do projeto e faça:

```
vagrant status
vagrant up
vagrant ssh servidor
python3 server.py
vagrant ssh cliente1
python3 client.py 192.168.56.10 50051
ping 192.168.56.10
```

# Resultado esperado

Ao final da configuração, devem existir três VMs em execução e comunicação por uma rede privada: servidor (192.168.56.10), cliente1 (192.168.56.11) e cliente2 (192.168.56.12). O servidor deve escutar na porta 50051 e os dois clientes devem conseguir executar operações sobre as tarefas. A criação de uma tarefa em um cliente e sua visualização em outro constitui a principal evidência de que o estado está centralizado no servidor gRPC.
