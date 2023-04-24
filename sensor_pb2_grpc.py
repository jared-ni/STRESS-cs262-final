# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import sensor_pb2 as sensor__pb2


class ServerStub(object):
    """service AlarmSensor {
    rpc SendData (MessageRequest) returns (Empty) {}
    }

    service WarningSensor {
    rpc SendData (MessageRequest) returns (Empty) {}
    }

    message Empty {}

    message MessageRequest {
    int32 id = 1;
    string message = 2;
    }

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Signup = channel.unary_unary(
                '/grpc.Server/Signup',
                request_serializer=sensor__pb2.SignupRequest.SerializeToString,
                response_deserializer=sensor__pb2.SignupReply.FromString,
                )
        self.Signout = channel.unary_unary(
                '/grpc.Server/Signout',
                request_serializer=sensor__pb2.SignoutRequest.SerializeToString,
                response_deserializer=sensor__pb2.SignoutReply.FromString,
                )
        self.GetTrainStatus = channel.unary_unary(
                '/grpc.Server/GetTrainStatus',
                request_serializer=sensor__pb2.TrainStatusRequest.SerializeToString,
                response_deserializer=sensor__pb2.TrainStatusResponse.FromString,
                )
        self.UpdateTrainStatus = channel.unary_unary(
                '/grpc.Server/UpdateTrainStatus',
                request_serializer=sensor__pb2.TrainUpdateRequest.SerializeToString,
                response_deserializer=sensor__pb2.TrainUpdateResponse.FromString,
                )
        self.GetOtherTrainStatus = channel.unary_unary(
                '/grpc.Server/GetOtherTrainStatus',
                request_serializer=sensor__pb2.OtherTrainStatusRequest.SerializeToString,
                response_deserializer=sensor__pb2.TrainStatusResponse.FromString,
                )
        self.SendSensorMessage = channel.unary_unary(
                '/grpc.Server/SendSensorMessage',
                request_serializer=sensor__pb2.SensorMessageRequest.SerializeToString,
                response_deserializer=sensor__pb2.SensorResponse.FromString,
                )
        self.TrainSensorStream = channel.unary_stream(
                '/grpc.Server/TrainSensorStream',
                request_serializer=sensor__pb2.TrainConnectRequest.SerializeToString,
                response_deserializer=sensor__pb2.TrainConnectReply.FromString,
                )


class ServerServicer(object):
    """service AlarmSensor {
    rpc SendData (MessageRequest) returns (Empty) {}
    }

    service WarningSensor {
    rpc SendData (MessageRequest) returns (Empty) {}
    }

    message Empty {}

    message MessageRequest {
    int32 id = 1;
    string message = 2;
    }

    """

    def Signup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Signout(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTrainStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTrainStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOtherTrainStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendSensorMessage(self, request, context):
        """sensors
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TrainSensorStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Signup': grpc.unary_unary_rpc_method_handler(
                    servicer.Signup,
                    request_deserializer=sensor__pb2.SignupRequest.FromString,
                    response_serializer=sensor__pb2.SignupReply.SerializeToString,
            ),
            'Signout': grpc.unary_unary_rpc_method_handler(
                    servicer.Signout,
                    request_deserializer=sensor__pb2.SignoutRequest.FromString,
                    response_serializer=sensor__pb2.SignoutReply.SerializeToString,
            ),
            'GetTrainStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTrainStatus,
                    request_deserializer=sensor__pb2.TrainStatusRequest.FromString,
                    response_serializer=sensor__pb2.TrainStatusResponse.SerializeToString,
            ),
            'UpdateTrainStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTrainStatus,
                    request_deserializer=sensor__pb2.TrainUpdateRequest.FromString,
                    response_serializer=sensor__pb2.TrainUpdateResponse.SerializeToString,
            ),
            'GetOtherTrainStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOtherTrainStatus,
                    request_deserializer=sensor__pb2.OtherTrainStatusRequest.FromString,
                    response_serializer=sensor__pb2.TrainStatusResponse.SerializeToString,
            ),
            'SendSensorMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendSensorMessage,
                    request_deserializer=sensor__pb2.SensorMessageRequest.FromString,
                    response_serializer=sensor__pb2.SensorResponse.SerializeToString,
            ),
            'TrainSensorStream': grpc.unary_stream_rpc_method_handler(
                    servicer.TrainSensorStream,
                    request_deserializer=sensor__pb2.TrainConnectRequest.FromString,
                    response_serializer=sensor__pb2.TrainConnectReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.Server', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Server(object):
    """service AlarmSensor {
    rpc SendData (MessageRequest) returns (Empty) {}
    }

    service WarningSensor {
    rpc SendData (MessageRequest) returns (Empty) {}
    }

    message Empty {}

    message MessageRequest {
    int32 id = 1;
    string message = 2;
    }

    """

    @staticmethod
    def Signup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.Server/Signup',
            sensor__pb2.SignupRequest.SerializeToString,
            sensor__pb2.SignupReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Signout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.Server/Signout',
            sensor__pb2.SignoutRequest.SerializeToString,
            sensor__pb2.SignoutReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTrainStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.Server/GetTrainStatus',
            sensor__pb2.TrainStatusRequest.SerializeToString,
            sensor__pb2.TrainStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTrainStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.Server/UpdateTrainStatus',
            sensor__pb2.TrainUpdateRequest.SerializeToString,
            sensor__pb2.TrainUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOtherTrainStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.Server/GetOtherTrainStatus',
            sensor__pb2.OtherTrainStatusRequest.SerializeToString,
            sensor__pb2.TrainStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendSensorMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.Server/SendSensorMessage',
            sensor__pb2.SensorMessageRequest.SerializeToString,
            sensor__pb2.SensorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TrainSensorStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpc.Server/TrainSensorStream',
            sensor__pb2.TrainConnectRequest.SerializeToString,
            sensor__pb2.TrainConnectReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
