from ._anvil_designer import oxiwheel_documentsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class oxiwheel_documents(oxiwheel_documentsTemplate):
  def __init__(self, oxiwheel_details, user_id, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_id =user_id
    self.oxiwheel_details=oxiwheel_details

    # Any code you write here will run before the form opens.

  def back_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('servicers_registration_form.servicers_register_add_oxiwheel')

  def Submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if not self.first_file_name and not self.second_file_name:
      pass
    else:
      user_details = app_tables.users.get(id=self.user_id)
      print(user_details)
      oxiwheel_details = self.oxiwheel_details
      app_tables.oxiclinics.add_row(id=str(user_details['id']),
                                   name=user_details['username'],
                                   email=user_details['email'],
                                   password=user_details['password'],
                                   phone=int(user_details['phone']),
                                   pincode=int(oxiwheel_details[4]),
                                   Oxiclinics_Name=oxiwheel_details[0],
                                   established_year=str(oxiwheel_details[1]),
                                   State=oxiwheel_details[2],
                                   District=oxiwheel_details[3],
                                   address_2=oxiwheel_details[5],
                                   capsules=int(oxiwheel_details[6]),
                                   medical_licence=oxiwheel_details[7],
                                   building_licence=oxiwheel_details[8])
                                  
      
      open_form('servicers_registration_form.services_register_add_service',id=self.user_id)

  def medical_file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.first_file_name =file.get_name()
    self.file_name_1.text = self.first_file_name
    self.oxiwheel_details.append(file)

  def building_file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.second_file_name =file.get_name()
    self.file_name_2.text = self.second_file_name
    self.oxiwheel_details.append(file)
