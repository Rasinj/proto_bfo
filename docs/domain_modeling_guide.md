# Domain Modeling Guide

## Introduction

This guide shows you how to create domain-specific extensions of BFO using Protocol Buffers. Domain extensions allow you to model specialized concepts while maintaining compatibility with the core BFO ontology.

## Principles of Domain Extension

### 1. Build on Core BFO

Always extend core BFO messages rather than creating parallel hierarchies:

✅ **Good**:
```protobuf
message Disease {
    Process disease_process = 1;  // Extends BFO Process
    MaterialEntity affected_organism = 2;
}
```

❌ **Bad**:
```protobuf
message Disease {
    string name = 1;  // No connection to BFO
    string patient = 2;
}
```

### 2. Respect BFO Distinctions

Maintain the continuant/occurrent distinction:
- Diseases are **processes** (occurrents)
- Patients are **material entities** (continuants)
- Symptoms are **qualities** (dependent continuants)

### 3. Use Common Utilities

Leverage standard identifiers, units, and ontology references:

```protobuf
import "proto/common/units.proto";
import "proto/common/identifiers.proto";
import "proto/common/references.proto";
```

## Creating a Domain Extension

### Step 1: Define Your Domain

Identify the key concepts in your domain:
- What are the objects (continuants)?
- What are the processes (occurrents)?
- What qualities and relationships matter?

### Step 2: Create Proto File Structure

```protobuf
syntax = "proto3";

package protobuf_world.domains.yourdomain;

// Import core BFO
import "proto/core/bfo_core.proto";

// Import common utilities
import "proto/common/units.proto";
import "proto/common/identifiers.proto";
import "proto/common/references.proto";

// Your domain messages here
```

### Step 3: Define Domain Messages

Create messages that extend BFO concepts with domain-specific fields.

## Example: Clinical Medicine Domain

Let's model clinical medicine concepts:

```protobuf
syntax = "proto3";

package protobuf_world.domains.clinical;

import "proto/core/bfo_core.proto";
import "proto/common/units.proto";
import "proto/common/identifiers.proto";
import "proto/common/references.proto";
import "google/protobuf/timestamp.proto";

// A patient is a material entity with a clinical role
message Patient {
    MaterialEntity organism = 1;
    string patient_id = 2;
    repeated MedicalIdentifier identifiers = 3;
    google.protobuf.Timestamp date_of_birth = 4;
}

// A disease is a process occurring in an organism
message Disease {
    Process disease_process = 1;
    Patient patient = 2;
    repeated Quality pathological_qualities = 3;
    MedicalIdentifier icd_code = 4;
    MeSHReference mesh_reference = 5;
    ProcessBoundary onset = 6;
    ProcessBoundary resolution = 7;  // May be null for chronic diseases
}

// A clinical measurement is an observation of a quality
message ClinicalMeasurement {
    Quality measured_quality = 1;
    PhysicalQuantity value = 2;
    google.protobuf.Timestamp measurement_time = 3;
    Patient patient = 4;
    string measurement_type = 5;  // e.g., "blood_pressure", "temperature"
    MaterialEntity measuring_device = 6;  // Optional
}

// A treatment is a process intended to affect a disease
message Treatment {
    Process treatment_process = 1;
    Patient patient = 2;
    Disease target_disease = 3;
    repeated MaterialEntity therapeutic_agents = 4;
    Disposition therapeutic_disposition = 5;
    ProcessBoundary start_date = 6;
    ProcessBoundary end_date = 7;  // May be null for ongoing treatment
}

// A complete electronic health record
message HealthRecord {
    Patient patient = 1;
    repeated Disease diagnoses = 2;
    repeated Treatment treatments = 3;
    repeated ClinicalMeasurement measurements = 4;
    repeated Occurrent clinical_encounters = 5;
}
```

## Example: Ecological Domain

Modeling ecological systems:

```protobuf
syntax = "proto3";

package protobuf_world.domains.ecology;

import "proto/core/bfo_core.proto";
import "proto/common/units.proto";
import "proto/common/references.proto";

// An organism in an ecosystem
message Organism {
    MaterialEntity material_entity = 1;
    string taxon_name = 2;
    BiologicalIdentifier ncbi_taxonomy = 3;
    Process life_history = 4;
}

// An ecosystem is a complex of organisms and their environment
message Ecosystem {
    ImmaterialEntity spatial_boundary = 1;
    repeated Organism organisms = 2;
    repeated Process ecological_processes = 3;
    repeated MaterialEntity abiotic_components = 4;
    string ecosystem_type = 5;  // forest, grassland, aquatic, etc.
}

// A predation event
message PredationEvent {
    Process predation_process = 1;
    Organism predator = 2;
    Organism prey = 3;
    SpatioTemporalRegion location = 4;
    bool successful = 5;
}

// A population is an object aggregate of organisms
message Population {
    repeated Organism organisms = 1;
    string species = 2;
    ImmaterialEntity habitat = 3;
    QuantityValue population_size = 4;
    QuantityValue density = 5;
}
```

## Example: Manufacturing Domain

Modeling manufacturing processes:

