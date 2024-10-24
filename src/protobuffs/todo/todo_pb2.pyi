from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TodoNotificationTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TODO_NOTIFICATION_TYPE_ENUM_UNSPECIFIED: _ClassVar[TodoNotificationTypeEnum]
    TODO_NOTIFICATION_TYPE_ENUM_OK: _ClassVar[TodoNotificationTypeEnum]
TODO_NOTIFICATION_TYPE_ENUM_UNSPECIFIED: TodoNotificationTypeEnum
TODO_NOTIFICATION_TYPE_ENUM_OK: TodoNotificationTypeEnum

class Todo(_message.Message):
    __slots__ = ("id", "name", "completed", "day")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    completed: bool
    day: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., completed: bool = ..., day: _Optional[int] = ...) -> None: ...

class CreateTodoRequest(_message.Message):
    __slots__ = ("name", "completed", "day")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    name: str
    completed: bool
    day: int
    def __init__(self, name: _Optional[str] = ..., completed: bool = ..., day: _Optional[int] = ...) -> None: ...

class CreateTodoResponse(_message.Message):
    __slots__ = ("notificatioType", "todo")
    NOTIFICATIOTYPE_FIELD_NUMBER: _ClassVar[int]
    TODO_FIELD_NUMBER: _ClassVar[int]
    notificatioType: TodoNotificationTypeEnum
    todo: Todo
    def __init__(self, notificatioType: _Optional[_Union[TodoNotificationTypeEnum, str]] = ..., todo: _Optional[_Union[Todo, _Mapping]] = ...) -> None: ...

class ReadTodoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ReadTodoResponse(_message.Message):
    __slots__ = ("todo",)
    TODO_FIELD_NUMBER: _ClassVar[int]
    todo: Todo
    def __init__(self, todo: _Optional[_Union[Todo, _Mapping]] = ...) -> None: ...

class UpdateTodoRequest(_message.Message):
    __slots__ = ("id", "name", "completed")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    completed: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., completed: bool = ...) -> None: ...

class UpdateTodoResponse(_message.Message):
    __slots__ = ("todo",)
    TODO_FIELD_NUMBER: _ClassVar[int]
    todo: Todo
    def __init__(self, todo: _Optional[_Union[Todo, _Mapping]] = ...) -> None: ...

class DeleteTodoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DeleteTodoResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ListTodosRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTodosResponse(_message.Message):
    __slots__ = ("todos",)
    TODOS_FIELD_NUMBER: _ClassVar[int]
    todos: _containers.RepeatedCompositeFieldContainer[Todo]
    def __init__(self, todos: _Optional[_Iterable[_Union[Todo, _Mapping]]] = ...) -> None: ...
