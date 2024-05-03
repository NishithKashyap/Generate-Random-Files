import os
import random
import string

# generate random text data
def generate_random_text(size):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))

# create a text file with random data
def create_random_text_file(file_path, size):
    with open(file_path, 'w') as file:
        file.write(generate_random_text(size))

def create_file(file_index, output_folder, min_size, max_size):
    os.makedirs(output_folder, exist_ok=True)

    file_size = random.randint(min_size, max_size)

    file_name = f'file_{file_index}.txt'
    file_path = os.path.join(output_folder, file_name)

    create_random_text_file(file_path, file_size)
    
    print(f"File {file_name} created")
