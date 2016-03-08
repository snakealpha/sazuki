"""
Support for google proto buffers.
"""
from os import linesep

from support import PrimitiveCollection, ValueType
from support.MetaGenerator import *

class CurrentPrimitiveCollection(PrimitiveCollection):
    type_names = [
        "int32",
        "int64",
        "uint32",
        "uint64",
        "sint32",
        "sint64",
        "bool",
        "fixed64",
        "sfixed64",
        "double",
        "string",
        "bytes",
        "fixed32",
        "sfixed32",
        "float",
    ]

def generate_structure(struct_descriptor, depth=0, parsed_structs=None):
    if not (isinstance(struct_descriptor, StructDescriptor)):
        raise TypeError('enum_descriptor argument must be a instance of StructDescriptor.')

    if parsed_structs == None:
        parsed_structs = list()

    content = "%(wrap)smessage %(name)s%(nl)s%(wrap)s{%(nl)s" % {"wrap":"    " * depth,
                                                                "name":struct_descriptor.name,
                                                                "nl":linesep}

    for field in struct_descriptor.fields:
        if field.type == ValueType.enum and not field.struct_type.is_global and field.struct_type not in parsed_structs:
            parsed_structs.append(field.struct_type)
            content += generate_enum(field.struct_type, depth + 1)
        elif field.type == ValueType.structure and not field.struct_type.is_global and field.struct_type not in parsed_structs:
            parsed_structs.append(field.struct_type)
            content += generate_structure(field.struct_type, depth + 1, parsed_structs)

        content += generate_field(field, depth + 1)

    content += "    " * depth + "}" + linesep
    return content

def generate_enum(enum_descriptor, depth=0):
    if not (isinstance(enum_descriptor, EnumDescriptor)):
        raise TypeError('enum_descriptor argument must be a instance of EnumDescriptor.')

    content = ""
    for (name, value) in enum_descriptor.fields.items():
        content += ("%s%s = %d" % ("    " * depth + 1, name, value)) + linesep

    return "%(wrap)senum %(name)s%(nl)s%(wrap)s{%(nl)s%(content)s%(nl)s%(wrap)s}%(nl)s" % { "wrap":"    " * depth, 
                                                                                            "name":enum_descriptor.name, 
                                                                                            "content":content,
                                                                                            "nl":linesep}

def generate_field(field_descriptor, depth=0):
    if not (isinstance(field_descriptor, FieldDescriptor)):
        raise TypeError('field_descriptor argument must be a instance of FieldDescriptor.')

    field_descriptor.check_vaild()

    return "%s%s %s %s = %d;%s" % ("    " * depth, 
                             "repeated" if field_descriptor.is_collection else ("optional" if field_descriptor.is_optional else "required"), 
                             field_descriptor.type if (field_descriptor.type != ValueType.structure and field_descriptor.type!=ValueType.enum) else field_descriptor.struct_type.name,
                             field_descriptor.field_name, 
                             field_descriptor.field_index,
                             linesep)
