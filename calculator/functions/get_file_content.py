import os

def get_file_content(working_directory, file_path):
    working_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))


    if not abs_file_path.startswith(working_path): 
        result = f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        print(result)
        return result

    if not os.path.isfile(abs_file_path): 
        result = f'Error: File not found or is not a regular file: "{file_path}"'
        print(result)
        return result