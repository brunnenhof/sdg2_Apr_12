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
    msg = "Your game ID is "+game_id+". Make a note of it and tell your players."
    alert(msg, title="Your game ID:")
    anvil.server.call('set_roles', game_id)
    alert("Roles set up")
    pass

  def top_btn_join_click(self, **event_args):
    print('btn_join')
    how_many_new = len(app_tables.status.search(closed=0, current_gm =0))
    if how_many_new > 1:
      self.top_btn_join.visible = False
      self.top_btn_start.visible = False
      self.p_cp_choose_game.visible = True
      self.p_dd_select_game.items = [(row["game_id"], row) for row in app_tables.status.search(closed=0, current_gm =0, roles_avail=2)]
    elif how_many_new == 1:
      row = app_tables.status.get(closed=0)
      alert(row['game_id'], title="You are joining: ")
      mg.my_game_id = row['game_id']
      #### 
      #### xy must be replaced with the chosen region
      #### 
#      self.show_roles(row['game_id'], 'xy')
#      self.card_select_reg_role.visible = True
    else:
      alert("The game organizer has not yet started a game. Please wait until he/she does ...")

  def p_btn_join_after_choice_click(self, **event_args):
    alert(self.p_dd_select_game.selected_value['game_id'], title="You are joining: ")
    game_id_chosen = self.p_dd_select_game.selected_value['game_id']
    mg.my_game_id = game_id_chosen
#    self.show_roles(game_id_chosen, 'xy')
#    alert(my_globs.my_game_id,"stored globally")
    self.p_cp_choose_game.visible = False
#    self.card_select_reg_role.visible = True
