# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: protobuffs/todo/todo.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'protobuffs/todo/todo.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aprotobuffs/todo/todo.proto\x12\x04todo\"@\n\x04Todo\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tcompleted\x18\x03 \x01(\x08\x12\x0b\n\x03\x64\x61y\x18\x04 \x01(\x04\"A\n\x11\x43reateTodoRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tcompleted\x18\x02 \x01(\x08\x12\x0b\n\x03\x64\x61y\x18\x03 \x01(\x04\"g\n\x12\x43reateTodoResponse\x12\x37\n\x0fnotificatioType\x18\x01 \x01(\x0e\x32\x1e.todo.TodoNotificationTypeEnum\x12\x18\n\x04todo\x18\x02 \x01(\x0b\x32\n.todo.Todo\"\x1d\n\x0fReadTodoRequest\x12\n\n\x02id\x18\x01 \x01(\x04\",\n\x10ReadTodoResponse\x12\x18\n\x04todo\x18\x01 \x01(\x0b\x32\n.todo.Todo\"@\n\x11UpdateTodoRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tcompleted\x18\x03 \x01(\x08\".\n\x12UpdateTodoResponse\x12\x18\n\x04todo\x18\x01 \x01(\x0b\x32\n.todo.Todo\"\x1f\n\x11\x44\x65leteTodoRequest\x12\n\n\x02id\x18\x01 \x01(\x04\"%\n\x12\x44\x65leteTodoResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x12\n\x10ListTodosRequest\".\n\x11ListTodosResponse\x12\x19\n\x05todos\x18\x01 \x03(\x0b\x32\n.todo.Todo*k\n\x18TodoNotificationTypeEnum\x12+\n\'TODO_NOTIFICATION_TYPE_ENUM_UNSPECIFIED\x10\x00\x12\"\n\x1eTODO_NOTIFICATION_TYPE_ENUM_OK\x10\x01\x32\xc9\x02\n\x0bTodoService\x12?\n\nCreateTodo\x12\x17.todo.CreateTodoRequest\x1a\x18.todo.CreateTodoResponse\x12\x39\n\x08ReadTodo\x12\x15.todo.ReadTodoRequest\x1a\x16.todo.ReadTodoResponse\x12?\n\nUpdateTodo\x12\x17.todo.UpdateTodoRequest\x1a\x18.todo.UpdateTodoResponse\x12?\n\nDeleteTodo\x12\x17.todo.DeleteTodoRequest\x1a\x18.todo.DeleteTodoResponse\x12<\n\tListTodos\x12\x16.todo.ListTodosRequest\x1a\x17.todo.ListTodosResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protobuffs.todo.todo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TODONOTIFICATIONTYPEENUM']._serialized_start=605
  _globals['_TODONOTIFICATIONTYPEENUM']._serialized_end=712
  _globals['_TODO']._serialized_start=36
  _globals['_TODO']._serialized_end=100
  _globals['_CREATETODOREQUEST']._serialized_start=102
  _globals['_CREATETODOREQUEST']._serialized_end=167
  _globals['_CREATETODORESPONSE']._serialized_start=169
  _globals['_CREATETODORESPONSE']._serialized_end=272
  _globals['_READTODOREQUEST']._serialized_start=274
  _globals['_READTODOREQUEST']._serialized_end=303
  _globals['_READTODORESPONSE']._serialized_start=305
  _globals['_READTODORESPONSE']._serialized_end=349
  _globals['_UPDATETODOREQUEST']._serialized_start=351
  _globals['_UPDATETODOREQUEST']._serialized_end=415
  _globals['_UPDATETODORESPONSE']._serialized_start=417
  _globals['_UPDATETODORESPONSE']._serialized_end=463
  _globals['_DELETETODOREQUEST']._serialized_start=465
  _globals['_DELETETODOREQUEST']._serialized_end=496
  _globals['_DELETETODORESPONSE']._serialized_start=498
  _globals['_DELETETODORESPONSE']._serialized_end=535
  _globals['_LISTTODOSREQUEST']._serialized_start=537
  _globals['_LISTTODOSREQUEST']._serialized_end=555
  _globals['_LISTTODOSRESPONSE']._serialized_start=557
  _globals['_LISTTODOSRESPONSE']._serialized_end=603
  _globals['_TODOSERVICE']._serialized_start=715
  _globals['_TODOSERVICE']._serialized_end=1044
# @@protoc_insertion_point(module_scope)
