from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.data_grid_1.visible = False
    self.rich_text_1.visible = False

    # Any code you write here will run when the form opens.

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def recommend_click(self, **event_args):
    """This method is called when the button is clicked"""
    song = str(self.track_name.text)
    number_of_recommendations = int(self.drop_down_1.selected_value)
    try:
      result = anvil.server.call('recommend_new_song', song, number_of_recommendations)
      self.data_grid_1.visible = True
      self.rich_text_1.visible = False
    except:
      self.rich_text_1.visible = True
      self.data_grid_1.visible = False
    to_show = []
    for i in result: 
        to_show.append({'artist': i, 'song': result[i]})

    self.repeating_panel_1.items = to_show

