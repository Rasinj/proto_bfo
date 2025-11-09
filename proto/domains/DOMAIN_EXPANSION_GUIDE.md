# Domain Expansion Guide

## Overview

The Proto BFO domain ontologies are designed to support **hierarchical tree cutting** - users can select any "leaf" node in the taxonomy, and all parent nodes up to the root are automatically included in their ontology subset.

## Design Principles

### 1. Hierarchical Composition

Each domain is organized as a tree where:
- **Root nodes** represent the most general concepts
- **Intermediate nodes** represent classifications and categories
- **Leaf nodes** represent the most specific entities

Example from disease.proto:
```
Disease (root)
  └─ InfectiousDisease
      └─ ViralInfection
          └─ RespiratoryViralInfection
              └─ Influenza (leaf)
              └─ COVID19 (leaf)
```

### 2. Message Composition Pattern

Child messages include their parent as a field:

```protobuf
message Disease {
    // Base disease fields
}

message InfectiousDisease {
    Disease base_disease = 1;  // Include parent
    // Infectious-specific fields
}

message ViralInfection {
    InfectiousDisease infectious_disease = 1;  // Include parent
    // Viral-specific fields
}
```

### 3. Tree Cutting Example

If a user requests `Influenza`:
1. System includes `Influenza` (leaf)
2. Automatically includes `RespiratoryViralInfection` (parent)
3. Automatically includes `ViralInfection` (grandparent)
4. Automatically includes `InfectiousDisease` (great-grandparent)
5. Automatically includes `Disease` (root)

All parent enums, supporting messages, and relationships are also included.

## Current Domain Expansions

### Biomedical Domains

#### 1. Disease Taxonomy (disease.proto - 622 lines)

**Hierarchy Depth: 5-6 levels**

Major branches:
- **Infectious Diseases**
  - Viral Infections (DNA virus, RNA virus, retrovirus)
    - Respiratory viral (Influenza, COVID-19)
  - Bacterial Infections (by Gram stain, resistance)
    - Tuberculosis (latent, active, drug-resistant)
  - Fungal, Parasitic, Prion

- **Genetic Diseases**
  - Single gene disorders (Cystic Fibrosis, Sickle Cell)
  - Chromosomal abnormalities
  - Inheritance patterns (autosomal, X-linked, mitochondrial)

- **Metabolic Diseases**
  - By pathway (carbohydrate, lipid, protein, etc.)
  - Diabetes Mellitus (Type 1, Type 2, MODY, Gestational)
  - Diabetic complications

- **Neoplastic Diseases** (Cancer)
  - Carcinoma, Sarcoma, Leukemia, Lymphoma
  - Tumor grading (1-4) and staging (0-IV)
  - Lung Cancer subtypes

- **Cardiovascular Diseases**
  - Coronary Artery Disease
  - Myocardial Infarction (STEMI, NSTEMI)

- **Neurological Diseases**
  - Neurodegenerative (Alzheimer's, Parkinson's)
  - By nervous system (central, peripheral, autonomic)

**Features:**
- Standard medical identifiers (ICD, MESH, SNOMED)
- Clinical components (signs, symptoms, risk factors)
- Disease progression tracking
- Comorbidity relationships

#### 2. Anatomical Structures (anatomy.proto - 759 lines)

**Hierarchy Depth: 4-7 levels**

Major branches:
- **Organ Systems** (11 systems)
  - Circulatory System
    - Heart (chambers, valves, coronary arteries, conduction)
    - Blood vessels (arteries, veins, capillaries by size)

  - Nervous System
    - Central (Brain, Spinal Cord)
      - Brain regions (cerebrum, cerebellum, brainstem)
      - Cerebral hemispheres → Lobes → Functional areas
      - Spinal segments (cervical, thoracic, lumbar, sacral)
    - Peripheral (nerves, ganglia)
    - Autonomic (sympathetic, parasympathetic, enteric)

  - Respiratory System
    - Lungs (lobes, bronchopulmonary segments)
    - Bronchial tree (airways by generation)
    - Alveoli

  - Digestive System
    - GI tract segments
    - Small intestine (duodenum, jejunum, ileum)
    - Large intestine (cecum, colon subsegments)
    - Accessory organs (liver with Couinaud segments)

  - Musculoskeletal System
    - Skeletal (axial, appendicular)
      - Skull (cranial bones, facial bones)
      - Vertebral column (by level and number)
      - Joints (fibrous, cartilaginous, synovial)
    - Muscular (skeletal, cardiac, smooth)

- **Tissue Level**
  - Epithelial, Connective, Muscle, Nervous
  - Tissue layers (mucosa, submucosa, muscularis, serosa)

- **Cellular Level**
  - Cell types (neuron, epithelial, endothelial, etc.)
  - Cellular components (organelles)

**Features:**
- Spatial relationships (superior, inferior, medial, lateral, etc.)
- Standard anatomical identifiers (UBERON, FMA)
- Functional areas and innervation

### Social & Organizational Domains

#### 3. Organization Taxonomy (organization.proto - to be expanded)

