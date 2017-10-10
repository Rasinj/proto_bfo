### Example of things

This is an attempt to translate the BFO structure to protobuf, in order to allow for dynamic transformation and extension of it. 

## Goals:
* The mid-term goal is to have a formal mechanism for reasoning about spatial and temporal entities.
* Reducing the verbosity of qualitatively identical objects will allow for a more succinct way of expressing knowledge.
* Allowing for rapid development of new subject ontologies
* Allowing for transfer of general algorithms by using similar behaviour of the underlying objects.

### List of things to do

* Transfer the complete definition of BFO to basic protobuf definitions
* [Entity]
* [Continuant]
* [Occurrent]

#### Entity
Contains

* A term
* A repeated subentity

### Level 0

#### Continuant
An object that persists over time

Contains:

* Description

#### Occurrent
A temporal entity with continuant participants

Contains:

* Description
* Participating continuants

Examples:

>     import Occurrent
>     occurrent = Occurrent(description = 'example', participants = [Entity1, Entity2])
>     occurrent.find_similar_occurrents()

### Level 1

#### Process
An occurrent that unfolds over a certain time interval

Contains:

* Description
* Start time
* End time

Basic Examples:

>     import Process
>     import Continuant
>     me = Continuant(snr = '123092039')
>     occurrent = Process(description = 'life', participants = Me, start_time = st, end_time = None)
>     occurrent.start_time

Advanced Examples:

>     # Find entities existing at overlapping temporal regions
>     overlapping_processes = occurrent.find(lambda (x,y): x∩y and y.decription == life)
>     print(overlapping_processes[0])
>     >>> Process(decription = 'life', participants = Continuant(...))

Application Examples:

>     # Instantiate health processes
>     import health_process_similarity
>     health_process = Process(description = 'MESH://D010612', participants = Continuant(snr = '12329929'))
>     health_process.find_similar_processes(similarity_algorithm = health_process_similarity) 

Here, a health_process_similarity algorithm would have dependencies on deeper qualities within the continuants and/or processes which make up the health process. For example, it could perform

>     # Infer the process type by stepping up in an external ontology hierarchy
>     process_type = health_process.infer_process_type()
>     print(process_type)
>     >>> 'disease_condition'
>     my_disease_processes = health_process.participants.participation_in_processses_of_type(process_type)

#### Process boundary
An occurrent that manifests at a specified time

Contains

* Time stamp

Basic examples:

>     process_boundary = ProcessBoundary(description = 'Fall of Berlin wall', time_stamp = datetime(1989,11,09))
>     # Find process boundaries manifested at neighboring temporal regions
>     nearby_process_boundaries = process_boundary.find_nearby()


#### Generically dependent continuant
An information containing continuant, not dependent on a preserved continuant bearer

#### Specifically dependent continuant
A quality-containing continuant, which depends on preserved continuant bearer

Something that depends_on a certain instance of an independent continuant

Contains:

#### Independent continuant
An independent continuant

Such as an object, a person, a thing with a specified boundary
