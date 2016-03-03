from support.protobuf import *

sub_type = StructDescriptor()
sub_type.name = "subType1"

field = FieldDescriptor()
field.field_index = 1
field.field_name = "test1"
field.type = ValueType.double
sub_type.fields.append(field)

field = FieldDescriptor()
field.field_index = 2
field.field_name = "test2"
field.type = ValueType.int32
sub_type.fields.append(field)

new_type = StructDescriptor()
new_type.name = "Type1"