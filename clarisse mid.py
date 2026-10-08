import tkinter as tk
from tkinter import messagebox, ttk
import re


class StudentManagementApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("900x900")
        self.root.resizable(False, False)

        self.students = {}

        self.root.configure(bg="#f4f6f9")

        self.create_widgets()

    def create_widgets(self):

        lbl_header = tk.Label(
            self.root,
            text="Student Management System",
            font=("Arial", 16, "bold"),
            bg="#f4f6f9",
            fg="#2c3e50",
        )
        lbl_header.pack(pady=(15, 10))

        frame_input = tk.Frame(
            self.root,
            bg="#ffffff",
            bd=1,
            relief="solid",
            padx=15,
            pady=15
        )
        frame_input.pack(
            padx=20,
            pady=5,
            fill="x"
        )

        tk.Label(
            frame_input,
            text="Student ID:",
            font=("Arial", 10, "bold"),
            bg="#ffffff",
            anchor="w",
        ).grid(row=0, column=0, sticky="w", pady=5)

        self.entry_student_id = tk.Entry(
            frame_input,
            font=("Arial", 10),
            width=35
        )
        self.entry_student_id.grid(
            row=0,
            column=1,
            sticky="e",
            pady=5,
            padx=(10, 0)
        )

        tk.Label(
            frame_input,
            text="Full Name:",
            font=("Arial", 10, "bold"),
            bg="#ffffff",
            anchor="w",
        ).grid(row=1, column=0, sticky="w", pady=5)

        self.entry_name = tk.Entry(
            frame_input,
            font=("Arial", 10),
            width=35
        )
        self.entry_name.grid(
            row=1,
            column=1,
            sticky="e",
            pady=5,
            padx=(10, 0)
        )

        tk.Label(
            frame_input,
            text="Age:",
            font=("Arial", 10, "bold"),
            bg="#ffffff",
            anchor="w",
        ).grid(row=2, column=0, sticky="w", pady=5)

        self.entry_age = tk.Entry(
            frame_input,
            font=("Arial", 10),
            width=35
        )
        self.entry_age.grid(
            row=2,
            column=1,
            sticky="e",
            pady=5,
            padx=(10, 0)
        )

        tk.Label(
            frame_input,
            text="Phone Number:",
            font=("Arial", 10, "bold"),
            bg="#ffffff",
            anchor="w",
        ).grid(row=3, column=0, sticky="w", pady=5)

        self.entry_phone = tk.Entry(
            frame_input,
            font=("Arial", 10),
            width=35
        )
        self.entry_phone.grid(
            row=3,
            column=1,
            sticky="e",
            pady=5,
            padx=(10, 0)
        )

        tk.Label(
            frame_input,
            text="Occupation:",
            font=("Arial", 10, "bold"),
            bg="#ffffff",
            anchor="w",
        ).grid(row=4, column=0, sticky="w", pady=5)

        self.entry_occupation = tk.Entry(
            frame_input,
            font=("Arial", 10),
            width=35
        )
        self.entry_occupation.grid(
            row=4,
            column=1,
            sticky="e",
            pady=5,
            padx=(10, 0)
        )

        tk.Label(
            frame_input,
            text="Email:",
            font=("Arial", 10, "bold"),
            bg="#ffffff",
            anchor="w",
        ).grid(row=5, column=0, sticky="w", pady=5)

        self.entry_email = tk.Entry(
            frame_input,
            font=("Arial", 10),
            width=35
        )
        self.entry_email.grid(
            row=5,
            column=1,
            sticky="e",
            pady=5,
            padx=(10, 0)
        )

        tk.Label(
            frame_input,
            text="City:",
            font=("Arial", 10, "bold"),
            bg="#ffffff",
            anchor="w",
        ).grid(row=6, column=0, sticky="w", pady=5)

        self.entry_city = tk.Entry(
            frame_input,
            font=("Arial", 10),
            width=35
        )
        self.entry_city.grid(
            row=6,
            column=1,
            sticky="e",
            pady=5,
            padx=(10, 0)
        )

        frame_buttons = tk.Frame(
            self.root,
            bg="#f4f6f9"
        )
        frame_buttons.pack(pady=12)

        tk.Button(
            frame_buttons,
            text="Add",
            bg="#27ae60",
            fg="white",
            font=("Arial", 10, "bold"),
            width=8,
            command=self.add_student,
        ).grid(row=0, column=0, padx=4)

        tk.Button(
            frame_buttons,
            text="Update",
            bg="#2980b9",
            fg="white",
            font=("Arial", 10, "bold"),
            width=8,
            command=self.update_student,
        ).grid(row=0, column=1, padx=4)

        tk.Button(
            frame_buttons,
            text="Delete",
            bg="#c0392b",
            fg="white",
            font=("Arial", 10, "bold"),
            width=8,
            command=self.delete_student,
        ).grid(row=0, column=2, padx=4)

        tk.Button(
            frame_buttons,
            text="Clear",
            bg="#f39c12",
            fg="white",
            font=("Arial", 10, "bold"),
            width=8,
            command=self.clear_fields,
        ).grid(row=0, column=3, padx=4)

        tk.Button(
            frame_buttons,
            text="Exit",
            bg="#7f8c8d",
            fg="white",
            font=("Arial", 10, "bold"),
            width=8,
            command=self.root.destroy,
        ).grid(row=0, column=4, padx=4)

        frame_table = tk.Frame(
            self.root,
            bg="#f4f6f9"
        )
        frame_table.pack(
            padx=20,
            pady=5,
            fill="both",
            expand=True
        )

        columns = (
            "Student ID",
            "Name",
            "Age",
            "Phone",
            "Occupation",
            "Email",
            "City"
        )

        self.tree = ttk.Treeview(
            frame_table,
            columns=columns,
            show="headings",
            height=7
        )

        headings = {
            "Student ID": "Student ID",
            "Name": "Full Name",
            "Age": "Age",
            "Phone": "Phone Number",
            "Occupation": "Occupation",
            "Email": "Email",
            "City": "City"
        }

        widths = {
            "Student ID": 90,
            "Name": 135,
            "Age": 45,
            "Phone": 110,
            "Occupation": 110,
            "Email": 170,
            "City": 90
        }

        for column in columns:
            self.tree.heading(
                column,
                text=headings[column]
            )
            self.tree.column(
                column,
                width=widths[column]
            )

        self.tree.column(
            "Student ID",
            anchor="center"
        )

        self.tree.column(
            "Age",
            anchor="center"
        )

        self.tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.on_select_item
        )

        scrollbar = ttk.Scrollbar(
            frame_table,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        frame_output = tk.LabelFrame(
            self.root,
            text=" Displayed Student Information ",
            font=("Arial", 10, "bold"),
            bg="#ffffff",
            fg="#2c3e50",
            bd=1,
            relief="solid",
            padx=15,
            pady=10,
        )

        frame_output.pack(
            padx=20,
            pady=(5, 15),
            fill="x"
        )

        self.lbl_output_student_id = tk.Label(
            frame_output,
            text="Student ID: ---",
            font=("Arial", 10),
            bg="#ffffff",
            anchor="w",
        )
        self.lbl_output_student_id.pack(
            fill="x",
            pady=2
        )

        self.lbl_output_name = tk.Label(
            frame_output,
            text="Full Name: ---",
            font=("Arial", 10),
            bg="#ffffff",
            anchor="w",
        )
        self.lbl_output_name.pack(
            fill="x",
            pady=2
        )

        self.lbl_output_age = tk.Label(
            frame_output,
            text="Age: ---",
            font=("Arial", 10),
            bg="#ffffff",
            anchor="w",
        )
        self.lbl_output_age.pack(
            fill="x",
            pady=2
        )

        self.lbl_output_phone = tk.Label(
            frame_output,
            text="Phone Number: ---",
            font=("Arial", 10),
            bg="#ffffff",
            anchor="w",
        )
        self.lbl_output_phone.pack(
            fill="x",
            pady=2
        )

        self.lbl_output_occupation = tk.Label(
            frame_output,
            text="Occupation: ---",
            font=("Arial", 10),
            bg="#ffffff",
            anchor="w",
        )
        self.lbl_output_occupation.pack(
            fill="x",
            pady=2
        )

        self.lbl_output_email = tk.Label(
            frame_output,
            text="Email: ---",
            font=("Arial", 10),
            bg="#ffffff",
            anchor="w",
        )
        self.lbl_output_email.pack(
            fill="x",
            pady=2
        )

        self.lbl_output_city = tk.Label(
            frame_output,
            text="City: ---",
            font=("Arial", 10),
            bg="#ffffff",
            anchor="w",
        )
        self.lbl_output_city.pack(
            fill="x",
            pady=2
        )

    def validate_inputs(self):

        student_id = self.entry_student_id.get().strip()
        name = self.entry_name.get().strip()
        age = self.entry_age.get().strip()
        phone = self.entry_phone.get().strip()
        occupation = self.entry_occupation.get().strip()
        email = self.entry_email.get().strip()
        city = self.entry_city.get().strip()

        if not student_id or not name or not age or not phone or not occupation or not email or not city:
            messagebox.showwarning(
                "Input Error",
                "Please fill in all fields."
            )
            return None

        if not re.match(r"^[A-Za-z0-9-]+$", student_id):
            messagebox.showerror(
                "Invalid Student ID",
                "Student ID can only contain letters, numbers, and hyphens."
            )
            return None

        if not age.isdigit() or int(age) <= 0 or int(age) > 120:
            messagebox.showerror(
                "Invalid Age",
                "Please enter a valid age between 1 and 120."
            )
            return None

        phone_digits = (
            phone
            .replace("-", "")
            .replace(" ", "")
            .replace("+", "")
        )

        if not phone_digits.isdigit():
            messagebox.showerror(
                "Invalid Phone Number",
                "Please enter a valid phone number."
            )
            return None

        if len(phone_digits) < 10:
            messagebox.showerror(
                "Invalid Phone Number",
                "Phone number must contain at least 10 digits."
            )
            return None

        email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

        if not re.match(email_pattern, email):
            messagebox.showerror(
                "Invalid Email",
                "Please enter a valid email address."
            )
            return None

        return (
            student_id,
            name,
            age,
            phone,
            occupation,
            email,
            city
        )

    def update_output_area(
        self,
        student_id="---",
        name="---",
        age="---",
        phone="---",
        occupation="---",
        email="---",
        city="---"
    ):

        self.lbl_output_student_id.config(
            text=f"Student ID: {student_id}"
        )

        self.lbl_output_name.config(
            text=f"Full Name: {name}"
        )

        self.lbl_output_age.config(
            text=(
                f"Age: {age}"
                if age == "---"
                else f"Age: {age} years old"
            )
        )

        self.lbl_output_phone.config(
            text=f"Phone Number: {phone}"
        )

        self.lbl_output_occupation.config(
            text=f"Occupation: {occupation}"
        )

        self.lbl_output_email.config(
            text=f"Email: {email}"
        )

        self.lbl_output_city.config(
            text=f"City: {city}"
        )

    def add_student(self):

        data = self.validate_inputs()

        if not data:
            return

        (
            student_id,
            name,
            age,
            phone,
            occupation,
            email,
            city
        ) = data

        if student_id in self.students:
            messagebox.showwarning(
                "Duplicate Entry",
                f"Student ID '{student_id}' already exists. "
                "Use Update instead."
            )
            return

        self.students[student_id] = {
            "name": name,
            "age": age,
            "phone": phone,
            "occupation": occupation,
            "email": email,
            "city": city
        }

        self.tree.insert(
            "",
            "end",
            iid=student_id,
            values=(
                student_id,
                name,
                age,
                phone,
                occupation,
                email,
                city
            )
        )

        self.update_output_area(
            student_id,
            name,
            age,
            phone,
            occupation,
            email,
            city
        )

        messagebox.showinfo(
            "Success",
            f"Student '{name}' added successfully!"
        )

    def update_student(self):

        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning(
                "Selection Error",
                "Please select a student from the list to update."
            )
            return

        data = self.validate_inputs()

        if not data:
            return

        (
            student_id,
            name,
            age,
            phone,
            occupation,
            email,
            city
        ) = data

        old_student_id = selected_item[0]

        if (
            student_id != old_student_id
            and student_id in self.students
        ):
            messagebox.showwarning(
                "Duplicate Entry",
                f"Student ID '{student_id}' already exists."
            )
            return

        if old_student_id in self.students:
            del self.students[old_student_id]

        self.students[student_id] = {
            "name": name,
            "age": age,
            "phone": phone,
            "occupation": occupation,
            "email": email,
            "city": city
        }

        self.tree.delete(old_student_id)

        self.tree.insert(
            "",
            "end",
            iid=student_id,
            values=(
                student_id,
                name,
                age,
                phone,
                occupation,
                email,
                city
            )
        )

        self.update_output_area(
            student_id,
            name,
            age,
            phone,
            occupation,
            email,
            city
        )

        messagebox.showinfo(
            "Success",
            f"Student '{name}' updated successfully!"
        )

    def delete_student(self):

        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning(
                "Selection Error",
                "Please select a student from the list to delete."
            )
            return

        student_id = selected_item[0]
        student_name = self.students[student_id]["name"]

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete '{student_name}'?"
        )

        if confirm:

            if student_id in self.students:
                del self.students[student_id]

            self.tree.delete(student_id)

            self.clear_fields()

            messagebox.showinfo(
                "Success",
                f"Student '{student_name}' deleted successfully!"
            )

    def clear_fields(self):

        self.entry_student_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_occupation.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_city.delete(0, tk.END)

        if self.tree.selection():
            self.tree.selection_remove(
                self.tree.selection()
            )

        self.update_output_area()

    def on_select_item(self, event):

        selected_item = self.tree.selection()

        if selected_item:

            item = self.tree.item(
                selected_item[0]
            )

            (
                student_id,
                name,
                age,
                phone,
                occupation,
                email,
                city
            ) = item["values"]

            self.entry_student_id.delete(
                0,
                tk.END
            )
            self.entry_student_id.insert(
                0,
                student_id
            )

            self.entry_name.delete(
                0,
                tk.END
            )
            self.entry_name.insert(
                0,
                name
            )

            self.entry_age.delete(
                0,
                tk.END
            )
            self.entry_age.insert(
                0,
                age
            )

            self.entry_phone.delete(
                0,
                tk.END
            )
            self.entry_phone.insert(
                0,
                phone
            )

            self.entry_occupation.delete(
                0,
                tk.END
            )
            self.entry_occupation.insert(
                0,
                occupation
            )

            self.entry_email.delete(
                0,
                tk.END
            )
            self.entry_email.insert(
                0,
                email
            )

            self.entry_city.delete(
                0,
                tk.END
            )
            self.entry_city.insert(
                0,
                city
            )

            self.update_output_area(
                student_id,
                name,
                age,
                phone,
                occupation,
                email,
                city
            )


if __name__ == "__main__":

    root = tk.Tk()

    app = StudentManagementApp(root)

    root.mainloop()
