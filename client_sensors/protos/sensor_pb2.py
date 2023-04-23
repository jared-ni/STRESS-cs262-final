# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sensor.proto',
  package='grpc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0csensor.proto\x12\x04grpc\"\'\n\x13TrainConnectRequest\x12\x10\n\x08train_id\x18\x01 \x01(\x05\"E\n\x11TrainConnectReply\x12\x10\n\x08train_id\x18\x01 \x01(\x05\x12\r\n\x05\x61larm\x18\x02 \x01(\x08\x12\x0f\n\x07message\x18\x03 \x01(\t\"B\n\x14SensorMessageRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x61larm\x18\x02 \x01(\x08\x12\x0f\n\x07message\x18\x03 \x01(\t\"D\n\x0eSensorResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x15\n\rerror_message\x18\x03 \x01(\t\"N\n\x17OtherTrainStatusRequest\x12\x1b\n\x13requesting_train_id\x18\x01 \x01(\x05\x12\x16\n\x0eother_train_id\x18\x02 \x01(\x05\"&\n\x12TrainStatusRequest\x12\x10\n\x08train_id\x18\x01 \x01(\x05\"H\n\x13TrainStatusResponse\x12\x10\n\x08train_id\x18\x01 \x01(\x05\x12\x10\n\x08location\x18\x02 \x01(\x01\x12\r\n\x05speed\x18\x03 \x01(\x01\"G\n\x12TrainUpdateRequest\x12\x10\n\x08train_id\x18\x01 \x01(\x05\x12\x10\n\x08location\x18\x02 \x01(\x01\x12\r\n\x05speed\x18\x03 \x01(\x01\"&\n\x13TrainUpdateResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\x86\x03\n\x06Server\x12G\n\x0eGetTrainStatus\x12\x18.grpc.TrainStatusRequest\x1a\x19.grpc.TrainStatusResponse\"\x00\x12J\n\x11UpdateTrainStatus\x12\x18.grpc.TrainUpdateRequest\x1a\x19.grpc.TrainUpdateResponse\"\x00\x12Q\n\x13GetOtherTrainStatus\x12\x1d.grpc.OtherTrainStatusRequest\x1a\x19.grpc.TrainStatusResponse\"\x00\x12G\n\x11SendSensorMessage\x12\x1a.grpc.SensorMessageRequest\x1a\x14.grpc.SensorResponse\"\x00\x12K\n\x11TrainSensorStream\x12\x19.grpc.TrainConnectRequest\x1a\x17.grpc.TrainConnectReply\"\x00\x30\x01\x62\x06proto3'
)




_TRAINCONNECTREQUEST = _descriptor.Descriptor(
  name='TrainConnectRequest',
  full_name='grpc.TrainConnectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='train_id', full_name='grpc.TrainConnectRequest.train_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=61,
)


_TRAINCONNECTREPLY = _descriptor.Descriptor(
  name='TrainConnectReply',
  full_name='grpc.TrainConnectReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='train_id', full_name='grpc.TrainConnectReply.train_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alarm', full_name='grpc.TrainConnectReply.alarm', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='grpc.TrainConnectReply.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=132,
)


_SENSORMESSAGEREQUEST = _descriptor.Descriptor(
  name='SensorMessageRequest',
  full_name='grpc.SensorMessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='grpc.SensorMessageRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alarm', full_name='grpc.SensorMessageRequest.alarm', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='grpc.SensorMessageRequest.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=200,
)


_SENSORRESPONSE = _descriptor.Descriptor(
  name='SensorResponse',
  full_name='grpc.SensorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='grpc.SensorResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='success', full_name='grpc.SensorResponse.success', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='grpc.SensorResponse.error_message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=270,
)


_OTHERTRAINSTATUSREQUEST = _descriptor.Descriptor(
  name='OtherTrainStatusRequest',
  full_name='grpc.OtherTrainStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='requesting_train_id', full_name='grpc.OtherTrainStatusRequest.requesting_train_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='other_train_id', full_name='grpc.OtherTrainStatusRequest.other_train_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=350,
)


_TRAINSTATUSREQUEST = _descriptor.Descriptor(
  name='TrainStatusRequest',
  full_name='grpc.TrainStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='train_id', full_name='grpc.TrainStatusRequest.train_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=352,
  serialized_end=390,
)


_TRAINSTATUSRESPONSE = _descriptor.Descriptor(
  name='TrainStatusResponse',
  full_name='grpc.TrainStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='train_id', full_name='grpc.TrainStatusResponse.train_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='grpc.TrainStatusResponse.location', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speed', full_name='grpc.TrainStatusResponse.speed', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=392,
  serialized_end=464,
)


_TRAINUPDATEREQUEST = _descriptor.Descriptor(
  name='TrainUpdateRequest',
  full_name='grpc.TrainUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='train_id', full_name='grpc.TrainUpdateRequest.train_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='grpc.TrainUpdateRequest.location', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speed', full_name='grpc.TrainUpdateRequest.speed', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=466,
  serialized_end=537,
)


_TRAINUPDATERESPONSE = _descriptor.Descriptor(
  name='TrainUpdateResponse',
  full_name='grpc.TrainUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='grpc.TrainUpdateResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=539,
  serialized_end=577,
)

