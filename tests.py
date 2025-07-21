# import unittest
from functions.get_files_info import get_files_info

# class TestGetFilesInfo(unittest.TestCase):
#     def test_get_files_calculator_directory(self):
#         result = get_files_info("calculator", ".")
#         self.assertEqual(result, " - main.py: file_size=564 bytes, is_dir=False\n"
#         " - tests.py: file_size=1330 bytes, is_dir=False\n"
#         " - pkg: file_size=4096 bytes, is_dir=True")

#     def test_get_files_pkg_directory(self):
#         result = get_files_info("calculator", "pkg")
#         self.assertEqual(result, " - calculator.py: file_size=1720 bytes, is_dir=False\n"
#         " - render.py: file_size=753 bytes, is_dir=False\n"
#         " - __pycache__: file_size=4096 bytes, is_dir=True")

#     def test_get_files_bin_directory(self):
#         result = get_files_info("calculator", "/bin")
#         self.assertEqual(result, "Error: Cannot list \"/bin\" as it is outside the permitted working directory")

#     def test_get_files_error(self):
#         result = get_files_info("calculator", "../")
#         self.assertEqual(result, "Error: Cannot list \"../\" as it is outside the permitted working directory")

# if __name__ == "__main__":
#     unittest.main()

# def test():
#     result = get_files_info("calculator", ".")
#     print("Result for current directory:")
#     print(result)
#     print("")

#     result = get_files_info("calculator", "pkg")
#     print("Result for 'pkg' directory:")
#     print(result)

#     result = get_files_info("calculator", "/bin")
#     print("Result for '/bin' directory:")
#     print(result)

#     result = get_files_info("calculator", "../")
#     print("Result for '../' directory:")
#     print(result)

# if __name__ == "__main__":
#     test()

# from functions.get_file_info import get_file_content

# def test():
#     # print(get_file_content("calculator", "lorem.txt"))
#     print(get_file_content("calculator", "main.py"))
#     print(get_file_content("calculator", "pkg/calculator.py"))
#     print(get_file_content("calculator", "/bin/cat"))
#     print(get_file_content("calculator", "pkg/does_not_exist.py"))

# if __name__ == "__main__":
#     test()


# from functions.write_file import write_file

# def test():
#     print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
#     print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
#     print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

# if __name__ == "__main__":
#     test()

from functions.run_python import run_python_file

def test():
    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))

if __name__ == "__main__":
    test()