from enum import Enum

class BaseValueType(Enum):
    """
    Value Type that must included in a Sazuki ValueType enum.
    """
    structure = "sazuki.ValueType.Struct"
    enum = "sazuki.ValueType.Enum"
    not_assigned = "sazuki.ValueType.not_assigned"
