"""
Unit tests for common identifiers module.
"""

import pytest


class TestURI:
    """Tests for URI message."""

    def test_create_uri(self):
        """Test creating a URI."""
        from proto.common import identifiers_pb2

        uri = identifiers_pb2.URI(
            uri="https://example.com/resource?key=value#section",
            scheme="https",
            authority="example.com",
            path="/resource",
            query="key=value",
            fragment="section"
        )
        assert uri.uri == "https://example.com/resource?key=value#section"
        assert uri.scheme == "https"


class TestDOI:
    """Tests for DOI message."""

    def test_create_doi(self):
        """Test creating a DOI."""
        from proto.common import identifiers_pb2

        doi = identifiers_pb2.DOI(
            identifier="10.1038/s41586-020-1234-5"
        )
        assert doi.identifier == "10.1038/s41586-020-1234-5"


class TestORCID:
    """Tests for ORCID message."""

    def test_create_orcid(self):
        """Test creating an ORCID."""
        from proto.common import identifiers_pb2

        orcid = identifiers_pb2.ORCID(
            identifier="0000-0002-1825-0097",
            display_name="Dr. Jane Smith"
        )
        assert orcid.identifier == "0000-0002-1825-0097"
        assert orcid.display_name == "Dr. Jane Smith"


class TestMedicalIdentifier:
    """Tests for MedicalIdentifier message."""

    def test_create_with_icd10(self):
        """Test creating medical identifier with ICD-10 code."""
        from proto.common import identifiers_pb2

        med_id = identifiers_pb2.MedicalIdentifier(
            icd10_code="J02.9"
        )
        assert med_id.icd10_code == "J02.9"

    def test_create_with_mesh(self):
        """Test creating medical identifier with MeSH ID."""
        from proto.common import identifiers_pb2

        med_id = identifiers_pb2.MedicalIdentifier(
            mesh_id="D010612"
        )
        assert med_id.mesh_id == "D010612"


class TestBiologicalIdentifier:
    """Tests for BiologicalIdentifier message."""

    def test_create_with_uniprot(self):
        """Test creating biological identifier with UniProt ID."""
        from proto.common import identifiers_pb2

        bio_id = identifiers_pb2.BiologicalIdentifier(
            uniprot_id="P12345"
        )
        assert bio_id.uniprot_id == "P12345"

    def test_create_with_ncbi_gene(self):
        """Test creating biological identifier with NCBI Gene ID."""
        from proto.common import identifiers_pb2

        bio_id = identifiers_pb2.BiologicalIdentifier(
            ncbi_gene_id="672"
        )
        assert bio_id.ncbi_gene_id == "672"


class TestChemicalIdentifier:
    """Tests for ChemicalIdentifier message."""

    def test_create_with_cas(self):
        """Test creating chemical identifier with CAS number."""
        from proto.common import identifiers_pb2

        chem_id = identifiers_pb2.ChemicalIdentifier(
            cas_number="50-00-0"
        )
        assert chem_id.cas_number == "50-00-0"

    def test_create_with_smiles(self):
        """Test creating chemical identifier with SMILES."""
        from proto.common import identifiers_pb2

        chem_id = identifiers_pb2.ChemicalIdentifier(
            smiles="CCO"
        )
        assert chem_id.smiles == "CCO"


class TestUUID:
    """Tests for UUID message."""

    def test_create_uuid(self):
        """Test creating a UUID."""
        from proto.common import identifiers_pb2

        uuid = identifiers_pb2.UUID(
            uuid="550e8400-e29b-41d4-a716-446655440000",
            version=4
        )
        assert uuid.uuid == "550e8400-e29b-41d4-a716-446655440000"
        assert uuid.version == 4
