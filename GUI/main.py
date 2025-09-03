import customtkinter as ctk

from GUI import conversion
from operations import unary_ops
from operations import binary_ops

def run():
    app = ctk.CTk()
    app.geometry("405x425")
    app.title("Quinary Calculator")
    app.resizable(False, False)

    button_attributes = {
        "master": app, 
        "width": 75, 
        "height": 75, 
        "corner_radius": 7, 
        "border_width": 2, 
        "border_color": "#385FFC", 
        "fg_color": "#1A4BEB", 
        "hover_color": "#03308B", 
        "text_color":"#000000", 
        "font": ("Arial", 24),
        "hover": True
    } 
    current_operator = {"op": None} 
    first_operand = {"value": None}

    def set_entry(value):
        entry.configure(state="normal")
        entry.insert(ctk.END, str(value))
        entry.configure(state="readonly")

    def convert_entry_to_decimal():
        entry_value = entry.get()
        decimal_value = conversion.convert_to_decimal(entry_value)
        entry.configure(state="normal")
        entry.delete(0, ctk.END)
        entry.insert(0, str(decimal_value))

    def convert_entry_to_quinary():
        entry_value = entry.get()
        quinary_value = conversion.convert_to_quinary(entry_value)
        entry.configure(state="normal")
        entry.delete(0, ctk.END)
        entry.insert(0, str(quinary_value))

    def optionmenu_callback(choice):
        if choice == "Base 10":
            convert_entry_to_decimal()
        elif choice == "Base 5":
            convert_entry_to_quinary()

    entry = ctk.CTkEntry(master=app, width=380, height=60, state="readonly", corner_radius=10, fg_color="#D9D9D9", border_width=2, border_color="#385FFC", text_color="#000000", font=("Arial", 24))
    entry.place(x=15, y=15)

    togglemenu = ctk.CTkOptionMenu(app, values=["Base 5", "Base 10"], command= optionmenu_callback)
    togglemenu.place(x=185, y=85)

    num0_button = ctk.CTkButton(**button_attributes, text="0", command=lambda: set_entry(0))
    num0_button.place(x=15, y=135)

    num1_button = ctk.CTkButton(**button_attributes, text="1", command=lambda: set_entry(1))
    num1_button.place(x=115, y=135)

    num2_button = ctk.CTkButton(**button_attributes, text="2", command=lambda: set_entry(2))
    num2_button.place(x=15, y=235)

    num3_button = ctk.CTkButton(**button_attributes, text="3", command=lambda: set_entry(3))
    num3_button.place(x=115, y=235)

    num4_button = ctk.CTkButton(**button_attributes, text="4", command=lambda: set_entry(4))
    num4_button.place(x=15, y=335)

    def on_square():
        entry_value = entry.get()
        square_value = unary_ops.square(entry_value)
        entry.configure(state="normal")
        entry.delete(0, ctk.END)
        entry.insert(0, str(square_value))

    def on_square_root():
        entry_value = entry.get()
        square_root_value = unary_ops.square_root(entry_value)
        entry.configure(state="normal")
        entry.delete(0, ctk.END)
        entry.insert(0, str(square_root_value))

    def set_operator(op):
        first_operand["value"] = entry.get()
        current_operator["op"] = op
        entry.configure(state="normal")
        entry.delete(0, ctk.END)
        entry.configure(state="readonly")

    def on_equals():
        second_operand = entry.get()
        op = current_operator["op"]
        a = first_operand["value"]
        b = second_operand

        try:
            if op == "+":
                result = binary_ops.add(a, b)
            elif op == "-":
                result = binary_ops.subtract(a, b)
            elif op == "*":
                result = binary_ops.multiply(a, b)
            elif op == "/":
                result = binary_ops.divide(a, b)
            else:
                result = "ERR"
        except ZeroDivisionError:
            result = "DIV0"
        except Exception:
            result = "ERR"

        entry.configure(state="normal")
        entry.delete(0, ctk.END)
        entry.insert(0, str(result))
        entry.configure(state="readonly")

        first_operand["value"] = None
        current_operator["op"] = None

    addition_button = ctk.CTkButton(**button_attributes, text="+", command=lambda: set_operator("+"))
    addition_button.place(x=215, y=135)

    subtraction_button = ctk.CTkButton(**button_attributes, text="-", command=lambda: set_operator("-"))
    subtraction_button.place(x=315, y=135)

    multiplication_button = ctk.CTkButton(**button_attributes, text="x", command=lambda: set_operator("*"))
    multiplication_button.place(x=215, y=235)

    division_button = ctk.CTkButton(**button_attributes, text="÷", command=lambda: set_operator("/"))
    division_button.place(x=315, y=235)

    square_button = ctk.CTkButton(**button_attributes, text="x²", command=on_square)
    square_button.place(x=215, y=335)

    square_root_button = ctk.CTkButton(**button_attributes, text="√x", command=on_square_root)
    square_root_button.place(x=315, y=335)

    equals_button = ctk.CTkButton(**button_attributes, text="=")
    equals_button.place(x=115, y=335)

    app.mainloop()
    if __name__ == "__main__":
        run() 