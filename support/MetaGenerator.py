"""
Generator of meta objects of structs.
"""
import imp
from importlib import import_module

from support import *

# TODO: import of the serializer will happend from outer caller,this line should be deleted while released.
protocol_module = import_module("support.protobuf")


class FieldDescriptor:
    """
    Used to descript a field in a struct.
    """
    type = ValueType.not_assigned
    struct_type = None
    is_collection = False
    is_optional = False
    field_name = ""
    field_index = 0

    def check_vaild(self):
        """
        Check if current field can generate a meta string currect.
        """
        if self.type == ValueType.not_assigned:
            raise ValueError('Have not assign a type to a field.')
        if self.field_index <= 0:
            raise ValueError('Index of a field is 0.')
        if not self.field_name:
            raise ValueError('A field must have a name')
        if self.type == ValueType.structure and not self.struct_type:
            raise ValueError('Field type is a struct, but struct type is not assigned.')

        pass

    def generate_meta(self, depth = 0):
        """
        Return generated meta string.
        """
        return protocol_module.generate_field(self, depth)

class StructDescriptor:
    """
    Used to descript a struct.
    """
    fields = list()
    name = ""
    is_global = True

    def generate_meta(self, depth = 0):
        """
        Return generated meta string.
        """
        return protocol_module.generate_structure(self, depth)

class EnumDescriptor(StructDescriptor):
    """
    Used to descript a enum.
    """
    fields = dict()

    def generate_meta(self, depth = 0):
        """
        Return generated meta string.
        """
        return protocol_module.generate_enum(self, depth)
    