from utils import TemplateMachingBase
import cv2 as cv

class TemplateMaching(TemplateMachingBase):
    image_name = 'example.jpg'
    template_name = 'template.png'

    def run(self, *args, **kwargs):
        methods = self.getTemplateMatchingMethods()
        images = self.getImages()
        image_color_copy = images.image
        
        for meth in methods:
           self.matching(meth, images.image_gray, images.template_gray, image_color_copy)
        self.showImage(image_color_copy)
            
TemplateMaching()