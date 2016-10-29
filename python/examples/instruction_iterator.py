#!/usr/bin/env python
# Copyright (c) 2015-2016 Vector 35 LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import sys
import binaryninja


if sys.platform.lower().startswith("linux"):
	bintype = "ELF"
elif sys.platform.lower() == "darwin":
	bintype = "Mach-O"
else:
	raise Exception("%s is not supported on this plugin" % sys.platform)

if len(sys.argv) > 1:
	target = sys.argv[1]
else:
	target = "/bin/ls"

bv = binaryninja.BinaryViewType[bintype].open(target)
bv.update_analysis_and_wait()

print "-------- %s --------" % target
print "START: 0x%x" % bv.start
print "ENTRY: 0x%x" % bv.entry_point
print "ARCH: %s" % bv.arch.name
print "\n-------- Function List --------"

""" print all the functions, their basic blocks, and their il instructions """
for func in bv.functions:
    print repr(func)
    for block in func.low_level_il:
        print "\t{0}".format(block)

        for insn in block:
            print "\t\t{0}".format(insn)


""" print all the functions, their basic blocks, and their mc instructions """
for func in bv.functions:
    print repr(func)
    for block in func:
        print "\t{0}".format(block)

        for insn in block:
            print "\t\t{0}".format(insn)