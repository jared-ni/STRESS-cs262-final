# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensor.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0csensor.proto\x12\x04grpc\"\x07\n\x05\x45mpty\"-\n\x0eMessageRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"N\n\x17OtherTrainStatusRequest\x12\x1b\n\x13requesting_train_id\x18\x01 \x01(\x05\x12\x16\n\x0eother_train_id\x18\x02 \x01(\x05\"&\n\x12TrainStatusRequest\x12\x10\n\x08train_id\x18\x01 \x01(\x05\"H\n\x13TrainStatusResponse\x12\x10\n\x08train_id\x18\x01 \x01(\x05\x12\x10\n\x08location\x18\x02 \x01(\x01\x12\r\n\x05speed\x18\x03 \x01(\x01\"G\n\x12TrainUpdateRequest\x12\x10\n\x08train_id\x18\x01 \x01(\x05\x12\x10\n\x08location\x18\x02 \x01(\x01\x12\r\n\x05speed\x18\x03 \x01(\x01\"&\n\x13TrainUpdateResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32>\n\x0b\x41larmSensor\x12/\n\x08SendData\x12\x14.grpc.MessageRequest\x1a\x0b.grpc.Empty\"\x00\x32@\n\rWarningSensor\x12/\n\x08SendData\x12\x14.grpc.MessageRequest\x1a\x0b.grpc.Empty\"\x00\x32\xf3\x01\n\tScheduler\x12G\n\x0eGetTrainStatus\x12\x18.grpc.TrainStatusRequest\x1a\x19.grpc.TrainStatusResponse\"\x00\x12J\n\x11UpdateTrainStatus\x12\x18.grpc.TrainUpdateRequest\x1a\x19.grpc.TrainUpdateResponse\"\x00\x12Q\n\x13GetOtherTrainStatus\x12\x1d.grpc.OtherTrainStatusRequest\x1a\x19.grpc.TrainStatusResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sensor_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=22
  _EMPTY._serialized_end=29
  _MESSAGEREQUEST._serialized_start=31
  _MESSAGEREQUEST._serialized_end=76
  _OTHERTRAINSTATUSREQUEST._serialized_start=78
  _OTHERTRAINSTATUSREQUEST._serialized_end=156
  _TRAINSTATUSREQUEST._serialized_start=158
  _TRAINSTATUSREQUEST._serialized_end=196
  _TRAINSTATUSRESPONSE._serialized_start=198
  _TRAINSTATUSRESPONSE._serialized_end=270
  _TRAINUPDATEREQUEST._serialized_start=272
  _TRAINUPDATEREQUEST._serialized_end=343
  _TRAINUPDATERESPONSE._serialized_start=345
  _TRAINUPDATERESPONSE._serialized_end=383
  _ALARMSENSOR._serialized_start=385
  _ALARMSENSOR._serialized_end=447
  _WARNINGSENSOR._serialized_start=449
  _WARNINGSENSOR._serialized_end=513
  _SCHEDULER._serialized_start=516
  _SCHEDULER._serialized_end=759
# @@protoc_insertion_point(module_scope)
