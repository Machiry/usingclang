__author__ = 'machiry'

import sys
import clang.cindex
import IPython

index = clang.cindex.Index.create()
tu = index.parse('examples/temp_test.c')
print tu.spelling
for curr_child in tu.cursor.get_children():
    if curr_child.spelling == 'myfunc':
        IPython.embed()
