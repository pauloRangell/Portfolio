import flet as ft
from itertools import starmap

output = ft.Text("", size=24)

def main(page: ft.Page):
    
    page.title = "Bin2Dec"
    page.theme_mode = "light"
    user_input = ft.TextField(label="Enter a binary number of 8 digits", width=400)
    
    
    def binary_to_decimal(input:str):
        input_is_not_up_to_8_digits = len(input) > 8
        input_is_not_binary = not all(map(lambda digit: digit in ["0","1"], input))
        global output
        
        if input_is_not_up_to_8_digits:
            output.value = "Binary number must e up to 8 digits!"
        elif input_is_not_binary:
            output.value = "Binary numbers are composed just by 1's and 0's."
        else:
            decimal_form = sum(starmap(lambda index, digit: int(digit) * 2 ** ((len(input) - 1) - index),enumerate(input)))
            output.value = f"This binary number in decimal is {decimal_form}"
        page.update()
        
        
    page.add(
        
        ft.Container(
            content=ft.Column(controls=[
                user_input,
                ft.ElevatedButton(text="Convert to decimal", on_click= lambda e: binary_to_decimal(user_input.value)),
                output
            ],
            alignment="center",horizontal_alignment="center", expand=True),
            alignment=ft.alignment.center, expand=True)
)

ft.app(main)

        
        
    