DESCRIPTOR.message_types_by_name['TrainConnectRequest'] = _TRAINCONNECTREQUEST
DESCRIPTOR.message_types_by_name['TrainConnectReply'] = _TRAINCONNECTREPLY
DESCRIPTOR.message_types_by_name['SensorMessageRequest'] = _SENSORMESSAGEREQUEST
DESCRIPTOR.message_types_by_name['SensorResponse'] = _SENSORRESPONSE
DESCRIPTOR.message_types_by_name['OtherTrainStatusRequest'] = _OTHERTRAINSTATUSREQUEST
DESCRIPTOR.message_types_by_name['TrainStatusRequest'] = _TRAINSTATUSREQUEST
DESCRIPTOR.message_types_by_name['TrainStatusResponse'] = _TRAINSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['TrainUpdateRequest'] = _TRAINUPDATEREQUEST
DESCRIPTOR.message_types_by_name['TrainUpdateResponse'] = _TRAINUPDATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrainConnectRequest = _reflection.GeneratedProtocolMessageType('TrainConnectRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRAINCONNECTREQUEST,
  '__module__' : 'sensor_pb2'
  # @@protoc_insertion_point(class_scope:grpc.TrainConnectRequest)
  })
_sym_db.RegisterMessage(TrainConnectRequest)

TrainConnectReply = _reflection.GeneratedProtocolMessageType('TrainConnectReply', (_message.Message,), {
  'DESCRIPTOR' : _TRAINCONNECTREPLY,
  '__module__' : 'sensor_pb2'
  # @@protoc_insertion_point(class_scope:grpc.TrainConnectReply)
  })
_sym_db.RegisterMessage(TrainConnectReply)

SensorMessageRequest = _reflection.GeneratedProtocolMessageType('SensorMessageRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENSORMESSAGEREQUEST,
  '__module__' : 'sensor_pb2'
  # @@protoc_insertion_point(class_scope:grpc.SensorMessageRequest)
  })
_sym_db.RegisterMessage(SensorMessageRequest)

SensorResponse = _reflection.GeneratedProtocolMessageType('SensorResponse', (_message.Message,), {
  'DESCRIPTOR' : _SENSORRESPONSE,
  '__module__' : 'sensor_pb2'
  # @@protoc_insertion_point(class_scope:grpc.SensorResponse)
  })
_sym_db.RegisterMessage(SensorResponse)

OtherTrainStatusRequest = _reflection.GeneratedProtocolMessageType('OtherTrainStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _OTHERTRAINSTATUSREQUEST,
  '__module__' : 'sensor_pb2'
  # @@protoc_insertion_point(class_scope:grpc.OtherTrainStatusRequest)
  })
_sym_db.RegisterMessage(OtherTrainStatusRequest)

TrainStatusRequest = _reflection.GeneratedProtocolMessageType('TrainStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRAINSTATUSREQUEST,
  '__module__' : 'sensor_pb2'
  # @@protoc_insertion_point(class_scope:grpc.TrainStatusRequest)
  })
_sym_db.RegisterMessage(TrainStatusRequest)

TrainStatusResponse = _reflection.GeneratedProtocolMessageType('TrainStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRAINSTATUSRESPONSE,
  '__module__' : 'sensor_pb2'
  # @@protoc_insertion_point(class_scope:grpc.TrainStatusResponse)
  })
_sym_db.RegisterMessage(TrainStatusResponse)

TrainUpdateRequest = _reflection.GeneratedProtocolMessageType('TrainUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRAINUPDATEREQUEST,
  '__module__' : 'sensor_pb2'
  # @@protoc_insertion_point(class_scope:grpc.TrainUpdateRequest)
  })
_sym_db.RegisterMessage(TrainUpdateRequest)

TrainUpdateResponse = _reflection.GeneratedProtocolMessageType('TrainUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRAINUPDATERESPONSE,
  '__module__' : 'sensor_pb2'
  # @@protoc_insertion_point(class_scope:grpc.TrainUpdateResponse)
  })
_sym_db.RegisterMessage(TrainUpdateResponse)



_SERVER = _descriptor.ServiceDescriptor(
  name='Server',
  full_name='grpc.Server',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=580,
  serialized_end=970,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTrainStatus',
    full_name='grpc.Server.GetTrainStatus',
    index=0,
    containing_service=None,
    input_type=_TRAINSTATUSREQUEST,
    output_type=_TRAINSTATUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateTrainStatus',
    full_name='grpc.Server.UpdateTrainStatus',
    index=1,
    containing_service=None,
    input_type=_TRAINUPDATEREQUEST,
    output_type=_TRAINUPDATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetOtherTrainStatus',
    full_name='grpc.Server.GetOtherTrainStatus',
    index=2,
    containing_service=None,
    input_type=_OTHERTRAINSTATUSREQUEST,
    output_type=_TRAINSTATUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendSensorMessage',
    full_name='grpc.Server.SendSensorMessage',
    index=3,
    containing_service=None,
    input_type=_SENSORMESSAGEREQUEST,
    output_type=_SENSORRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TrainSensorStream',
    full_name='grpc.Server.TrainSensorStream',
    index=4,
    containing_service=None,
    input_type=_TRAINCONNECTREQUEST,
    output_type=_TRAINCONNECTREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVER)

DESCRIPTOR.services_by_name['Server'] = _SERVER

# @@protoc_insertion_point(module_scope)
