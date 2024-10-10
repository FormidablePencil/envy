import flet as ft
from core import CentralAIManager

def main(page: ft.Page):
    CentralAIManager(page, start_ui=True)

if __name__ == "__main__":
    print('fk dd')
    ft.app(target=main)

print('fk')