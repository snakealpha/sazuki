"""
Used to parse meta data from table or external files, and generate meta files.
"""

from support.MetaGenerator import *

class Record:
    """
    To descripe a record.
    A record may serialize from a row in a table, or combained from multi rows from any number of tables.
    """
    table_context = None        # The table where this record come from.
    content = dict()            # Restore field and content from table. Key is FieldDescriptor, Value is content read from table.

    pass

class OutputFile:
    """
    To descripe a file restore processed data.
    Only one struct per file.
    """
    relative_path = ""
    file_name = "file.data"    
    struct_descriptor = None    # Must be a StructDescriptor.

    pass

class TableContext:
    """
    Information used to generate a table, including output infomation and indexing relation between reocrds.
    """
    output_file_info = None     # Must be a OutputFile.
    column_map = dict()         # A dict used to descripe the mapping from a column to a field. Key as a column index, and Value as a FieldDescriptor in output_file_info.

    pass

