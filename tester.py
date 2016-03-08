from support.protobuf import *
from support import *

sub_type = StructDescriptor()
sub_type.is_global = False
sub_type.name = "subType1"

field = FieldDescriptor()
field.field_index = 1
field.field_name = "test1"
field.type = "uint32"
sub_type.fields.append(field)

field = FieldDescriptor()
field.field_index = 2
field.is_collection = True
field.field_name = "test2"
field.type = "uint32"
sub_type.fields.append(field)

new_type = StructDescriptor()
new_type.name = "Type1"

field = FieldDescriptor()
field.field_index = 3
field.field_name = "structure_field_1"
field.type = ValueType.structure
field.struct_type = sub_type
new_type.fields.append(field)

res = new_type.generate_meta()
print(res)