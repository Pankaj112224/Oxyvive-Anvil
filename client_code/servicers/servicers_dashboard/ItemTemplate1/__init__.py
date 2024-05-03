from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, timedelta
import time


class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('slot_book')

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    try:
      current_time = datetime.now().strftime("%I:%M:%S %p")
      # Update the time label
      date = self.label_13.text
      time_interval = self.label_6.text
      start_time, end_time = time_interval.split(" - ")
      
      # Parse the current date and time
      current_date = datetime.now().date()
      current_time = datetime.now().time()
      
      # Parse start and end times
      start_time_obj = datetime.strptime(start_time, "%I:%M %p").time()
      end_time_obj = datetime.strptime(end_time, "%I:%M %p").time()
      
      # Calculate dates for yesterday, today, and tomorrow
      yesterday = current_date - timedelta(days=0)
      tomorrow = current_date + timedelta(days=0)
      
      # Compare current date and time with the interval
      if date < yesterday:
          self.label_11.foreground="#fa1900"
          self.label_11.text = "COMPLETED"
      elif date == current_date:
          if current_time < start_time_obj:
              self.label_11.foreground="#f3f718"
              self.label_11.text = "UPCOMING"
          elif start_time_obj <= current_time <= end_time_obj:
              self.label_11.foreground="#08bf2d"
              self.label_11.text = "NOW"
          else:
              self.label_11.foreground="#fa1900"
              self.label_11.text = "COMPLETED"
      elif date > tomorrow:
          self.label_11.foreground="#f3f718"
          self.label_11.text = "UPCOMING"
      else:
          self.label_11.foreground="#fa1900"
          self.label_11.text = "Other date"
      time.sleep(1)
    except Exception as e:
      Notification(f"Error: {e}")

  
