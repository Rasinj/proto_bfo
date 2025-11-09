"""
Pytest configuration and shared fixtures for proto_bfo tests.
"""

import pytest
import time
from google.protobuf.timestamp_pb2 import Timestamp


@pytest.fixture
def sample_timestamp():
    """Provides a sample timestamp for testing."""
    return Timestamp(seconds=int(time.time()))


@pytest.fixture
def past_timestamp():
    """Provides a timestamp from the past."""
    return Timestamp(seconds=int(time.time()) - 86400)  # 1 day ago


@pytest.fixture
def future_timestamp():
    """Provides a timestamp in the future."""
    return Timestamp(seconds=int(time.time()) + 86400)  # 1 day from now


@pytest.fixture
def sample_continuant():
    """Provides a sample Continuant for testing."""
    try:
        from proto.core import bfo_core_pb2
        return bfo_core_pb2.Continuant(description="Test continuant")
    except ImportError:
        pytest.skip("Proto files not compiled")


@pytest.fixture
def sample_material_entity():
    """Provides a sample MaterialEntity for testing."""
    try:
        from proto.core import bfo_core_pb2
        return bfo_core_pb2.MaterialEntity(
            continuant=bfo_core_pb2.Continuant(description="Test material entity")
        )
    except ImportError:
        pytest.skip("Proto files not compiled")


@pytest.fixture
def sample_process_boundary(sample_timestamp):
    """Provides a sample ProcessBoundary for testing."""
    try:
        from proto.core import bfo_core_pb2
        return bfo_core_pb2.ProcessBoundary(
            description="Test boundary",
            timestamp=sample_timestamp
        )
    except ImportError:
        pytest.skip("Proto files not compiled")


@pytest.fixture
def sample_process(sample_continuant, sample_process_boundary):
    """Provides a sample Process for testing."""
    try:
        from proto.core import bfo_core_pb2
        return bfo_core_pb2.Process(
            description="Test process",
            participants=[sample_continuant],
            start_process_boundary=sample_process_boundary
        )
    except ImportError:
        pytest.skip("Proto files not compiled")


@pytest.fixture
def sample_quantity_value():
    """Provides a sample QuantityValue for testing."""
    try:
        from proto.common import units_pb2
        return units_pb2.QuantityValue(
            value=100.0,
            si_base=units_pb2.SIBaseUnit.KILOGRAM,
            uncertainty=0.1
        )
    except ImportError:
        pytest.skip("Proto files not compiled")
