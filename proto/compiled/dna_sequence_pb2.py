# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dna_sequence.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dna_sequence.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x12\x64na_sequence.proto\",\n\x08sequence\x12 \n\x0bnucleotides\x18\x01 \x03(\x0e\x32\x0b.nucleotide*(\n\nnucleotide\x12\x05\n\x01\x41\x10\x00\x12\x05\n\x01T\x10\x01\x12\x05\n\x01\x43\x10\x02\x12\x05\n\x01G\x10\x03\x62\x06proto3')
)

_NUCLEOTIDE = _descriptor.EnumDescriptor(
  name='nucleotide',
  full_name='nucleotide',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='A', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='T', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='G', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=68,
  serialized_end=108,
)
_sym_db.RegisterEnumDescriptor(_NUCLEOTIDE)

nucleotide = enum_type_wrapper.EnumTypeWrapper(_NUCLEOTIDE)
A = 0
T = 1
C = 2
G = 3



_SEQUENCE = _descriptor.Descriptor(
  name='sequence',
  full_name='sequence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nucleotides', full_name='sequence.nucleotides', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=66,
)

_SEQUENCE.fields_by_name['nucleotides'].enum_type = _NUCLEOTIDE
DESCRIPTOR.message_types_by_name['sequence'] = _SEQUENCE
DESCRIPTOR.enum_types_by_name['nucleotide'] = _NUCLEOTIDE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

sequence = _reflection.GeneratedProtocolMessageType('sequence', (_message.Message,), dict(
  DESCRIPTOR = _SEQUENCE,
  __module__ = 'dna_sequence_pb2'
  # @@protoc_insertion_point(class_scope:sequence)
  ))
_sym_db.RegisterMessage(sequence)


# @@protoc_insertion_point(module_scope)
