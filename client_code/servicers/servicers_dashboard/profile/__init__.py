from ._anvil_designer import profileTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class profile(profileTemplate):
  def __init__(self,user_data, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_data = user_data
    print("user_data profile page ",self.user_data)
    

  

    # Any code you write here will run before the form opens.
