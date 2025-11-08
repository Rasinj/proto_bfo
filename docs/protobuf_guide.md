# Protocol Buffers Guide for BFO

## Introduction

This guide explains how to use Protocol Buffers (protobuf) to work with Basic Formal Ontology (BFO) definitions in the proto_bfo project.

## Setup

### Installation

```bash
# Install required dependencies
pip install -r requirements.txt

# Compile proto files
python setup.py build
```

### Project Structure

```
proto_bfo/
├── proto/
│   ├── core/           # Core BFO definitions
│   ├── common/         # Common utilities
│   └── domains/        # Domain-specific extensions
├── examples/           # Example code
├── tests/             # Test suite
└── docs/              # Documentation
```

## Compiling Proto Files

### Manual Compilation

```bash
# Compile core BFO proto
protoc --python_out=. proto/core/bfo_core.proto

# Compile with imports
protoc --python_out=. \
  -I proto \
  proto/common/units.proto \
  proto/common/identifiers.proto \
  proto/common/references.proto
```

### Automated Compilation

The `setup.py` script handles compilation automatically:

```bash
python setup.py build
```

## Basic Usage

### Importing Generated Code

```python
# Import core BFO messages
from proto.core import bfo_core_pb2

# Import common utilities
from proto.common import units_pb2
from proto.common import identifiers_pb2
from proto.common import references_pb2

# Import domain-specific messages
from proto.domains.biomedical import disease_pb2
```

### Creating Messages

#### Simple Continuant

```python
from proto.core import bfo_core_pb2

# Create a continuant (e.g., a person)
person = bfo_core_pb2.Continuant(
    description="John Doe, patient"
)
```

#### Material Entity

```python
# Create a material entity
organism = bfo_core_pb2.MaterialEntity(
    continuant=bfo_core_pb2.Continuant(
        description="Homo sapiens individual"
    )
)
```

#### Process with Temporal Boundaries

```python
from google.protobuf.timestamp_pb2 import Timestamp
import time

# Create start boundary
birth = bfo_core_pb2.ProcessBoundary(
    description="Birth",
    timestamp=Timestamp(seconds=int(time.mktime((1990, 1, 1, 0, 0, 0, 0, 0, 0))))
)

# Create process
life = bfo_core_pb2.Process(
    description="Life of John Doe",
    participants=[person],
    start_process_boundary=birth
)
```

### Using Common Utilities

#### Physical Quantities with Units

```python
from proto.common import units_pb2

# Create a mass measurement
mass = units_pb2.PhysicalQuantity(
    quantity=units_pb2.QuantityValue(
        value=70.5,
        common=units_pb2.CommonUnit.KILOGRAM,
        uncertainty=0.1
    ),
    dimension_name="mass"
)

# Create a temperature measurement
temp = units_pb2.PhysicalQuantity(
    quantity=units_pb2.QuantityValue(
        value=37.0,
        common=units_pb2.CommonUnit.CELSIUS
    ),
    dimension_name="temperature"
)
```

#### Identifiers

```python
from proto.common import identifiers_pb2

# Create a DOI
paper_doi = identifiers_pb2.DOI(
    identifier="10.1038/s41586-020-1234-5"
)

# Create an ORCID
researcher = identifiers_pb2.ORCID(
    identifier="0000-0002-1825-0097",
    display_name="Dr. Jane Smith"
)

# Create a medical identifier
diagnosis = identifiers_pb2.MedicalIdentifier(
    icd10_code="J02.9"  # Pharyngitis
)
```

#### Ontology References

```python
from proto.common import references_pb2

# Create a MeSH reference
mesh_ref = references_pb2.MeSHReference(
    mesh_id="D010612",
    descriptor_name="Pharyngitis",
    tree_numbers=["C08.730", "C09.775"]
)

# Create a Gene Ontology reference
go_ref = references_pb2.GOReference(
    go_id="GO:0008150",
    go_term="biological_process",
    aspect=references_pb2.GOReference.BIOLOGICAL_PROCESS
)
```

## Serialization

### Binary Serialization

```python
# Serialize to binary
binary_data = life.SerializeToString()

# Save to file
with open("life_process.bin", "wb") as f:
    f.write(binary_data)

# Deserialize from binary
new_process = bfo_core_pb2.Process()
new_process.ParseFromString(binary_data)
```

### JSON Serialization

```python
from google.protobuf import json_format

# Serialize to JSON
json_str = json_format.MessageToJson(life)

# Deserialize from JSON
new_process = bfo_core_pb2.Process()
json_format.Parse(json_str, new_process)
```

### Text Format (for debugging)

```python
from google.protobuf import text_format

# Convert to text
text_str = text_format.MessageToString(life)
print(text_str)

# Parse from text
new_process = bfo_core_pb2.Process()
text_format.Parse(text_str, new_process)
```

## Advanced Patterns

### Nested Entities

