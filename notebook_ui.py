import flet as ft
from data_wallet.notebook.main import Notebook

class NotebookUI:
    def __init__(self, target: ft.Page):
        # TODO Even listen to itself
        # super().__init__(target)
        self.notebook = Notebook()
        self.notebook.create_tables()

    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Notebook"),
                ft.TextField(label="Source", name="source"),
                ft.TextField(label="Relation", name="relation"),
                ft.TextField(label="Permission", name="permission"),
                ft.TextField(label="Subject", name="subject"),
                ft.TextField(label="Keywords", name="keywords"),
                ft.ElevatedButton("Add Note", on_click=self.add_note),
                ft.Divider(),
                ft.ListView(
                    expand=True,
                    scroll=ft.ScrollMode.AUTO,
                    item_builder=self.build_note_item,
                    name="note_list"
                )
            ]
        )

    def add_note(self, event):
        source = self.controls.get("source").value
        relation = self.controls.get("relation").value
        permission = self.controls.get("permission").value
        subject = self.controls.get("subject").value
        keywords = self.controls.get("keywords").value
        user_id = 1  # Replace with actual user ID

        if self.notebook.add(source, relation, permission, subject, keywords):
            self.controls.get("note_list").update()
            self.reset_form()
        else:
            ft.alert(f"Failed to add note: {source}")

    def build_note_item(self, index, item):
        return ft.Row(
            controls=[
                ft.Text(item["source"]),
                ft.Text(item["relation"]),
                ft.Text(item["permission"]),
                ft.Text(item["subject"]),
                ft.Text(item["keywords"])
            ]
        )

    def reset_form(self):
        self.controls.get("source").value = ""
        self.controls.get("relation").value = ""
        self.controls.get("permission").value = ""
        self.controls.get("subject").value = ""
        self.controls.get("keywords").value = ""

def main(page: ft.Page):
    page.title = "Notebook"
    NotebookUI(page).run()

if __name__ == "__main__":
    ft.app(target=main, port=9000)
