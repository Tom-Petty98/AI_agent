import os
import subprocess
from google.genai import types

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


# schema_run_python_file = types.FunctionDeclaration(
#     name="run_python_file",
#     description="Execute Python file with optional arguments with the given file path, constrained to the working directory.",
#     parameters=types.Schema(
#         type=types.Type.OBJECT,
#         properties={
#             "file_path": types.Schema(
#                 type=types.Type.STRING,
#                 description="The file path, relative to the working directory.",
#             ),
#             "args": types.Schema(
#                 type=types.Type.ARRAY,
#                 description="Optional additional string arguments that are executed along with the file to be run. If not provided, it will be an empty array.",
#             ),
#         },
#     ),
# )

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)