```python
# Create a hierarchy of entities
organism = bfo_core_pb2.MaterialEntity(
    continuant=bfo_core_pb2.Continuant(
        description="Human organism"
    )
)

# Create organs as parts
heart = bfo_core_pb2.MaterialEntity(
    continuant=bfo_core_pb2.Continuant(
        description="Heart"
    )
)

liver = bfo_core_pb2.MaterialEntity(
    continuant=bfo_core_pb2.Continuant(
        description="Liver"
    )
)
```

### Spatiotemporal Regions

```python
# Create spatial region
spatial = bfo_core_pb2.SpatialRegion(
    description="Hospital room 302",
    placeholder_spatialregiondata="coordinates or geometry here"
)

# Create temporal region
temporal = bfo_core_pb2.TemporalRegion(
    description="Surgery duration",
    start_timestamp=Timestamp(seconds=start_time),
    end_timestamp=Timestamp(seconds=end_time)
)

# Create spatiotemporal region
location = bfo_core_pb2.SpatioTemporalRegion(
    description="Surgery in room 302",
    temporal_region=temporal,
    spatial_region=spatial
)

# Create history
surgery_history = bfo_core_pb2.History(
    description="Patient surgical history",
    participant=patient,
    spatiotemporal_region=location
)
```

### Relational Qualities

```python
# Model a relationship between two entities
parent = bfo_core_pb2.Continuant(description="Parent")
child = bfo_core_pb2.Continuant(description="Child")

parent_child_relation = bfo_core_pb2.RelationalQuality(
    description="parent-child relationship",
    relational_giver=parent,
    relational_receiver=child,
    invert_relation=False
)
```

## Working with Domain Extensions

### Biomedical Domain

```python
from proto.domains.biomedical import disease_pb2

# Create a disease process with ontology references
disease = disease_pb2.Disease(
    disease_process=life,  # The disease process
    affected_organism=organism,
    mesh_id="D010612",
    icd_code="J02.9"
)
```

### Transaction Domain

```python
from proto.domains.social import transaction_pb2
from proto.common import units_pb2

# Create transactional entities
buyer = transaction_pb2.TransactionalEntity(
    name="Alice",
    type=transaction_pb2.TransactionalEntity.TRANSACTEE
)

seller = transaction_pb2.TransactionalEntity(
    name="Bob",
    type=transaction_pb2.TransactionalEntity.TRANSACTEE
)

# Create resources
money = transaction_pb2.Resource(
    description="US Dollars",
    physical_quantity=units_pb2.PhysicalQuantity(
        quantity=units_pb2.QuantityValue(
            value=100.0,
            common=units_pb2.CommonUnit.CURRENCY_USD
        )
    )
)

# Create transaction
transaction = transaction_pb2.Transaction(
    transactee_1=buyer,
    transactee_2=seller,
    transactee_1_given=money,
    datetime=Timestamp(seconds=int(time.time()))
)
```

## Validation

### Field Validation

```python
# Check required fields
if not life.HasField("start_process_boundary"):
    print("Warning: Process missing start boundary")

# Check repeated fields
if len(life.participants) == 0:
    print("Warning: Process has no participants")
```

### Custom Validation

```python
def validate_process(process):
    """Validate BFO process constraints"""
    errors = []

    # Process should have at least one participant
    if len(process.participants) == 0:
        errors.append("Process must have at least one participant")

    # Process should have a start boundary
    if not process.HasField("start_process_boundary"):
        errors.append("Process must have a start boundary")

    # If has end boundary, check it's after start
    if process.HasField("end_process_boundary"):
        if (process.end_process_boundary.timestamp.seconds <
            process.start_process_boundary.timestamp.seconds):
            errors.append("End boundary must be after start boundary")

    return errors

# Use validation
errors = validate_process(life)
if errors:
    for error in errors:
        print(f"Validation error: {error}")
```

## Performance Tips

1. **Reuse message objects** instead of creating new ones repeatedly
2. **Use binary serialization** for storage and transmission (more efficient than JSON)
3. **Lazy parsing** - protobuf only parses fields when accessed
4. **Arena allocation** (C++ only) for high-performance scenarios

## Common Pitfalls

1. **Forgetting to compile** proto files after changes
2. **Import path issues** - use `-I` flag correctly with protoc
3. **Default values** - unset fields return default values (0, "", False)
4. **Timestamp precision** - protobuf Timestamp is in seconds + nanoseconds

## Next Steps

- Read [Domain Modeling Guide](domain_modeling_guide.md) for creating extensions
- Explore [examples/](../examples/) for complete working examples
- See [API Reference](api_reference/) for detailed message documentation

## Resources

- [Protocol Buffers Documentation](https://developers.google.com/protocol-buffers)
- [Python Tutorial](https://developers.google.com/protocol-buffers/docs/pythontutorial)
- [Proto3 Language Guide](https://developers.google.com/protocol-buffers/docs/proto3)