```protobuf
syntax = "proto3";

package protobuf_world.domains.manufacturing;

import "proto/core/bfo_core.proto";
import "proto/common/units.proto";
import "proto/common/identifiers.proto";

// A manufactured product
message Product {
    MaterialEntity artifact = 1;
    string product_id = 2;
    string sku = 3;
    Design design_specification = 4;
    repeated Quality quality_metrics = 5;
    ProcessBoundary manufacture_date = 6;
}

// A design is information content
message Design {
    string design_id = 1;
    string cad_model_url = 2;
    repeated Specification requirements = 3;
    MaterialEntity physical_bearer = 4;  // e.g., hard drive storing the design
}

// A manufacturing process
message ManufacturingProcess {
    Process process = 1;
    repeated MaterialEntity inputs = 2;
    Product output = 3;
    repeated MaterialEntity equipment = 4;
    SpatioTemporalRegion production_location = 5;
    Disposition manufacturing_capability = 6;
}

// A specification is a type of directive
message Specification {
    string specification_name = 1;
    string requirement_description = 2;
    QuantityRange acceptable_range = 3;
    bool is_critical = 4;
}

// Quality control measurement
message QualityControlMeasurement {
    Quality measured_quality = 1;
    PhysicalQuantity measured_value = 2;
    Specification specification = 3;
    bool passes = 4;
    Product product = 5;
}
```

## Common Patterns

### Pattern 1: Participant Roles

Use roles to model different ways entities participate in processes:

```protobuf
message SurgicalProcedure {
    Process surgical_process = 1;
    Patient patient = 2;
    repeated ClinicalRole roles = 3;  // surgeon, anesthesiologist, nurse
}

message ClinicalRole {
    Role role = 1;
    MaterialEntity bearer = 2;  // Person bearing the role
    string role_type = 3;  // "surgeon", "nurse", etc.
}
```

### Pattern 2: Temporal Tracking

Track entity state changes over time:

```protobuf
message DiseaseProgression {
    Disease disease = 1;
    repeated DiseaseState states = 2;
}

message DiseaseState {
    Quality disease_quality = 1;
    ProcessBoundary state_change = 2;
    string severity = 3;  // mild, moderate, severe
}
```

### Pattern 3: Provenance

Track where information came from:

```protobuf
message ProvenanceRecord {
    google.protobuf.Timestamp recorded_at = 1;
    string recorded_by = 2;  // Person or system
    repeated DOI supporting_publications = 3;
    string confidence_level = 4;
    string method = 5;  // How information was obtained
}

message AnnotatedDisease {
    Disease disease = 1;
    ProvenanceRecord provenance = 2;
}
```

### Pattern 4: Hierarchical Classification

Model taxonomies and classifications:

```protobuf
message TaxonomicClassification {
    Organism organism = 1;
    string kingdom = 2;
    string phylum = 3;
    string class = 4;
    string order = 5;
    string family = 6;
    string genus = 7;
    string species = 8;
    BiologicalIdentifier ncbi_taxonomy = 9;
}
```

## Best Practices

### 1. Use Descriptive Names

✅ **Good**: `DiseaseOnsetBoundary`, `TreatmentProcess`, `PathologicalQuality`
❌ **Bad**: `DOB`, `Proc1`, `Thing`

### 2. Document Your Messages

```protobuf
// A disease represents a pathological process occurring in an organism.
// It is modeled as a BFO Process with specific participants and qualities.
message Disease {
    Process disease_process = 1;  // The underlying BFO process
    Patient patient = 2;           // The affected organism
    // Additional fields...
}
```

### 3. Version Your Proto Files

```protobuf
syntax = "proto3";

// Version 1.2.0 - Added disease severity classification
// Version 1.1.0 - Added MeSH references
// Version 1.0.0 - Initial release

package protobuf_world.domains.clinical.v1;
```

### 4. Provide Examples

Include example usage in comments:

```protobuf
// Example usage:
//   Disease measles = Disease(
//     disease_process=Process(description="Measles infection"),
//     patient=patient,
//     icd_code=MedicalIdentifier(icd10_code="B05.9"),
//     mesh_reference=MeSHReference(mesh_id="D008457")
//   );
message Disease {
    // ...
}
```

### 5. Consider Interoperability

Link to standard ontologies and vocabularies:

```protobuf
message Phenotype {
    Quality quality = 1;
    HPOReference hpo_term = 2;      // Human Phenotype Ontology
    string description = 3;
    QuantityValue frequency = 4;     // How often observed
}
```

## Testing Your Domain Model

Create test cases for your domain:

```python
def test_disease_creation():
    """Test creating a disease with all required fields"""
    patient = Patient(
        organism=MaterialEntity(
            continuant=Continuant(description="John Doe")
        ),
        patient_id="P12345"
    )

    onset = ProcessBoundary(
        description="Disease onset",
        timestamp=Timestamp(seconds=int(time.time()))
    )

    disease = Disease(
        disease_process=Process(
            description="Pharyngitis",
            participants=[patient.organism.continuant]
        ),
        patient=patient,
        onset=onset
    )

    assert disease.patient.patient_id == "P12345"
    assert disease.disease_process.description == "Pharyngitis"
```

## Publishing Your Domain Extension

1. **Document thoroughly** - Write guides specific to your domain
2. **Provide examples** - Include working code examples
3. **Create tests** - Ensure your domain model works correctly
4. **Version properly** - Use semantic versioning
5. **Share widely** - Make it available for others to use

## Next Steps

- See [examples/](../examples/) for complete domain implementations
- Review [domain_guides/](domain_guides/) for specialized documentation
- Read [API Reference](api_reference/) for message details

## Resources

- [BFO 2.0 Specification](https://basic-formal-ontology.org/)
- [Protocol Buffers Style Guide](https://developers.google.com/protocol-buffers/docs/style)
- [OBO Foundry](http://www.obofoundry.org/) - Examples of domain ontologies built on BFO
