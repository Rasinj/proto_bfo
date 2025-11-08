# Proto BFO - Basic Formal Ontology in Protocol Buffers

A comprehensive implementation of [Basic Formal Ontology (BFO)](https://basic-formal-ontology.org/) using Protocol Buffers for efficient serialization, cross-language support, and domain-specific knowledge representation.

## Overview

Proto BFO translates the BFO structure to Protocol Buffers, enabling:
- **Dynamic transformation and extension** of ontological structures
- **Efficient binary serialization** for storage and transmission
- **Cross-language compatibility** (Python, Java, C++, Go, etc.)
- **Domain-specific modeling** across biomedical, social, physical, and computational domains
- **Formal reasoning** about spatial and temporal entities

## Features

### Core BFO Implementation
- ✅ Complete BFO 2.0 hierarchy (Continuants, Occurrents, Qualities, Processes)
- ✅ Temporal and spatial reasoning
- ✅ Process boundaries and spatiotemporal regions
- ✅ Material and immaterial entities
- ✅ Relational qualities and participant relationships

### Common Utilities
- **Units System** - SI base units, derived units, physical quantities with uncertainty
- **Identifiers** - DOI, ORCID, ISBN, medical IDs (ICD, MESH, SNOMED), biological IDs (UniProt, NCBI)
- **Ontology References** - Integration with GO, MESH, SNOMED CT, HPO, ChEBI, and more

### Domain Extensions (15 domains)
Ready-to-implement extensions across:
- **Biomedical** - Disease, clinical medicine, molecular biology
- **Social & Organizational** - Organizations, economics, transactions
- **Information & Knowledge** - Documents, knowledge graphs
- **Physical & Engineering** - Geospatial, manufacturing
- **Scientific** - Ecology, observation, experimentation
- **Temporal** - Historical events and chronology
- **Computational** - Software systems

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Rasinj/proto_bfo.git
cd proto_bfo

# Install dependencies
pip install -r requirements.txt

# Compile proto files
python setup.py build
```

### Basic Usage

```python
from proto.core import bfo_core_pb2
from proto.common import units_pb2
from google.protobuf.timestamp_pb2 import Timestamp
import time

# Create a person (Continuant/MaterialEntity)
person = bfo_core_pb2.MaterialEntity(
    continuant=bfo_core_pb2.Continuant(description="John Doe")
)

# Create a process (life)
birth = bfo_core_pb2.ProcessBoundary(
    description="Birth",
    timestamp=Timestamp(seconds=int(time.time()))
)

life = bfo_core_pb2.Process(
    description="Life of John Doe",
    participants=[person.continuant],
    start_process_boundary=birth
)

# Create a physical quantity with units
mass = units_pb2.PhysicalQuantity(
    quantity=units_pb2.QuantityValue(
        value=70.0,
        common=units_pb2.CommonUnit.KILOGRAM,
        uncertainty=0.1
    ),
    dimension_name="mass"
)

# Serialize to binary
binary_data = life.SerializeToString()

# Save to file
with open("life_process.bin", "wb") as f:
    f.write(binary_data)
```

## Project Structure

```
proto_bfo/
├── proto/
│   ├── core/                   # Core BFO definitions
│   │   └── bfo_core.proto
│   ├── common/                 # Common utilities
│   │   ├── units.proto         # SI units and measurements
│   │   ├── identifiers.proto   # Standard ID systems
│   │   └── references.proto    # Ontology references
│   └── domains/                # Domain-specific extensions
│       ├── biomedical/         # Disease, clinical, molecular
│       ├── social/             # Organizations, economics
│       ├── information/        # Documents, knowledge
│       ├── physical/           # Geospatial, manufacturing
│       ├── scientific/         # Ecology, observation
│       ├── temporal/           # Historical events
│       └── computational/      # Software systems
├── examples/                   # Example code by domain
├── tests/
│   ├── unit/                   # Unit tests
│   └── integration/            # Integration tests
├── docs/                       # Comprehensive documentation
│   ├── bfo_primer.md          # Introduction to BFO
│   ├── protobuf_guide.md      # Protobuf usage guide
│   ├── domain_modeling_guide.md
│   └── domain_guides/         # Domain-specific guides
└── tools/                      # Validators, converters, generators
```

## Documentation

- **[BFO Primer](docs/bfo_primer.md)** - Introduction to Basic Formal Ontology concepts
- **[Protobuf Guide](docs/protobuf_guide.md)** - How to use Protocol Buffers with BFO
- **[Domain Modeling Guide](docs/domain_modeling_guide.md)** - Creating domain-specific extensions
- **[API Reference](docs/api_reference/)** - Detailed message documentation
- **[Domain Guides](docs/domain_guides/)** - Specialized documentation per domain

## Examples

### Disease Modeling (Biomedical)

```python
from proto.domains.biomedical import disease_pb2
from proto.common import references_pb2

# Create a disease with ontology references
pharyngitis = disease_pb2.Disease(
    disease_process=bfo_core_pb2.Process(
        description="Pharyngitis",
        participants=[patient.continuant]
    ),
    affected_organism=patient,
    mesh_id="D010612",
    icd_code="J02.9"
)
```

### Transaction Modeling (Social/Economic)

```python
from proto.domains.social import transaction_pb2

# Create a transaction
transaction = transaction_pb2.Transaction(
    transactee_1=buyer,
    transactee_2=seller,
    transactee_1_given=money_resource,
    transactee_2_given=product_resource,
    datetime=Timestamp(seconds=int(time.time()))
)
```

## Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=proto --cov-report=term --cov-report=html

# Run specific test module
pytest tests/unit/test_bfo_core.py -v
```

## CI/CD

GitHub Actions workflow includes:
- ✅ Proto file validation
- ✅ Multi-version Python testing (3.8-3.11)
- ✅ Code formatting checks (black, isort, flake8)
- ✅ Test coverage reporting
- ✅ Documentation building
- ✅ Security vulnerability scanning

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Key areas for contribution:
1. **Domain implementations** - Implement placeholder domain proto files
2. **Examples** - Add working examples for each domain
3. **Tests** - Expand test coverage
4. **Documentation** - Domain-specific guides and tutorials
5. **Tools** - Validators, converters (OWL↔Proto, JSON-LD↔Proto)

## Roadmap

### Phase 1 (Current) - Infrastructure ✅
- [x] Core BFO implementation
- [x] Common utilities (units, identifiers, references)
- [x] Documentation structure
- [x] Testing infrastructure
- [x] CI/CD pipeline
- [x] Domain placeholders

### Phase 2 - Domain Implementation
- [ ] Biomedical domain (disease, clinical, molecular)
- [ ] Social domain (organizations, economics)
- [ ] Information domain (documents, knowledge)
- [ ] Scientific domain (ecology, observation)

### Phase 3 - Tools & Ecosystem
- [ ] Validation tools for BFO conformance
- [ ] Converters (OWL, JSON-LD, RDF)
- [ ] gRPC service definitions
- [ ] GraphQL schema generation
- [ ] Visualization tools

### Phase 4 - Advanced Features
- [ ] Reasoning engine integration
- [ ] Query language (SPARQL-like)
- [ ] Version control for ontologies
- [ ] Collaborative editing tools

## Use Cases

- **Healthcare** - Electronic health records, disease surveillance, clinical decision support
- **Research** - Scientific data integration, experimental protocols, observations
- **Manufacturing** - Product lifecycle management, quality control, supply chain
- **Social Sciences** - Organizational analysis, economic modeling, social networks
- **Environmental** - Ecological monitoring, biodiversity tracking, climate data

## License

[Specify License]

## Citation

If you use Proto BFO in your research, please cite:

```bibtex
@software{proto_bfo,
  title = {Proto BFO: Basic Formal Ontology in Protocol Buffers},
  author = {Nordesjo, Olle},
  year = {2024},
  url = {https://github.com/Rasinj/proto_bfo}
}
```

## References

- [Basic Formal Ontology](https://basic-formal-ontology.org/)
- [BFO 2.0 Specification](https://github.com/BFO-ontology/BFO)
- [Protocol Buffers](https://developers.google.com/protocol-buffers)
- [OBO Foundry](http://www.obofoundry.org/)

## Contact

- **Issues**: [GitHub Issues](https://github.com/Rasinj/proto_bfo/issues)
- **Email**: olle@nordesjo.net

---

**Status**: Active Development | **Version**: 2.0.0 | **Last Updated**: 2024
