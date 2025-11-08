# Domain-Specific Proto Extensions

This directory contains domain-specific extensions of Basic Formal Ontology (BFO) using Protocol Buffers.

## Domain Categories

### Biomedical
- **disease.proto** - Disease and pathology modeling
- **clinical.proto** - Clinical medicine and patient care
- **molecular.proto** - Molecular biology and biochemistry
- **dna_sequence.proto** - DNA/RNA sequences (existing)

### Social & Organizational
- **organization.proto** - Organizations, roles, and social structures
- **economic.proto** - Economic activities and markets
- **transaction.proto** - Transactions and exchanges (existing)

### Information & Knowledge
- **documents.proto** - Documents and information artifacts
- **knowledge.proto** - Knowledge representation and semantics

### Physical & Engineering
- **geospatial.proto** - Geographic and spatial information
- **manufacturing.proto** - Manufacturing and production

### Scientific
- **ecology.proto** - Ecological systems and biodiversity
- **observation.proto** - Scientific observation and experimentation

### Temporal
- **historical.proto** - Historical events and chronology

### Computational
- **software.proto** - Software systems and computation

## Development Status

Current status: **PLACEHOLDER - Ready for Implementation**

All domain proto files are currently placeholders with:
- Basic message structure
- Import statements for core BFO and common utilities
- TODO comments for planned features
- Minimal example messages

## Next Steps

For each domain, the following should be implemented:

1. **Define core messages** - Key entities specific to the domain
2. **Establish relationships** - How entities relate to core BFO concepts
3. **Add validations** - Constraints specific to the domain
4. **Create examples** - Working code examples in `/examples/<domain>/`
5. **Write tests** - Unit and integration tests in `/tests/`
6. **Document** - Domain-specific guide in `/docs/domain_guides/`

## Implementation Priority

Suggested implementation order based on maturity and utility:

1. **biomedical/disease.proto** - Builds on existing MeSH integration
2. **biomedical/clinical.proto** - Practical healthcare applications
3. **social/organization.proto** - Widely applicable social modeling
4. **information/documents.proto** - Essential for knowledge management
5. **scientific/observation.proto** - Core scientific methodology
6. **biomedical/molecular.proto** - Extends biological domain
7. **social/economic.proto** - Extends transaction.proto
8. **physical/geospatial.proto** - Location-based applications
9. **scientific/ecology.proto** - Environmental and biological systems
10. **temporal/historical.proto** - Event modeling
11. **physical/manufacturing.proto** - Industrial applications
12. **information/knowledge.proto** - Advanced semantic modeling
13. **computational/software.proto** - Software engineering applications

## Contributing

When implementing a domain:

1. Follow the patterns in existing proto files
2. Maintain compatibility with core BFO concepts
3. Use common utilities (units, identifiers, references)
4. Document all messages and fields
5. Create working examples
6. Add comprehensive tests
7. Update this README with implementation status

## Resources

- [BFO Primer](../../docs/bfo_primer.md)
- [Domain Modeling Guide](../../docs/domain_modeling_guide.md)
- [Protobuf Guide](../../docs/protobuf_guide.md)
