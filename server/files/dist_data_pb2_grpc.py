# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import dist_data_pb2 as dist__data__pb2

GRPC_GENERATED_VERSION = '1.66.1'
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
        + f' but the generated code in dist_data_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TrainLoaderServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTrainLoader = channel.unary_unary(
                '/dist_data.TrainLoaderService/GetTrainLoader',
                request_serializer=dist__data__pb2.TrainLoaderRequest.SerializeToString,
                response_deserializer=dist__data__pb2.TrainLoaderResponse.FromString,
                _registered_method=True)
        self.GetTestLoader = channel.unary_unary(
                '/dist_data.TrainLoaderService/GetTestLoader',
                request_serializer=dist__data__pb2.Empty.SerializeToString,
                response_deserializer=dist__data__pb2.TrainLoaderResponse.FromString,
                _registered_method=True)
        self.GetSoloLoader = channel.unary_unary(
                '/dist_data.TrainLoaderService/GetSoloLoader',
                request_serializer=dist__data__pb2.Empty.SerializeToString,
                response_deserializer=dist__data__pb2.TrainLoaderResponse.FromString,
                _registered_method=True)
        self.GetSoloTest = channel.unary_unary(
                '/dist_data.TrainLoaderService/GetSoloTest',
                request_serializer=dist__data__pb2.Empty.SerializeToString,
                response_deserializer=dist__data__pb2.TrainLoaderResponse.FromString,
                _registered_method=True)


class TrainLoaderServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTrainLoader(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTestLoader(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSoloLoader(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSoloTest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrainLoaderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTrainLoader': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTrainLoader,
                    request_deserializer=dist__data__pb2.TrainLoaderRequest.FromString,
                    response_serializer=dist__data__pb2.TrainLoaderResponse.SerializeToString,
            ),
            'GetTestLoader': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTestLoader,
                    request_deserializer=dist__data__pb2.Empty.FromString,
                    response_serializer=dist__data__pb2.TrainLoaderResponse.SerializeToString,
            ),
            'GetSoloLoader': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSoloLoader,
                    request_deserializer=dist__data__pb2.Empty.FromString,
                    response_serializer=dist__data__pb2.TrainLoaderResponse.SerializeToString,
            ),
            'GetSoloTest': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSoloTest,
                    request_deserializer=dist__data__pb2.Empty.FromString,
                    response_serializer=dist__data__pb2.TrainLoaderResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dist_data.TrainLoaderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('dist_data.TrainLoaderService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TrainLoaderService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTrainLoader(request,
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
            '/dist_data.TrainLoaderService/GetTrainLoader',
            dist__data__pb2.TrainLoaderRequest.SerializeToString,
            dist__data__pb2.TrainLoaderResponse.FromString,
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
    def GetTestLoader(request,
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
            '/dist_data.TrainLoaderService/GetTestLoader',
            dist__data__pb2.Empty.SerializeToString,
            dist__data__pb2.TrainLoaderResponse.FromString,
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
    def GetSoloLoader(request,
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
            '/dist_data.TrainLoaderService/GetSoloLoader',
            dist__data__pb2.Empty.SerializeToString,
            dist__data__pb2.TrainLoaderResponse.FromString,
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
    def GetSoloTest(request,
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
            '/dist_data.TrainLoaderService/GetSoloTest',
            dist__data__pb2.Empty.SerializeToString,
            dist__data__pb2.TrainLoaderResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
