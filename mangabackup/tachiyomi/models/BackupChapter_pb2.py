# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BackupChapter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x42\x61\x63kupChapter.proto\"\xc6\x01\n\rBackupChapter\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tscanlator\x18\x03 \x01(\t\x12\x0c\n\x04read\x18\x04 \x01(\x08\x12\x10\n\x08\x62ookmark\x18\x05 \x01(\x08\x12\x14\n\x0clastPageRead\x18\x06 \x01(\x05\x12\x11\n\tdateFetch\x18\x07 \x01(\x03\x12\x12\n\ndateUpload\x18\x08 \x01(\x03\x12\x15\n\rchapterNumber\x18\t \x01(\x02\x12\x13\n\x0bsourceOrder\x18\n \x01(\x05\x62\x06proto3')



_BACKUPCHAPTER = DESCRIPTOR.message_types_by_name['BackupChapter']
BackupChapter = _reflection.GeneratedProtocolMessageType('BackupChapter', (_message.Message,), {
  'DESCRIPTOR' : _BACKUPCHAPTER,
  '__module__' : 'BackupChapter_pb2'
  # @@protoc_insertion_point(class_scope:BackupChapter)
  })
_sym_db.RegisterMessage(BackupChapter)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BACKUPCHAPTER._serialized_start=24
  _BACKUPCHAPTER._serialized_end=222
# @@protoc_insertion_point(module_scope)