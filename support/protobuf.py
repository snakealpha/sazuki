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

def generate_structure(struct_descriptor, depth=0):
    if not (struct_descriptor is StructDescriptor):
        raise TypeError('enum_descriptor argument must be a instance of StructDescriptor.')

    parsed_structs = list()
    content = "%(wrap)message %(name)%(nl)%(wrap){%(nl)" % {"wrap":"    " * depth,
                                                            "name":struct_descriptor.name,
                                                            "nu":linesep}

    for field in struct_descriptor.fields:
        if field.type == ValueType.enum and not field.struct_type.is_global and field.struct_type not in parsed_structs:
            parsed_structs.append(field.struct_type)
            content += generate_enum(field.struct_type, depth + 1)
        elif field.type == ValueType.struct and not field.struct_type.is_global and field.struct_type not in parsed_structs:
            parsed_structs.append(field.struct_type)
            content += generate_struct(field.struct_type, depth + 1)

        content += generate_field(field, depth + 1)

    content += "    " * depth + "}" + linesep
    return content

def generate_enum(enum_descriptor, depth=0):
    if not (enum_descriptor is EnumDescriptor):
        raise TypeError('enum_descriptor argument must be a instance of EnumDescriptor.')

    content = ""
    for (name, value) in enum_descriptor.fields.items():
        content += ("%s%s = %d" % ("    " * depth + 1, name, value)) + linesep

    return "%(wrap)enum %(name)%(nl)%(wrap){%(nl)%(content)%(nl)%(wrap)}%(nl)" % {"wrap":"    " * depth, 
                                                                                  "name":enum_descriptor.name, 
                                                                                  "content":content,
                                                                                  "nl":linesep}

def generate_field(field_descriptor, depth=0):
    if not (field_descriptor is FieldDescriptor):
        raise TypeError('field_descriptor argument must be a instance of FieldDescriptor.')

    field_descriptor.check_vaild()

    return "%s%s %s = %d;%s" % ("    " * depth, 
                             "repeated" if field_descriptor.is_collection else ("optional" if field_descriptor.is_optional else "required"), 
                             field_descriptor.field_name if field_descriptor.type != ValueType.structure and field_descriptor.type != ValueType.enum else field_descriptor.struct_type.name, 
                             field_descriptor.field_index,
                             linesep)
