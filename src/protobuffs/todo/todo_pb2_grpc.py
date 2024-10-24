# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from protobuffs.todo import todo_pb2 as protobuffs_dot_todo_dot_todo__pb2

GRPC_GENERATED_VERSION = '1.67.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in protobuffs/todo/todo_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TodoServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateTodo = channel.unary_unary(
                '/todo.TodoService/CreateTodo',
                request_serializer=protobuffs_dot_todo_dot_todo__pb2.CreateTodoRequest.SerializeToString,
                response_deserializer=protobuffs_dot_todo_dot_todo__pb2.CreateTodoResponse.FromString,
                _registered_method=True)
        self.ReadTodo = channel.unary_unary(
                '/todo.TodoService/ReadTodo',
                request_serializer=protobuffs_dot_todo_dot_todo__pb2.ReadTodoRequest.SerializeToString,
                response_deserializer=protobuffs_dot_todo_dot_todo__pb2.ReadTodoResponse.FromString,
                _registered_method=True)
        self.UpdateTodo = channel.unary_unary(
                '/todo.TodoService/UpdateTodo',
                request_serializer=protobuffs_dot_todo_dot_todo__pb2.UpdateTodoRequest.SerializeToString,
                response_deserializer=protobuffs_dot_todo_dot_todo__pb2.UpdateTodoResponse.FromString,
                _registered_method=True)
        self.DeleteTodo = channel.unary_unary(
                '/todo.TodoService/DeleteTodo',
                request_serializer=protobuffs_dot_todo_dot_todo__pb2.DeleteTodoRequest.SerializeToString,
                response_deserializer=protobuffs_dot_todo_dot_todo__pb2.DeleteTodoResponse.FromString,
                _registered_method=True)
        self.ListTodos = channel.unary_unary(
                '/todo.TodoService/ListTodos',
                request_serializer=protobuffs_dot_todo_dot_todo__pb2.ListTodosRequest.SerializeToString,
                response_deserializer=protobuffs_dot_todo_dot_todo__pb2.ListTodosResponse.FromString,
                _registered_method=True)


class TodoServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateTodo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadTodo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTodo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTodo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTodos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TodoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateTodo': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTodo,
                    request_deserializer=protobuffs_dot_todo_dot_todo__pb2.CreateTodoRequest.FromString,
                    response_serializer=protobuffs_dot_todo_dot_todo__pb2.CreateTodoResponse.SerializeToString,
            ),
            'ReadTodo': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadTodo,
                    request_deserializer=protobuffs_dot_todo_dot_todo__pb2.ReadTodoRequest.FromString,
                    response_serializer=protobuffs_dot_todo_dot_todo__pb2.ReadTodoResponse.SerializeToString,
            ),
            'UpdateTodo': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTodo,
                    request_deserializer=protobuffs_dot_todo_dot_todo__pb2.UpdateTodoRequest.FromString,
                    response_serializer=protobuffs_dot_todo_dot_todo__pb2.UpdateTodoResponse.SerializeToString,
            ),
            'DeleteTodo': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTodo,
                    request_deserializer=protobuffs_dot_todo_dot_todo__pb2.DeleteTodoRequest.FromString,
                    response_serializer=protobuffs_dot_todo_dot_todo__pb2.DeleteTodoResponse.SerializeToString,
            ),
            'ListTodos': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTodos,
                    request_deserializer=protobuffs_dot_todo_dot_todo__pb2.ListTodosRequest.FromString,
                    response_serializer=protobuffs_dot_todo_dot_todo__pb2.ListTodosResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'todo.TodoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('todo.TodoService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TodoService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateTodo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/todo.TodoService/CreateTodo',
            protobuffs_dot_todo_dot_todo__pb2.CreateTodoRequest.SerializeToString,
            protobuffs_dot_todo_dot_todo__pb2.CreateTodoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ReadTodo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/todo.TodoService/ReadTodo',
            protobuffs_dot_todo_dot_todo__pb2.ReadTodoRequest.SerializeToString,
            protobuffs_dot_todo_dot_todo__pb2.ReadTodoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateTodo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/todo.TodoService/UpdateTodo',
            protobuffs_dot_todo_dot_todo__pb2.UpdateTodoRequest.SerializeToString,
            protobuffs_dot_todo_dot_todo__pb2.UpdateTodoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteTodo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/todo.TodoService/DeleteTodo',
            protobuffs_dot_todo_dot_todo__pb2.DeleteTodoRequest.SerializeToString,
            protobuffs_dot_todo_dot_todo__pb2.DeleteTodoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListTodos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/todo.TodoService/ListTodos',
            protobuffs_dot_todo_dot_todo__pb2.ListTodosRequest.SerializeToString,
            protobuffs_dot_todo_dot_todo__pb2.ListTodosResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
