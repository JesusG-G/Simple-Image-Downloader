import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from imagedownloader import ImageDownloader
from shared.popup.popup import *

#load the kv file
Builder.load_file('main.kv')
Builder.load_file("shared/popup/popup.kv")

class MainLayout(Widget):
    #Class inyection
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image_downloader = ImageDownloader()
        self.successpopup = SuccessPopup()
        self.failpopup = FailPopup()
    
    image_url: ObjectProperty(None)
    image_name: ObjectProperty(None)
    def messag_popup(self, txt:str) :
        if txt:
            self.successpopup.result_text.text = txt
            self.successpopup.open()
        else:
            self.failpopup.result_text.text = txt
            self.failpopup.open()
        
    def on_press(self):
        image_url = self.image_url.text
        image_url_list = image_url.split(";") 
        image_name = self.image_name.text
        print(image_url_list)
        if len(image_url_list) > 1:
            for index,image in enumerate(image_url_list):
                image_name = f'{image_name}_{index}'
                result: str = self.image_downloader.download_image(image, image_name, folder='src/images')
            self.messag_popup(result)
        else:
            result: str = self.image_downloader.download_image(image_url, image_name, folder='src/images')
            print(result)
            self.messag_popup(result)
        self.image_url.text = ""
        self.image_name.text = ""
class ImageDownloaderApp(App):
    def build(self):
        return MainLayout()
    
if __name__ == "__main__":
    app = ImageDownloaderApp()
    app.run()