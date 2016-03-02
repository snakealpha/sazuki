"""
Generator of meta objects of structs.
"""

import imp

# TODO: import of the serializer will happend from outer caller,this line should be deleted while released.
from support.protobuf import *

class FieldDescriptor:
    """
    Used to descript a field in a struct.
    """
    type = ValueType(ValueType.not_assigned)
    struct_type = None
    is_collection = False
    is_optional = False
    field_name = ""
    field_index = 0

    def check_vaild(self):
        """
        Check if current field can generate a meta string currect.
        """
        if type == ValueType.not_assigned:
            raise ValueError('Have not assign a type to a field.')
        if field_index <= 0:
            raise ValueError('Index of a field is 0.')
        if not field_name:
            raise ValueError('A field must have a name')
        if type == ValueType.structure and not struct_type:
            raise ValueError('Field type is a struct, but struct type is not assigned.')

        pass

    def generate_meta(self, depth = 0):
        """
        Return generated meta string.
        """
        generate_field(self, depth)
        pass

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
        generate_struct(self, depth)
        pass

class EnumDescriptor(StructDescriptor):
    """
    Used to descript a enum.
    """
    fields = dict()

    def generate_meta(self, depth = 0):
        """
        Return generated meta string.
        """
        generate_enum(self, depth)
        pass
    