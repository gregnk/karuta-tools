LICENSE_TEXT = '''
Copyright (c) 2025 Gregory Karastergios

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
'''

import csv
import sys

class Colnum:
    def __init__(self, name, index):
        self.name = name
        self.index = index

# True: Uses tabs to separate columns (easier to read, long entries are cut off)
# False: Uses dots to separate columns (uses less characters, better for longer entries)
USE_STRAIGHT_COLS = True

# Determines how many lines per message
HAS_NITRO = True
MAX_CHARS = 4000 if HAS_NITRO else 2000

# The tag where the cards are listed from
TAG = "for-sale"

# For debugging
PRINT_LINE_NOS = False

# Name, col width (if USE_STRAIGHT_COLS == True)
COLS = [
    Colnum("tag", 14),
    Colnum("wishlist", 16),
    Colnum("code", 0),
    Colnum("quality", 5),
    Colnum("edition", 2),
    Colnum("series", 4),
    Colnum("character", 3),
    Colnum("number", 1)
]

# Get the col index by name
def col_index(tag_name):
        for col in COLS:
            if (col.name == tag_name):
                return col.index

# Open the file
csv_file = open(sys.argv[1])

# Sort by series (descending)
csv_rows_unsorted = csv.reader(csv_file)
next(csv_rows_unsorted)
csv_rows = sorted(csv_rows_unsorted, key=lambda row: row[col_index("series")].capitalize(), reverse=False)
#csv_rows = sorted(csv_rows_unsorted, key=lambda row: int(row[col_index("wishlist")]), reverse=True)

chars = 0
line_no = 1
# Print each row
for row in csv_rows:
    
    # Get the col index by name
    def col_index_value(tag_name):
        return row[col_index(tag_name)]
    
    # Format each col into a table
    def print_col(print_str, col_size):

        if (USE_STRAIGHT_COLS):
            if (len(print_str) >= col_size):
                print_str = print_str[:col_size-4] + "..."

            tab_len = col_size - len(print_str)
            separator = " " * tab_len
        
        else:
            separator = " \u22C5 "

        return print_str + separator

    
    # Print each row which matches the tag
    if (col_index_value("tag") == TAG):

        print_str = ""

        if (USE_STRAIGHT_COLS): print_str += "`"
        print_str += print_col(f"\u2661{col_index_value("wishlist")}", 6)
        print_str += print_col(f"{col_index_value("code")}", 8)
        print_str += print_col(("\u2605" * int(col_index_value("quality"))) + ("\u2606" * (5 - int(col_index_value("quality")))), 7)
        print_str += print_col(f"#{col_index_value("number")}", 7)
        print_str += print_col(f"\u25C8{col_index_value("edition")}", 4)
        print_str += print_col(f"{col_index_value("series")}", 40) # You might need to increase the width for this one if you're selling isekais, lol
        print_str += f"{col_index_value("character")}"
        if (USE_STRAIGHT_COLS): print_str += "`"

        print_str += "\n" # Include newline in char count

        # Check the character limit
        if ((chars + len(print_str)) > MAX_CHARS - 100):
            #print(chars)
            print("=" * 120)
            chars = len(print_str)
            
        else:
            chars += len(print_str)
        
        if (PRINT_LINE_NOS):
            line_no_str = f"{line_no}. "
            print(line_no_str + " " * (8-len(line_no_str)), end="")

        print(print_str, end="")
        line_no += 1


