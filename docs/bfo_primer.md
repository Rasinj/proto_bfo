# Basic Formal Ontology (BFO) Primer

## Introduction

Basic Formal Ontology (BFO) is a top-level ontology designed to support information integration, retrieval, and analysis across all domains of scientific investigation. This primer introduces the core concepts of BFO and how they are represented in Protocol Buffers.

## Core Distinctions

### Entity

The most general category. Every existing thing is an entity.

```protobuf
message Entity {
    string term = 1;
    repeated Entity sub_entity = 2;
}
```

### Continuant vs. Occurrent

BFO makes a fundamental distinction between:

**Continuants** - Entities that persist through time and can be wholly present at any point in time
- Examples: a person, a cell, a building, a quality
- Properties: Has spatial location, endures through time

**Occurrents** - Entities that unfold over time and have temporal parts
- Examples: a process, an event, a life
- Properties: Has temporal extent, cannot be wholly present at a single time point

```protobuf
message Continuant {
    string description = 1;
}

message Occurrent {
    string description = 1;
    repeated Continuant participants = 2;
    google.protobuf.Timestamp datetime = 3;
}
```

## Continuant Categories

### Independent Continuant
Entities that exist independently and do not require other entities to exist.

#### Material Entity
Physical objects with mass
- **Object**: Maximally self-connected material entities (e.g., a person, an organism)
- **Fiat Object Part**: Parts of objects defined by convention (e.g., upper half of a building)
- **Object Aggregate**: Collections of objects (e.g., a flock of birds)

```protobuf
message MaterialEntity {
    Continuant continuant = 1;
}
```

#### Immaterial Entity
Spatial regions or boundaries without mass
- **Spatial Region**: Regions of space
- **Site**: Spatial regions occupied by material entities
- **Continuant Fiat Boundary**: Boundaries defined by convention (e.g., political borders)

```protobuf
message ImmaterialEntity {
    Continuant continuant = 1;
}
```

### Dependent Continuant

Entities that depend on other continuants for their existence.

#### Specifically Dependent Continuant

**Quality**: Properties that inhere in exactly one bearer
- Examples: the color of an apple, the mass of a person, the temperature of a solution

```protobuf
message Quality {
    Continuant continuant = 1;
}
```

**Realizable Entity**: Properties that can be realized in processes
- **Role**: Realizable entities that depend on external circumstances (e.g., being a teacher)
- **Disposition**: Realizable entities that are intrinsic (e.g., fragility, solubility)
- **Function**: Dispositions that exist because of selection (e.g., the function of a heart)

```protobuf
message Role {
    Continuant continuant = 1;
}

message Disposition {
    Continuant continuant = 1;
}
```

**Relational Quality**: Qualities that relate two or more entities

```protobuf
message RelationalQuality {
    string description = 1;
    Continuant relational_receiver = 2;
    Continuant relational_giver = 3;
    bool invert_relation = 4;
}
```

#### Generically Dependent Continuant
Information content entities that can have multiple bearers
- Examples: a PDF document, a gene sequence, a pattern

## Occurrent Categories

### Process
An occurrent that has temporal parts and unfolds over time

```protobuf
message Process {
    string description = 1;
    repeated Continuant participants = 2;
    ProcessBoundary start_process_boundary = 3;
    ProcessBoundary end_process_boundary = 4;
}
```

Examples:
- The life of a person (from birth to death)
- A chemical reaction
- A disease process
- A conversation

### Process Boundary
An occurrent that occurs at a single instant of time

```protobuf
message ProcessBoundary {
    string description = 1;
    google.protobuf.Timestamp timestamp = 2;
}
```

Examples:
- Birth
- Death
- The exact moment a chemical reaction reaches completion
- The beginning of a conversation

### Temporal Region
Regions of time

```protobuf
message TemporalRegion {
    string description = 1;
    google.protobuf.Timestamp start_timestamp = 2;
    google.protobuf.Timestamp end_timestamp = 3;
}
```

### Spatiotemporal Region
Regions of spacetime occupied by processes

```protobuf
message SpatioTemporalRegion {
    string description = 1;
    TemporalRegion temporal_region = 2;
    SpatialRegion spatial_region = 3;
}
```

## Key Relationships

### Participation
Continuants participate in occurrents
- A person participates in a conversation
- A molecule participates in a chemical reaction
- A cell participates in mitosis

### Location
Entities can be located in spatial or spatiotemporal regions
- An object is located in a spatial region
- A process is located in a spatiotemporal region

### Temporal Relations
- **occurs_at**: Process boundary occurs at a temporal instant
- **occupies_temporal_region**: Process occupies a temporal region
- **exists_at**: Continuant exists at a temporal instant

### Part-Whole (Mereology)
- **part_of / has_part**: Basic parthood relation
- Material entities can have material parts
- Processes can have process parts (temporal parts)

### Realization
- Realizable entities are realized in processes
- A role is realized when an entity acts in that role
- A disposition is realized when triggered

## Common Patterns

### Modeling a Life History

```python
# Create a person (MaterialEntity/Continuant)
person = MaterialEntity(
    continuant=Continuant(description="John Doe")
)

# Create birth event (ProcessBoundary)
birth = ProcessBoundary(
    description="Birth of John Doe",
    timestamp=Timestamp(seconds=...)
)

# Create life process
life = Process(
    description="Life of John Doe",
    participants=[person.continuant],
    start_process_boundary=birth,
    end_process_boundary=None  # Still living
)
```

### Modeling a Disease Process

```python
# Patient (MaterialEntity)
patient = MaterialEntity(
    continuant=Continuant(description="Patient XYZ")
)

# Disease onset (ProcessBoundary)
onset = ProcessBoundary(
    description="Disease onset",
    timestamp=Timestamp(...)
)

# Disease process
disease = Process(
    description="Pharyngitis",
    participants=[patient.continuant],
    start_process_boundary=onset
)
```

### Modeling Qualities

```python
# Object with quality
apple = MaterialEntity(
    continuant=Continuant(description="Apple")
)

# Color quality
color = Quality(
    continuant=Continuant(description="Red color of apple")
)

# Mass quality with measurement
mass = Quality(
    continuant=Continuant(description="Mass of apple")
)
# Associated with PhysicalQuantity: 150g
```

## Benefits of BFO

1. **Consistency**: Provides consistent framework across domains
2. **Integration**: Enables data integration from diverse sources
3. **Reasoning**: Supports formal reasoning about entities and relationships
4. **Clarity**: Makes implicit assumptions explicit
5. **Reusability**: Domain-neutral patterns can be reused

## Next Steps

- Read [Protobuf Guide](protobuf_guide.md) to learn how to use these concepts in code
- Explore [Domain Modeling Guide](domain_modeling_guide.md) for creating extensions
- See [examples/](../examples/) for practical implementations
- Review domain-specific guides in [domain_guides/](domain_guides/)

## References

- [BFO 2.0 Specification](https://basic-formal-ontology.org/)
- Smith, B. (2016). "Basic Formal Ontology 2.0: Specification and User's Guide"
- [OBO Foundry](http://www.obofoundry.org/) - Repository of ontologies built on BFO
