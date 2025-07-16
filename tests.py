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

def test():
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)


if __name__ == "__main__":
    test()