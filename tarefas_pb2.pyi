from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class STATUS(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGUARDANDO: _ClassVar[STATUS]
    PROCESSANDO: _ClassVar[STATUS]
    FINALIZADA: _ClassVar[STATUS]
AGUARDANDO: STATUS
PROCESSANDO: STATUS
FINALIZADA: STATUS

class Tarefa(_message.Message):
    __slots__ = ("id", "nome", "descricao", "status", "data_limite", "responsavel", "memoria", "cpu")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_LIMITE_FIELD_NUMBER: _ClassVar[int]
    RESPONSAVEL_FIELD_NUMBER: _ClassVar[int]
    MEMORIA_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    id: str
    nome: str
    descricao: str
    status: STATUS
    data_limite: str
    responsavel: str
    memoria: int
    cpu: int
    def __init__(self, id: _Optional[str] = ..., nome: _Optional[str] = ..., descricao: _Optional[str] = ..., status: _Optional[_Union[STATUS, str]] = ..., data_limite: _Optional[str] = ..., responsavel: _Optional[str] = ..., memoria: _Optional[int] = ..., cpu: _Optional[int] = ...) -> None: ...

class Request_Criar(_message.Message):
    __slots__ = ("nome", "descricao", "status", "data_limite", "responsavel", "memoria", "cpu")
    NOME_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_LIMITE_FIELD_NUMBER: _ClassVar[int]
    RESPONSAVEL_FIELD_NUMBER: _ClassVar[int]
    MEMORIA_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    nome: str
    descricao: str
    status: STATUS
    data_limite: str
    responsavel: str
    memoria: int
    cpu: int
    def __init__(self, nome: _Optional[str] = ..., descricao: _Optional[str] = ..., status: _Optional[_Union[STATUS, str]] = ..., data_limite: _Optional[str] = ..., responsavel: _Optional[str] = ..., memoria: _Optional[int] = ..., cpu: _Optional[int] = ...) -> None: ...

class Request_Listar(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Lista(_message.Message):
    __slots__ = ("tarefas",)
    TAREFAS_FIELD_NUMBER: _ClassVar[int]
    tarefas: _containers.RepeatedCompositeFieldContainer[Tarefa]
    def __init__(self, tarefas: _Optional[_Iterable[_Union[Tarefa, _Mapping]]] = ...) -> None: ...

class Request_Atualizar(_message.Message):
    __slots__ = ("id", "nome", "descricao", "status", "data_limite", "responsavel", "memoria", "cpu")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_LIMITE_FIELD_NUMBER: _ClassVar[int]
    RESPONSAVEL_FIELD_NUMBER: _ClassVar[int]
    MEMORIA_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    id: str
    nome: str
    descricao: str
    status: STATUS
    data_limite: str
    responsavel: str
    memoria: int
    cpu: int
    def __init__(self, id: _Optional[str] = ..., nome: _Optional[str] = ..., descricao: _Optional[str] = ..., status: _Optional[_Union[STATUS, str]] = ..., data_limite: _Optional[str] = ..., responsavel: _Optional[str] = ..., memoria: _Optional[int] = ..., cpu: _Optional[int] = ...) -> None: ...

class Request_Deletar(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class Delete(_message.Message):
    __slots__ = ("deletado", "mensagem")
    DELETADO_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    deletado: bool
    mensagem: str
    def __init__(self, deletado: _Optional[bool] = ..., mensagem: _Optional[str] = ...) -> None: ...
