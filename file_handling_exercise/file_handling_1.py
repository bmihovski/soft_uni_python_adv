from os import remove


def create_file(file_to_create):
    file = open(file_to_create, 'w')
    file.close()


def append_to_file(target_file, content):
    with open(target_file, 'a') as file_to_append:
        file_to_append.write(content + "\n")


def replace_file_content(target_file, content, replacement):
    try:
        file_to_read = open(target_file, 'r')
        file_content = file_to_read.read()
        file_to_read.close()
        new_data = file_content.replace(content, replacement)
        with open(target_file, 'w') as file_to_write:
            file_to_write.write(new_data)
    except FileNotFoundError:
        print("An error occurred")


def delete_file(target_file):
    try:
        remove(target_file)
    except FileNotFoundError:
        print("An error occurred")


while True:
    user_input = input()
    if user_input == "End":
        break
    user_inputs_parsed = user_input.split('-')
    command_name = user_inputs_parsed[0]
    file_name = user_inputs_parsed[1]

    if command_name == "Create":
        create_file(file_name)
        continue
    if command_name == "Add":
        append_to_file(file_name, *user_inputs_parsed[2:])
        continue
    if command_name == "Replace":
        replace_file_content(file_name, *user_inputs_parsed[2:])
        continue
    if command_name == "Delete":
        delete_file(file_name)
        continue
