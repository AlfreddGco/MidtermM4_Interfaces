# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import interfases_pb2 as interfases__pb2


class LocationTrackerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getCoordinate = channel.unary_unary(
                '/Interfases.LocationTracker/getCoordinate',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=interfases__pb2.Coordinate.FromString,
                )


class LocationTrackerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getCoordinate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LocationTrackerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getCoordinate': grpc.unary_unary_rpc_method_handler(
                    servicer.getCoordinate,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=interfases__pb2.Coordinate.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Interfases.LocationTracker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LocationTracker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getCoordinate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Interfases.LocationTracker/getCoordinate',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            interfases__pb2.Coordinate.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
