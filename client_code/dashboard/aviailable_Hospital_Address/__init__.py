# from ._anvil_designer import aviailable_Hospital_AddressTemplate
# from anvil import *
# import anvil.server




# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables



# class aviailable_Hospital_Address(aviailable_Hospital_AddressTemplate):
#   def __init__(self, **properties):
#     # Set Form properties and Data Bindings.
#     self.init_components(**properties)

#     # Any code you write here will run before the form opens.
    
#     # Any code you write here will run before the form opens.
#     data = app_tables.oxiclinics.search()
    

#     customers_list =[]
#     for row in data:
#       customer_details =app_tables.oxiclinics.get(id=row['id'])
#       customer = {}
#       customer["name"]=customer_details['Oxiclinics_Name']
#       customer["email"]=customer_details['email']
#       customer["phone"]=customer_details['phone']
#       # customer["slot_time"]=row['book_time']
#       customer["address"]=row['address']
#       # customer["image"] = customer_details['profile']
#       # customer["date"] = row['book_date']
#       customers_list.append(customer)
#     self.repeating_panel_1.items=customers_list

#   def button_2_click(self, **event_args):
#     """This method is called when the button is clicked"""
#     open_form('dashboard')
