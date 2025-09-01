import unittest
from calculator.functions.get_files_info import get_files_info
from typing import List


class TestGetFilesInfo(unittest.TestCase):

    def get_lines(self, text: str) -> List[str]: 
        return text.split('\n')
    
    def get_names(self, lines: List[str]) -> List[str]: 
        names = []
        for line in lines: 
            fields = line.split(':')
            if len(fields) == 2: 
                names.append(fields[0][2:])
        return names

    
    def test_current_directory(self):
        result = get_files_info("calculator", ".")
        lines = self.get_lines(result)
        expected = ['main.py', 'tests.py', 'pkg']
        actual_names = self.get_names(lines)
        for name in expected: 
            self.assertTrue(name in actual_names)       

    def test_pkg_directory(self):
        result = get_files_info("calculator", "pkg")
        lines = self.get_lines(result)
        expected = ['calculator.py', 'render.py']
        actual_names = self.get_names(lines)
        for name in expected: 
            self.assertTrue(name in actual_names)

    def test_out_of_bounds(self):
        result = get_files_info("calculator", "/bin")
        self.assertEqual(result, 'Error: Cannot list "/bin" as it is outside the permitted working directory')

    def test_out_of_bounds2(self):
        result = get_files_info("calculator", "../")
        self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory')


if __name__ == "__main__":
    unittest.main()