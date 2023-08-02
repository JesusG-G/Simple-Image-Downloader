from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty

class SuccessPopup(Popup):
    result_text = ObjectProperty()
    pass

class FailPopup(Popup):
    result_text = ObjectProperty()
    pass

