"""
Unit tests for core BFO message types.
"""

import pytest
from google.protobuf.timestamp_pb2 import Timestamp
import time


class TestContinuant:
    """Tests for Continuant message."""

    def test_create_continuant(self):
        """Test creating a basic continuant."""
        from proto.core import bfo_core_pb2

        continuant = bfo_core_pb2.Continuant(description="Test continuant")
        assert continuant.description == "Test continuant"

    def test_continuant_empty_description(self):
        """Test creating continuant with empty description."""
        from proto.core import bfo_core_pb2

        continuant = bfo_core_pb2.Continuant()
        assert continuant.description == ""


class TestOccurrent:
    """Tests for Occurrent message."""

    def test_create_occurrent(self, sample_continuant, sample_timestamp):
        """Test creating a basic occurrent."""
        from proto.core import bfo_core_pb2

        occurrent = bfo_core_pb2.Occurrent(
            description="Test occurrent",
            participants=[sample_continuant],
            datetime=sample_timestamp
        )
        assert occurrent.description == "Test occurrent"
        assert len(occurrent.participants) == 1
        assert occurrent.HasField("datetime")

    def test_occurrent_multiple_participants(self, sample_timestamp):
        """Test occurrent with multiple participants."""
        from proto.core import bfo_core_pb2

        p1 = bfo_core_pb2.Continuant(description="Participant 1")
        p2 = bfo_core_pb2.Continuant(description="Participant 2")

        occurrent = bfo_core_pb2.Occurrent(
            description="Multi-participant event",
            participants=[p1, p2],
            datetime=sample_timestamp
        )
        assert len(occurrent.participants) == 2


class TestProcess:
    """Tests for Process message."""

    def test_create_process(self, sample_continuant, sample_process_boundary):
        """Test creating a process with boundaries."""
        from proto.core import bfo_core_pb2

        process = bfo_core_pb2.Process(
            description="Test process",
            participants=[sample_continuant],
            start_process_boundary=sample_process_boundary
        )
        assert process.description == "Test process"
        assert process.HasField("start_process_boundary")

    def test_process_with_end_boundary(self, sample_continuant, past_timestamp, sample_timestamp):
        """Test process with both start and end boundaries."""
        from proto.core import bfo_core_pb2

        start = bfo_core_pb2.ProcessBoundary(
            description="Start",
            timestamp=past_timestamp
        )
        end = bfo_core_pb2.ProcessBoundary(
            description="End",
            timestamp=sample_timestamp
        )

        process = bfo_core_pb2.Process(
            description="Complete process",
            participants=[sample_continuant],
            start_process_boundary=start,
            end_process_boundary=end
        )
        assert process.HasField("start_process_boundary")
        assert process.HasField("end_process_boundary")


class TestProcessBoundary:
    """Tests for ProcessBoundary message."""

    def test_create_process_boundary(self, sample_timestamp):
        """Test creating a process boundary."""
        from proto.core import bfo_core_pb2

        boundary = bfo_core_pb2.ProcessBoundary(
            description="Birth event",
            timestamp=sample_timestamp
        )
        assert boundary.description == "Birth event"
        assert boundary.HasField("timestamp")


class TestTemporalRegion:
    """Tests for TemporalRegion message."""

    def test_create_temporal_region(self, past_timestamp, sample_timestamp):
        """Test creating a temporal region."""
        from proto.core import bfo_core_pb2

        region = bfo_core_pb2.TemporalRegion(
            description="Time interval",
            start_timestamp=past_timestamp,
            end_timestamp=sample_timestamp
        )
        assert region.HasField("start_timestamp")
        assert region.HasField("end_timestamp")


class TestSpatialRegion:
    """Tests for SpatialRegion message."""

    def test_create_spatial_region(self):
        """Test creating a spatial region."""
        from proto.core import bfo_core_pb2

        region = bfo_core_pb2.SpatialRegion(
            description="Room 302",
            placeholder_spatialregiondata="coordinates here"
        )
        assert region.description == "Room 302"


class TestSpatioTemporalRegion:
    """Tests for SpatioTemporalRegion message."""

    def test_create_spatiotemporal_region(self, past_timestamp, sample_timestamp):
        """Test creating a spatiotemporal region."""
        from proto.core import bfo_core_pb2

        spatial = bfo_core_pb2.SpatialRegion(description="Location")
        temporal = bfo_core_pb2.TemporalRegion(
            description="Duration",
            start_timestamp=past_timestamp,
            end_timestamp=sample_timestamp
        )

        st_region = bfo_core_pb2.SpatioTemporalRegion(
            description="Event location",
            temporal_region=temporal,
            spatial_region=spatial
        )
        assert st_region.HasField("temporal_region")
        assert st_region.HasField("spatial_region")


class TestMaterialEntity:
    """Tests for MaterialEntity message."""

    def test_create_material_entity(self):
        """Test creating a material entity."""
        from proto.core import bfo_core_pb2

        entity = bfo_core_pb2.MaterialEntity(
            continuant=bfo_core_pb2.Continuant(description="Physical object")
        )
        assert entity.continuant.description == "Physical object"


class TestQuality:
    """Tests for Quality message."""

    def test_create_quality(self):
        """Test creating a quality."""
        from proto.core import bfo_core_pb2

        quality = bfo_core_pb2.Quality(
            continuant=bfo_core_pb2.Continuant(description="Color quality")
        )
        assert quality.continuant.description == "Color quality"


class TestRelationalQuality:
    """Tests for RelationalQuality message."""

    def test_create_relational_quality(self):
        """Test creating a relational quality."""
        from proto.core import bfo_core_pb2

        giver = bfo_core_pb2.Continuant(description="Parent")
        receiver = bfo_core_pb2.Continuant(description="Child")

        relation = bfo_core_pb2.RelationalQuality(
            description="Parent-child relationship",
            relational_giver=giver,
            relational_receiver=receiver,
            invert_relation=False
        )
        assert relation.description == "Parent-child relationship"
        assert relation.relational_giver.description == "Parent"
        assert relation.relational_receiver.description == "Child"


class TestHistory:
    """Tests for History message."""

    def test_create_history(self, sample_continuant, past_timestamp, sample_timestamp):
        """Test creating a history."""
        from proto.core import bfo_core_pb2

        spatial = bfo_core_pb2.SpatialRegion(description="Location")
        temporal = bfo_core_pb2.TemporalRegion(
            start_timestamp=past_timestamp,
            end_timestamp=sample_timestamp
        )
        st_region = bfo_core_pb2.SpatioTemporalRegion(
            temporal_region=temporal,
            spatial_region=spatial
        )

        history = bfo_core_pb2.History(
            description="Life history",
            participant=sample_continuant,
            spatiotemporal_region=st_region
        )
        assert history.HasField("participant")
        assert history.HasField("spatiotemporal_region")
