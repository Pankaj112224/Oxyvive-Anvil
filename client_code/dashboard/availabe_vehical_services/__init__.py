from ._anvil_designer import availabe_vehical_servicesTemplate
from anvil import *
import anvil.server
from ._anvil_designer import services_listTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import servicer_id

class availabe_vehical_services(availabe_vehical_servicesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_id = user_id
    # Any code you write here will run before the form opens.
    data = app_tables.oxiclinics.search(serviceProvider_id =self.id)
    if not data:
        alert("No bookings yet on this date")

    customers_list =[]
    for row in data:
      customer_details =app_tables.users.get(id=row['user_id'])
      customer = {}
      customer["name"]=customer_details['Oxiclinics_Name']
      customer["email"]=customer_details['email']
      customer["phone"]=customer_details['phone']
      customer["slot_time"]=row['book_time']
      customer["address"]=row['address']
      customer["image"] = customer_details['profile']
      customer["date"] = row['book_date']
      customers_list.append(customer)
    self.repeating_panel_1.items=customers_list