Planned hierarchy:
- Organization types
  - Government (federal, state, local, international)
  - Corporate (public, private, partnerships)
  - Non-profit (charitable, educational, religious)
- Role hierarchies (executive, managerial, operational)
- Organizational processes
- Membership structures

### Information & Knowledge Domains

#### 4. Document & Knowledge Taxonomy (documents.proto - to be expanded)

Planned hierarchy:
- Document types (academic, legal, technical, administrative)
- Data structures (relational, hierarchical, graph, time-series)
- Knowledge representations (ontologies, taxonomies, thesauri)
- Media types (text, image, audio, video, multimodal)

## Expansion Guidelines

### Adding New Hierarchies

1. **Identify the root concept**
   - Most general entity in the domain
   - Includes universal fields shared by all subtypes

2. **Map major categories**
   - 3-5 major branches from root
   - Each represents a different classification aspect

3. **Define intermediate levels**
   - 2-4 levels between root and leaves
   - Each level adds specificity

4. **Create leaf nodes**
   - Most specific, concrete entities
   - Include all parent types via composition

5. **Add supporting messages**
   - Shared clinical/technical components
   - Enumerations for classifications
   - Relationship types

### Composition Best Practices

```protobuf
// ✅ Good: Include parent type
message SpecificDisease {
    GeneralDisease parent = 1;
    // Specific fields
}

// ❌ Avoid: Copying parent fields
message SpecificDisease {
    string description = 1;  // Duplicated from parent
    // This breaks the hierarchy
}

// ✅ Good: Use enums for closed classifications
message Disease {
    DiseaseCategory category = 1;

    enum DiseaseCategory {
        INFECTIOUS = 1;
        GENETIC = 2;
        METABOLIC = 3;
    }
}

// ✅ Good: Use standard references
message Disease {
    protobuf_world.common.MedicalIdentifier icd_code = 1;
    protobuf_world.common.MeSHReference mesh_ref = 2;
}
```

### Relationship Modeling

Use parent fields for **is-a** relationships:
```protobuf
message Influenza {
    RespiratoryViralInfection respiratory_viral = 1;  // IS-A relationship
}
```

Use repeated fields for **has-a** relationships:
```protobuf
message Disease {
    repeated Disease comorbidities = 1;  // HAS-A relationship
    repeated ClinicalSign signs = 2;     // HAS-A relationship
}
```

Use references for **relates-to** relationships:
```protobuf
message SpatialRelation {
    AnatomicalStructure related_structure = 1;
    RelationType relation = 2;  // ADJACENT-TO, SUPERIOR-TO, etc.
}
```

## Tree Cutting Implementation

### Selection Algorithm

```python
def get_ontology_subset(leaf_node_names):
    """
    Given a list of leaf node names, return complete ontology
    including all parent nodes up to root.
    """
    included_messages = set()

    for leaf in leaf_node_names:
        current = leaf
        # Traverse up the tree
        while current is not None:
            included_messages.add(current)
            current = get_parent_message(current)

    return included_messages
```

### Example Use Cases

**Use Case 1: Cardiology Application**
```
Requested: [MyocardialInfarction, CoronaryArteryDisease]

Automatically includes:
- MyocardialInfarction
- CoronaryArteryDisease
- CardiovascularDisease
- Disease
- All supporting messages (CardiacBiomarker, etc.)
```

**Use Case 2: Respiratory Medicine**
```
Requested: [Influenza, COVID19, Tuberculosis]

Automatically includes:
- Influenza
- COVID19
- RespiratoryViralInfection
- ViralInfection
- Tuberculosis
- BacterialInfection
- InfectiousDisease
- Disease
- All supporting messages
```

**Use Case 3: Neurology Application**
```
Requested: [AlzheimersDisease, ParkinsonsDisease, CerebralCortex]

Automatically includes:
- Disease hierarchy (AlzheimersDisease → NeurodegenerativeDisease → NeurologicalDisease → Disease)
- Anatomy hierarchy (CerebralCortex → CerebralLobe → CerebralHemisphere → Brain → CNS → NervousSystem)
- All supporting messages
```

## Benefits of This Approach

1. **Flexible granularity** - Users select only what they need
2. **Automatic completeness** - No missing parent definitions
3. **Consistent semantics** - Hierarchy guarantees proper typing
4. **Efficient storage** - No duplication of common fields
5. **Easy extension** - Add new leaves without changing structure
6. **Clear semantics** - Parent-child relationships explicit

## Next Steps

1. Expand remaining biomedical domains (clinical, molecular)
2. Create comprehensive social/organizational hierarchies
3. Build extensive information/knowledge taxonomies
4. Add physical/manufacturing hierarchies
5. Develop scientific methodology taxonomies
6. Implement tree-cutting selection tools

## Contributing

When adding new hierarchies:
1. Start with 3-5 major categories
2. Build 3-5 levels deep minimum
3. Include 10+ leaf nodes per branch
4. Add standard identifiers/references
5. Document relationships clearly
6. Test tree-cutting scenarios
