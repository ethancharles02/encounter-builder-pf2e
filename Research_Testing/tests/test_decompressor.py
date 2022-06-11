import unittest
from sys import path
path.append("..")
from os import getcwd, listdir, remove as os_remove, path as os_path

from decompressor import Decompressor


TXT_FOLDER = "Research_Testing/tests/compressor_text_files"
TST_FOLDER = f"{TXT_FOLDER}/test_files"
REF_FOLDER = f"{TXT_FOLDER}/reference_files"
DUMP_FOLDER = f"{TXT_FOLDER}/dump_files"

class Test_Decompressor(unittest.TestCase):
    def setUp(self):
        self.decompressor = Decompressor()
        self.decompressor.input_folder = REF_FOLDER
        self.decompressor.output_folder = DUMP_FOLDER

    def tearDown(self):
        for f in listdir(DUMP_FOLDER):
            os_remove(os_path.join(DUMP_FOLDER, f))

    def assert_files_in_test_folders_are_equal(self, tst_filename, ref_filename = None):
        if ref_filename == None:
            ref_filename = tst_filename
        with open(f"{DUMP_FOLDER}/{tst_filename}") as f:
            test_list = list(f)
        with open(f"{TST_FOLDER}/{ref_filename}") as f:
            ref_list = list(f)
        self.assertListEqual(test_list, ref_list)

    def test_default_input_folder(self):
        x = Decompressor()
        self.assertEqual(x.input_folder, getcwd())

    def test_default_output_folder(self):
        x = Decompressor()
        self.assertEqual(x.output_folder, getcwd())

    def test_empty_file_decompresses(self):
        filename = "text_empty.lor"
        self.decompressor.run(filename)
        output_file = filename.replace(".lor", ".txt")
        self.assert_files_in_test_folders_are_equal(output_file)

    def test_generic_file_decompresses(self):
        filename = "text_generic.lor"
        self.decompressor.run(filename)
        output_file = filename.replace(".lor", ".txt")
        self.assert_files_in_test_folders_are_equal(output_file)

    def test_decompress_longer_file(self):
        filename = "text_three_chunks.lor"
        self.decompressor.run(filename)
        output_file = filename.replace(".lor", ".txt")
        self.assert_files_in_test_folders_are_equal(output_file)