from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
import requests

class StudentApp(MDApp):
    def build(self):
        self.screen = MDScreen()

        # Text Fields
        self.id_input = MDTextField(hint_text="ID", pos_hint={"center_x": 0.5, "center_y": 0.9}, size_hint=(None, None),width=200)
        self.name_input = MDTextField(hint_text="Name", pos_hint={"center_x": 0.5, "center_y": 0.8}, size_hint=(None, None),width=200)
        self.roll_input = MDTextField(hint_text="Roll", pos_hint={"center_x": 0.5, "center_y": 0.7}, size_hint=(None, None),width=200)
        self.city_input = MDTextField(hint_text="City", pos_hint={"center_x": 0.5, "center_y": 0.6}, size_hint=(None, None),width=200)

        # Buttons
        self.get_button = MDRaisedButton(text="GET", pos_hint={"center_x": 0.2, "center_y": 0.5}, on_release=self.get_data)
        self.post_button = MDRaisedButton(text="POST", pos_hint={"center_x": 0.4, "center_y": 0.5}, on_release=self.post_data)
        self.update_button = MDRaisedButton(text="UPDATE", pos_hint={"center_x": 0.6, "center_y": 0.5}, on_release=self.update_data)
        self.delete_button = MDRaisedButton(text="DELETE", pos_hint={"center_x": 0.8, "center_y": 0.5}, on_release=self.delete_data)

        self.screen.add_widget(self.id_input)
        self.screen.add_widget(self.name_input)
        self.screen.add_widget(self.roll_input)
        self.screen.add_widget(self.city_input)
        self.screen.add_widget(self.get_button)
        self.screen.add_widget(self.post_button)
        self.screen.add_widget(self.update_button)
        self.screen.add_widget(self.delete_button)

        return self.screen

    def get_data(self, *args):
        # Get the ID entered by the user
        student_id = self.id_input.text

        # Make the API request to get data for the specified ID
        response = requests.get(f"http://127.0.0.1:8000/StudentApi/{student_id}/")
        
        if response.status_code == 200:
            data = response.json()
            
            # Display the data in the corresponding text fields
            self.name_input.text = str(data.get("name", ""))
            self.roll_input.text = str(data.get("roll", ""))
            self.city_input.text = str(data.get("city", ""))
            
            print(f"GET Data for ID {student_id}:", data)
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    def post_data(self, *args):
        data = {
            "name": self.name_input.text,
            "roll": self.roll_input.text,
            "city": self.city_input.text,
        }
        response = requests.post("http://127.0.0.1:8000/StudentApi/", json=data)
        if response.status_code == 201:
            print("POST Data: Successfully created.")
        else:
            print(f"Failed to create data. Status code: {response.status_code}")

    def update_data(self, *args):
        # Get the ID entered by the user
        student_id = self.id_input.text

        # Make the API request to update data for the specified ID
        data = {
            "name": self.name_input.text,
            "roll": self.roll_input.text,
            "city": self.city_input.text,
        }
        response = requests.put(f"http://127.0.0.1:8000/StudentApi/{student_id}/", json=data)

        if response.status_code == 200:
            print(f"UPDATE Data for ID {student_id}: Successfully updated.")
        else:
            print(f"Failed to update data. Status code: {response.status_code}")


    def delete_data(self, *args):
        # Get the ID entered by the user
        student_id = self.id_input.text

        # Make the API request to delete data for the specified ID
        response = requests.delete(f"http://127.0.0.1:8000/StudentApi/{student_id}/")

        if response.status_code == 204:
            print(f"DELETE Data for ID {student_id}: Successfully deleted.")
            # Clear the text fields after successful deletion
            self.name_input.text = ""
            self.roll_input.text = ""
            self.city_input.text = ""
        else:
            print(f"Failed to delete data. Status code: {response.status_code}")

if __name__ == "__main__":
    StudentApp().run()
