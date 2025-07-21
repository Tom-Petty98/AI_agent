import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if file_path[-3::] != ".py":
        f'Error: "{file_path}" is not a Python file.'

    try:
        complete_process = subprocess.run(
            ["python", abs_file_path, *args],                                         
            capture_output=True,
            text=True,
            timeout=30,
            cwd=abs_working_dir,
        )

        if complete_process.returncode != 0:
            return f"Process exited with code {complete_process.returncode}"
        if not complete_process.stdout:
            return "No output produced"
        
        return f"STDOUT: {complete_process.stdout} STDERR: {complete_process.stderr}"
    
    except Exception as e:
        return f"Error: executing Python file: {e}"

