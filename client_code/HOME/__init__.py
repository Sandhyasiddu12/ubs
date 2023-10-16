from ._anvil_designer import HOMETemplate
from anvil import *



class HOME(HOMETemplate):
  def __init__(self, **properties):

    # Set Form properties and Data Bindings.

    self.init_components(**properties)



    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    open_form('AboutUs')

  def link_2_click(self, **event_args):
    open_form('Borrow')

  def link_3_click(self, **event_args):
    open_form('Lender')

  def link_4_click(self, **event_args):
     open_form('Howitworks')

  def link_5_click(self, **event_args):
    open_form('QuickFacts')

  def link_6_click(self, **event_args):
    open_form('FAQs')

  def link_7_click(self, **event_args):
    open_form('UserFeedback')

  def link_8_click(self, **event_args):
    open_form('Testimonials')

  def link_9_click(self, **event_args):
   open_form('OnlineChat')

  def button_1_click(self, **event_args):
    open_form('Login')

  def button_2_click(self, **event_args):
    open_form('Signup')








  

