from proto.compiled import bfo_pb2
from proto_composite import bfo_compile_definitions
import time
## As an example, we can instantiate a continuant and an occurrent, and say that the continuant participates in the
## occurrent
exampleContinuant = bfo_pb2.Continuant()
exampleContinuant.description = 'arnold'

exampleOccurrent = bfo_pb2.Occurrent();    
exampleOccurrent.description = 'method_transfer' 
exampleOccurrent.datetime.seconds = int(time.time())

participants = exampleOccurrent.participants.add()
participants.CopyFrom(exampleContinuant) 

print(exampleOccurrent)

## An instantiated example with a process
exampleProcess = bfo_pb2.Process();    
exampleProcess.description = 'method_transfer' 
st = exampleProcess.start_process_boundary.timestamp.seconds = int(time.time())
exampleProcess.end_process_boundary.timestamp.seconds  = st + 100 

participants = exampleProcess.participants.add()
participants.CopyFrom(exampleContinuant) 

print(exampleProcess)

##
exampleSpatioTemporalRegion = bfo_pb2.SpatioTemporalRegion();    
exampleSpatioTemporalRegion.description = 'example_st_region' 
exampleSpatioTemporalRegion.temporal_region.start_timestamp.seconds = 120
exampleSpatioTemporalRegion.temporal_region.end_timestamp.seconds = 140
exampleSpatioTemporalRegion.spatial_region.description = 'example_s_region'
exampleSpatioTemporalRegion.spatial_region.placeholder_spatialregiondata = 'placeholder'
print(exampleSpatioTemporalRegion)

history = bfo_pb2.History()
history.description = 'example_history'
history.participant.CopyFrom(exampleContinuant) 
history.spatiotemporal_region.CopyFrom(exampleSpatioTemporalRegion) 
print(history)


