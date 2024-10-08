import flet as ft
def is_a_valid_binary_number(input:str):
    if len(input) > 8:
        raise ValueError("input must be a binary number of 8 digits")
    if not all(map(lambda digit: digit in ["0","1"], input)):
        raise ValueError("It must contain just 1's and 0's")
    
def binary_to_decimal(x:str):
    r = 0
    for i, n in enumerate(x):
        r += int(n) * 2 ** ((len(x) - 1) - i)
    return r








def main(page: ft.Page):
    page.title = "Bin2Dec"
    page.theme_mode = "light"
    user_input = ft.TextField(label="Enter a binary number of 8 digits", width=400)
    decimal_representation = None
    page.add(
        
        ft.Container(
            content=ft.Column(controls=[
                user_input,
                ft.ElevatedButton(text="Convert to decimal"), # add on_click argument
                ft.Text(value=decimal_representation)
            ],
            alignment="center",horizontal_alignment="center", expand=True),
            alignment=ft.alignment.center, expand=True)
   
    
)

ft.app(main)

        
        
    