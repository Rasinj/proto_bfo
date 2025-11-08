"""
Unit tests for common units module.
"""

import pytest


class TestQuantityValue:
    """Tests for QuantityValue message."""

    def test_create_with_si_base(self):
        """Test creating quantity with SI base unit."""
        from proto.common import units_pb2

        qty = units_pb2.QuantityValue(
            value=5.0,
            si_base=units_pb2.SIBaseUnit.METER,
            uncertainty=0.01
        )
        assert qty.value == 5.0
        assert qty.si_base == units_pb2.SIBaseUnit.METER
        assert qty.uncertainty == 0.01

    def test_create_with_common_unit(self):
        """Test creating quantity with common unit."""
        from proto.common import units_pb2

        qty = units_pb2.QuantityValue(
            value=100.0,
            common=units_pb2.CommonUnit.KILOGRAM
        )
        assert qty.value == 100.0
        assert qty.common == units_pb2.CommonUnit.KILOGRAM

    def test_create_with_si_derived(self):
        """Test creating quantity with SI derived unit."""
        from proto.common import units_pb2

        qty = units_pb2.QuantityValue(
            value=9.8,
            si_derived=units_pb2.SIDerivedUnit.NEWTON
        )
        assert qty.value == 9.8
        assert qty.si_derived == units_pb2.SIDerivedUnit.NEWTON


class TestPhysicalQuantity:
    """Tests for PhysicalQuantity message."""

    def test_create_physical_quantity(self):
        """Test creating a physical quantity."""
        from proto.common import units_pb2

        qty_val = units_pb2.QuantityValue(
            value=70.0,
            common=units_pb2.CommonUnit.KILOGRAM
        )
        phys_qty = units_pb2.PhysicalQuantity(
            quantity=qty_val,
            dimension_name="mass"
        )
        assert phys_qty.quantity.value == 70.0
        assert phys_qty.dimension_name == "mass"


class TestUnitDimension:
    """Tests for UnitDimension message."""

    def test_create_unit_dimension(self):
        """Test creating a custom unit dimension."""
        from proto.common import units_pb2

        # Create m/s (velocity)
        dim = units_pb2.UnitDimension(
            symbol="m/s",
            base_units=[units_pb2.SIBaseUnit.METER, units_pb2.SIBaseUnit.SECOND],
            exponents=[1, -1],
            scale_factor=1.0
        )
        assert dim.symbol == "m/s"
        assert len(dim.base_units) == 2
        assert len(dim.exponents) == 2


class TestQuantityRange:
    """Tests for QuantityRange message."""

    def test_create_quantity_range(self):
        """Test creating a quantity range."""
        from proto.common import units_pb2

        min_val = units_pb2.QuantityValue(
            value=36.0,
            common=units_pb2.CommonUnit.CELSIUS
        )
        max_val = units_pb2.QuantityValue(
            value=38.0,
            common=units_pb2.CommonUnit.CELSIUS
        )
        typical = units_pb2.QuantityValue(
            value=37.0,
            common=units_pb2.CommonUnit.CELSIUS
        )

        range_qty = units_pb2.QuantityRange(
            min_value=min_val,
            max_value=max_val,
            typical_value=typical
        )
        assert range_qty.min_value.value == 36.0
        assert range_qty.max_value.value == 38.0
        assert range_qty.typical_value.value == 37.0


class TestVectorQuantity:
    """Tests for VectorQuantity message."""

    def test_create_vector_quantity(self):
        """Test creating a vector quantity."""
        from proto.common import units_pb2

        vec = units_pb2.VectorQuantity(
            components=[1.0, 2.0, 3.0],
            si_base=units_pb2.SIBaseUnit.METER,
            coordinate_system="cartesian"
        )
        assert len(vec.components) == 3
        assert vec.components[0] == 1.0
        assert vec.coordinate_system == "cartesian"
