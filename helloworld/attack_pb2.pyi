from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HelloRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class HelloReply(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class ReadyRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ReadyReply(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class N(_message.Message):
    __slots__ = ["N"]
    N_FIELD_NUMBER: _ClassVar[int]
    N: int
    def __init__(self, N: _Optional[int] = ...) -> None: ...

class SoldiersPosition(_message.Message):
    __slots__ = ["soldiers"]
    SOLDIERS_FIELD_NUMBER: _ClassVar[int]
    soldiers: int
    def __init__(self, soldiers: _Optional[int] = ...) -> None: ...
