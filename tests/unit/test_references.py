"""
Unit tests for common references module.
"""

import pytest


class TestOntologyReference:
    """Tests for OntologyReference message."""

    def test_create_ontology_reference(self):
        """Test creating a generic ontology reference."""
        from proto.common import references_pb2

        ref = references_pb2.OntologyReference(
            ontology_name="GO",
            term_id="GO:0008150",
            term_label="biological_process",
            term_definition="A biological process...",
            version="2023-01-01"
        )
        assert ref.ontology_name == "GO"
        assert ref.term_id == "GO:0008150"


class TestMeSHReference:
    """Tests for MeSHReference message."""

    def test_create_mesh_reference(self):
        """Test creating a MeSH reference."""
        from proto.common import references_pb2

        mesh = references_pb2.MeSHReference(
            mesh_id="D010612",
            descriptor_name="Pharyngitis",
            tree_numbers=["C08.730", "C09.775"]
        )
        assert mesh.mesh_id == "D010612"
        assert mesh.descriptor_name == "Pharyngitis"
        assert len(mesh.tree_numbers) == 2


class TestGOReference:
    """Tests for GOReference message."""

    def test_create_go_reference(self):
        """Test creating a Gene Ontology reference."""
        from proto.common import references_pb2

        go = references_pb2.GOReference(
            go_id="GO:0008150",
            go_term="biological_process",
            aspect=references_pb2.GOReference.BIOLOGICAL_PROCESS,
            definition="Any process..."
        )
        assert go.go_id == "GO:0008150"
        assert go.aspect == references_pb2.GOReference.BIOLOGICAL_PROCESS


class TestSNOMEDCTReference:
    """Tests for SNOMEDCTReference message."""

    def test_create_snomed_reference(self):
        """Test creating a SNOMED CT reference."""
        from proto.common import references_pb2

        snomed = references_pb2.SNOMEDCTReference(
            concept_id="38341003",
            fully_specified_name="Hypertensive disorder (disorder)",
            preferred_term="Hypertension",
            semantic_tag="disorder"
        )
        assert snomed.concept_id == "38341003"
        assert snomed.preferred_term == "Hypertension"


class TestOntologyAnnotation:
    """Tests for OntologyAnnotation message."""

    def test_create_annotation(self):
        """Test creating an ontology annotation with evidence."""
        from proto.common import references_pb2

        term = references_pb2.OntologyReference(
            ontology_name="HP",
            term_id="HP:0000001",
            term_label="Test phenotype"
        )

        annotation = references_pb2.OntologyAnnotation(
            term=term,
            evidence_code="ECO:0000033",
            curator="John Doe",
            annotation_date="2024-01-15",
            confidence_score=0.95
        )
        assert annotation.term.term_id == "HP:0000001"
        assert annotation.confidence_score == 0.95
