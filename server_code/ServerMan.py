import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import datetime
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#


@anvil.server.callable
def add_project(title: str, desc: str, status, open=False):
  # TODO: Add input verification
  id = max([r["id"] for r in app_tables.project.search()]) + 1
  status_row = app_tables.status.get(status=status)
  app_tables.project.add_row(id = id, title=title, desc=desc, status=status_row, created=datetime.date.today(), open=open)