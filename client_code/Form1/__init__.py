from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    title = self.title.text
    desc = self.desc.text
    status = self.status.selected_value
    open = self.is_project_open.checked
    anvil.server.call('add_project', title, desc, status, open)
    Notification("Project submitted!").show()
    
