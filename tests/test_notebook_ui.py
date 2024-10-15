import unittest
import flet as ft
from notebook_ui import NotebookUI

class TestNotebookUI(unittest.TestCase):
    def setUp(self):
        self.page = ft.Test_Page()
        self.app = NotebookUI(self.page)

    def test_add_note(self):
        # Add a new note
        self.page.get_control("source").value = "Test Source"
        self.page.get_control("relation").value = "Test Relation"
        self.page.get_control("permission").value = "Test Permission"
        self.page.get_control("subject").value = "Test Subject"
        self.page.get_control("keywords").value = "test, keyword"
        self.page.get_control("add_note").click()

        # Verify the note is displayed in the list
        note_list = self.page.get_control("note_list")
        self.assertEqual(len(note_list.controls), 1)
        self.assertEqual(note_list.controls[0].controls[0].value, "Test Source")
        self.assertEqual(note_list.controls[0].controls[1].value, "Test Relation")
        self.assertEqual(note_list.controls[0].controls[2].value, "Test Permission")
        self.assertEqual(note_list.controls[0].controls[3].value, "Test Subject")
        self.assertEqual(note_list.controls[0].controls[4].value, "test, keyword")

    def test_reset_form(self):
        # Add a note
        self.test_add_note()

        # Reset the form
        self.page.get_control("source").value = ""
        self.page.get_control("relation").value = ""
        self.page.get_control("permission").value = ""
        self.page.get_control("subject").value = ""
        self.page.get_control("keywords").value = ""

        # Verify the form fields are empty
        self.assertEqual(self.page.get_control("source").value, "")
        self.assertEqual(self.page.get_control("relation").value, "")
        self.assertEqual(self.page.get_control("permission").value, "")
        self.assertEqual(self.page.get_control("subject").value, "")
        self.assertEqual(self.page.get_control("keywords").value, "")

if __name__ == '__main__':
    unittest.main()
