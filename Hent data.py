import csv
import os

# Get the current working directory
path = os.getcwd()

# Specify the file name
file_name = '201m (0).txt'

# Construct the full path to the file
file_A = os.path.join(path, file_name)

def read_file(file_A, delimiter=',', chunk_size=100000):

    data = []
    with open(file_A, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=delimiter)
        chunk = []
        for i, row in enumerate(reader):
            chunk.append(row)
            if (i + 1) % chunk_size == 0:
                data.extend(chunk)
                chunk = []  # Clear the chunk to save memory
        if chunk:  # Add the last chunk if it's not empty
            data.extend(chunk)
    return data

# Read the file
data = read_file(file_A)
# Print the first 10 rows
for row in data[:10]:
    print(row)
