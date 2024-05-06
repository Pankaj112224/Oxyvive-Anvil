from ._anvil_designer import slot_book_clinicTemplate
from anvil import *
import anvil.server
from datetime import datetime, timedelta

class slot_book_clinic(slot_book_clinicTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.set_button_date()

    def set_button_date(self):
        current_date = datetime.now()
        for i in range(1, 5):
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            date_for_button = current_date + timedelta(days=i - 1)
            formatted_date = date_for_button.strftime("%a %d")
            button.text = formatted_date

    def button_click(self, button_number):
        self.primary_color_1.visible = True
        current_date = datetime.now().date()
        current_time = datetime.now().time()
        times = ["09:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM", "7:00 PM"]

        for i in range(5, 11):
            button_name = f'button_{i}'
            button = getattr(self, button_name)

            if i - 5 < len(times):
                button.text = times[i - 5]
                button_date = current_date + timedelta(days=button_number - 1)
                button_time = datetime.strptime(button.text, "%I:%M %p").time()

                if current_date == button_date and current_time > button_time:
                    button.enabled = False
                else:
                    button.enabled = True
            else:
                button.text = "No Time"
                button.enabled = False

            button.visible = True

    def button_1_click(self, **event_args):
        self.button_click(1)

    def button_2_click(self, **event_args):
        self.button_click(2)

    def button_3_click(self, **event_args):
        self.button_click(3)

    def button_4_click(self, **event_args):
        self.button_click(4)

    def primary_color_1_click(self, **event_args):
        open_form('wallet')

    def button_2_copy(self, **event_args):
        open_form('dashboard')
