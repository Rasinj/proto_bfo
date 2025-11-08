from python import bfo_definitions
print(examplebfo)
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

