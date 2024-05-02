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
    List_oxiclinics = []
    for i, row in enumerate(rows, start=1):
      # Initialize dictionary to store row data
      user_info = {}
      user_info['serial_no'] = i  # Assuming you want to include a serial number
      user_info['clinic_id'] = row["oxiclinic_id"]
      user_info['Oxiclinics_Name'] = row['Oxiclinics_Name']
      user_info['State'] = row['State']
      
      # Append dictionary to list
      List_oxiclinics.append(user_info)

    # Set repeating panel items
    self.repeating_panel_1.items = List_oxiclinics
