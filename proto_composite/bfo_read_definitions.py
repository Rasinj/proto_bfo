from proto.compiled import bfo_pb2
import time

## This describes the typical way to construct Entities
examplebfo = bfo_pb2.Entity()
with open('defs_compiled.bin',"rb") as f:
    examplebfo.ParseFromString(f.read())
