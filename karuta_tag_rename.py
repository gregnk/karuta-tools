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

print("Current name: ", end="")
CURRENT_NAME = input()

print("New name: ", end="")
NEW_NAME = input()

print("New icon (leave blank if tag already exists): ", end="")
NEW_ICON = input()

# print("New icon (leave blank if tag already exists): ", end="")
# EXCLUDE = input()

print("")

# Open the file
csv_file = open("spreadsheet.csv")

csv_rows = csv.reader(csv_file)

KT = "kt {} ".format(NEW_NAME)
tag_commands = [KT]
tag_command_index = 0
card_count = 0

for row in csv_rows:

    if (row[14] == CURRENT_NAME):
        tag_commands[tag_command_index] += row[0] + " "

        card_count += 1

        if (card_count % 50 == 0):
            tag_command_index += 1
            tag_commands.append(KT)

# Generate the delete command
command_count = 1

if (NEW_ICON != ""):
    create_command = "ktc {} :{}:".format(NEW_NAME, NEW_ICON)
    print("{}.\t{}\n".format(command_count, create_command))

    command_count += 1

for command in tag_commands:
    print("{}.\t{}\n".format(command_count, command))
    command_count += 1

delete_command = "ktagdelete {}".format(CURRENT_NAME)
print("{}.\t{}\n".format(command_count, delete_command))