from ._anvil_designer import homeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import mg
import webbrowser

class home(homeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.top_title.text = mg.top_title
    self.top_btn_thanks.text = mg.top_btn_thanks
    self.top_btn_start.text = mg.top_btn_start
    self.top_btn_join.text = mg.top_btn_join

  def top_btn_thanks_click(self, **event_args):
    alert(content="... to our Alpha testers, the students in the SW101 course at the Realschule Baesweiler during April 2024 taught by René Langohr, and all the beta testers.", title="Thank you", large=True)

  def top_btn_poc_click(self, **event_args):
    alert("Neither the user interface nor the server code is elegant nor efficient. Contact us if you can help making either or all better.",
         title="So far, this app is a Proof of Concept")

  def top_btn_help_click(self, **event_args):
    webbrowser.open_new("http://sdggamehelp.blue-way.net")

  def top_btn_start_click(self, **event_args):
    game_id = anvil.server.call('generate_id')
    app_tables.status.add_row(game_id=game_id, closed=0, current_gm=0, current_p=0, roles_avail=2)
    anvil.server.call('set_roles', game_id)
    alert("Roles set up")
    pass

  def top_btn_join_click(self, **event_args):
    """This method is called when the component is clicked."""
    pass
