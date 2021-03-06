# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import exampleservice_pb2 as exampleservice__pb2


class FridayServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ItsFriday = channel.unary_unary(
                '/com.eventbrite.grpckotlintutorial.FridayService/ItsFriday',
                request_serializer=exampleservice__pb2.ItsFridayRequest.SerializeToString,
                response_deserializer=exampleservice__pb2.ItsFridayResponse.FromString,
                )


class FridayServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ItsFriday(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FridayServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ItsFriday': grpc.unary_unary_rpc_method_handler(
                    servicer.ItsFriday,
                    request_deserializer=exampleservice__pb2.ItsFridayRequest.FromString,
                    response_serializer=exampleservice__pb2.ItsFridayResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.eventbrite.grpckotlintutorial.FridayService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FridayService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ItsFriday(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.eventbrite.grpckotlintutorial.FridayService/ItsFriday',
            exampleservice__pb2.ItsFridayRequest.SerializeToString,
            exampleservice__pb2.ItsFridayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
