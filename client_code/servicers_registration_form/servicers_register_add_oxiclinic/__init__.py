from ._anvil_designer import servicers_register_add_oxiclinicTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class servicers_register_add_oxiclinic(servicers_register_add_oxiclinicTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens
  def back_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('servicers_registration_form.services_register_add_service')

  def next_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    hospital_name =self.hospital_name.text
    establised_year =self.oxiclini_established_year.date
    state = self.oxiclinic_state.text
    district =self.oxiclinic_district.text
    pincode = self.oxiclinic_pincode.text
    address = self.oxiclinic_address.text
    capsule = self.oxiclinic_capsules.text

    if not hospital_name and not address and not capsule and not district and not establised_year and not pincode and not state:
      pass
    else:
      oxiclinc_details =[hospital_name, establised_year, state, district, pincode, address, capsule]
      open_form('servicers_registration_form.oxiclinic_documents')
