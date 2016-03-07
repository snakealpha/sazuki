from enum import Enum

class ValueType(Enum):
    """
    Value Type that must included in a Sazuki ValueType enum.
    """
    structure = "sazuki.ValueType.Struct"
    enum = "sazuki.ValueType.Enum"
    primitive = "sazuki.ValueType.primitive"
    not_assigned = "sazuki.ValueType.not_assigned"

class PrimitiveCollection:
    type_names = list()
