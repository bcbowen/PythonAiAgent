import os 
#from pathlib import Path

def get_files_info(working_directory, directory=".") -> str:
    directory_path = os.path.abspath(os.path.join(working_directory, directory))
    working_path = os.path.abspath(working_directory)

    if not directory_path.startswith(working_path): 
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(directory_path): 
        return f'Error: "{directory}" is not a directory'
    
    output = []
    try: 
        with os.scandir(directory_path) as dir_info: 
            for item in dir_info:   
                file_stat = item.stat()
                output.append(f"- {item.name}: file_size={file_stat.st_size} bytes, is_dir={item.is_dir()} ")
            return "\n".join(output)
    except: 
        return "Error: Something strange is afoot"


"""
- README.md: file_size=1032 bytes, is_dir=False
- src: file_size=128 bytes, is_dir=True
- package.json: file_size=1234 bytes, is_dir=False
"""