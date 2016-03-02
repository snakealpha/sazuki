"""
Support for google proto buffers.
"""
from os import linesep

from support import BaseValueType
from support.MetaGenerator import *

class ValueType(BaseValueType):
    int32 = "int32"
    int64 = "int64"
    uint32 = "uint32"
    uint64 = "uint64"
    sint32 = "sint32"
    sint64 = "sint64"
    bool = "bool"
    fixed64 = "fixed64"
    sfixed64 = "sfixed64"
    double = "double"
    string = "string"
    bytes = "bytes"
    fixed32 = "fixed32"
    sfixed32 = "sfixed32"
    float = "float"

def generate_structure(struct_descriptor, descriptor_list, depth = 0):
    # TODO: to be implemented.
    pass

def generate_enum(enum_descriptor, depth = 0):
    if not (enum_descriptor is EnumDescriptor):
        raise TypeError('enum_descriptor argument must be a instance of EnumDescriptor.')

    content = ""
    for (name, value) in enum_descriptor.fields.items():
        content += ("%s%s = %d" % ("    " * depth + 1, name, value)) + linesep

    return "%(wrap)enum %(name)%(nl)%(wrap){%(nl)%(content)%(nl)%(wrap)}%(nl)" % {wrap:"    " * depth, 
                                                                                  name:enum_descriptor.name, 
                                                                                  content:content,
                                                                                  nl:linesep}

def generate_field(field_descriptor, depth = 0):
    if not (field_descriptor is FieldDescriptor):
        raise TypeError('field_descriptor argument must be a instance of FieldDescriptor.')

    field_descriptor.check_vaild()

    return "%s%s %s = %d;" % ("    " * depth, 
                             "repeated" if field_descriptor.is_collection else ("optional" if field_descriptor.is_optional else "required"), 
                             field_descriptor.field_name, 
                             field_descriptor.field_index)
