from ._anvil_designer import available_zym_addressTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class available_zym_address(available_zym_addressTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    data = app_tables.oxigyms.Search()
    

    customers_list =[]
    for row in data:
      customer_details =app_tables.oxigyms.get(id=row['id'])
      customer = {}
      customer["name"]=customer_details['Oxigyms_Name']
      customer["email"]=customer_details['email']
      customer["phone"]=customer_details['phone']
      # customer["slot_time"]=row['book_time']
      customer["address"]=row['address']
      # customer["image"] = customer_details['profile']
      # customer["date"] = row['book_date']
      customers_list.append(customer)
    self.repeating_panel_1.items=customers_list