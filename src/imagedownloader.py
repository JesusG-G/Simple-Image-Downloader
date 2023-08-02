import os
import requests

class ImageDownloader():
    def __init__(self) -> None:
        pass
    
    def get_extension(self,image_url: str) -> str | None:
        extensions: list[str] = ['.png', '.jpeg', '.jpg', '.gif', '.svg']
        for ext in extensions: 
            if ext in image_url:
                return ext

    def download_image(self,image_url: str, name: str, folder: str = None) -> str:

        if ext := self.get_extension(image_url):
            if folder:
                image_name: str = f'{folder}/{name}{ext}'

            else:
                image_name: str = f'{name}{ext}'
        else:
            Exception('Image extension could not be located')
            
        if ext != None:
            #Check if name Already exists
            if os.path.isfile(image_name):
                Exception('File name Already exists')
        else:
            Exception('Image could not be downloaded')
        #Download image
        try:
            image_content: bytes = requests.get(image_url).content
            with open(image_name, 'wb') as handler:
                handler.write(image_content)
                result = f'Downloaded: succesfully'
                return result
        except Exception as e:
            result = f'Error: {e}'
            return result

