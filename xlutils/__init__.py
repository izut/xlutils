# Copyright (c) 2008 Simplistix Ltd
#
# This Software is released under the MIT License:
# http://www.opensource.org/licenses/mit-license.html
# See license.txt for more details.


def copy_sheet(from_sheet, to_sheet):
    """
    
    """
    for k, v in from_sheet.__dict__.items():
        if k != '_Worksheet__name':
            setattr(to_sheet, k, v)
    return to_sheet
