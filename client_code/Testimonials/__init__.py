from ._anvil_designer import TestimonialsTemplate
from anvil import *

class Testimonials(TestimonialsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    open_form('HOME')

