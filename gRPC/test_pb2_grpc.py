# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import test_pb2 as test__pb2


class get_configStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Login_info = channel.unary_unary(
                '/get_config.get_config/Login_info',
                request_serializer=test__pb2.Request.SerializeToString,
                response_deserializer=test__pb2.Reply.FromString,
                )


class get_configServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Login_info(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_get_configServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Login_info': grpc.unary_unary_rpc_method_handler(
                    servicer.Login_info,
                    request_deserializer=test__pb2.Request.FromString,
                    response_serializer=test__pb2.Reply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'get_config.get_config', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class get_config(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Login_info(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/get_config.get_config/Login_info',
            test__pb2.Request.SerializeToString,
            test__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)