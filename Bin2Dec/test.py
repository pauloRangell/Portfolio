import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.TextField(label="Enter something", width=300),  # Text field
                    ft.ElevatedButton(text="Submit")        # Button
                ],
                alignment="center",  # Vertically center the column
                horizontal_alignment="center",  # Horizontally center the widgets
                spacing=20  # Space between the text field and button
            ),
            alignment=ft.alignment.center,  # Center the container in both axes
            expand=True  # Fill the entire window
        )
    )

ft.app(target=main)
