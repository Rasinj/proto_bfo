# Proto BFO Documentation

Welcome to the Proto BFO documentation. This directory contains comprehensive documentation for using Protocol Buffers with Basic Formal Ontology (BFO).

## Documentation Structure

### Core Documentation
- [BFO Primer](bfo_primer.md) - Introduction to Basic Formal Ontology concepts
- [Protobuf Guide](protobuf_guide.md) - How to use Protocol Buffers with BFO
- [Domain Modeling Guide](domain_modeling_guide.md) - Creating domain-specific extensions
- [Quick Start](quick_start.md) - Get started quickly with examples

### API Reference
The [api_reference/](api_reference/) directory contains detailed documentation for all message types:
- Core BFO messages
- Domain-specific messages
- Common utilities (units, identifiers, references)

### Domain Guides
The [domain_guides/](domain_guides/) directory contains specialized guides for each domain:
- Biomedical applications
- Social and organizational modeling
- Information and knowledge representation
- Physical and engineering systems
- Scientific observations and experiments
- Temporal and historical events
- Computational systems

## Key Concepts

### Basic Formal Ontology (BFO)
BFO is a top-level ontology designed to support information integration and retrieval. It provides:
- A framework for representing entities across domains
- Clear distinctions between continuants (objects) and occurrents (processes)
- Formal relationships between entities
- Temporal and spatial reasoning capabilities

### Why Protocol Buffers?
Protocol Buffers provide:
- Language-agnostic serialization
- Efficient binary encoding
- Strong typing and validation
- Easy evolution and extension
- Wide language support

## Getting Started

1. **Install dependencies**: `pip install -r requirements.txt`
2. **Compile proto files**: `python setup.py build`
3. **Run examples**: See `examples/` directory
4. **Read the primer**: Start with [BFO Primer](bfo_primer.md)

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for contribution guidelines.

## License

See [LICENSE](../LICENSE) for licensing information.
