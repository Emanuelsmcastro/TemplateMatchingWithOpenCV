import cv2 as cv 
from collections import namedtuple
from settings import *
import numpy as np

class TemplateMachingBase:
    image_name: str = 'example.jpg'
    template_name: str = 'template.png'
    images = namedtuple('Images', 'image image_gray template template_gray'.split())
    
    def __init__(self, image_name: str | None = None, template_name: str | None = None, *args, **kwargs) -> None:
        if image_name: self.image_name = image_name
        if template_name: self.template_name = template_name
        self.run(*args, **kwargs)
        
    @staticmethod
    def showImage(image) -> None:
        cv.imshow('Template Matching', image)
        cv.waitKey(0)
        cv.destroyAllWindows()
      
    @staticmethod
    def getTemplateMatchingMethods() -> list:
        methods = TEMPLATE_MATCHING.get('methods')
        if not methods: raise Exception('Template Matching methods not defined in settings')
        return methods
        
    def getImagePath(self) -> str:
        if not self.image_name: raise Exception('Image name not defined')
        return os.path.join(IMAGES_DIR, self.image_name)
    
    def getTemplatePath(self) -> str:
        if not self.template_name: raise Exception('Template name not defined')
        return os.path.join(IMAGES_DIR, self.template_name)

    def getImages(self) -> images:
        img = cv.imread(self.getImagePath(), 3)
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        template = cv.imread(self.getTemplatePath(), 3)
        template_gray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
        
        return self.images(img, img_gray, template, template_gray)
    
    def getRandomColor(self):
        np.random.randint(0, 255, 3, dtype=np.uint8)
    
    def matching(self, meth, image, template, image_to_render) -> dict:
        top_left, bottom_right = None, None
        w, h = template.shape[::-1]
        color = np.random.randint(0, 255, 3, dtype=np.uint8)
        method = eval(meth)
        res = cv.matchTemplate(image, template, method)
            
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
        cv.rectangle(image_to_render, top_left, bottom_right, color.tolist(), 2)
        
        text_x = top_left[0]
        text_y = top_left[1] - 5
    
        cv.putText(image_to_render, 'Founded', (text_x, text_y), cv.FONT_HERSHEY_SIMPLEX, .6, [255, 255, 255], 1)
        
        return {
            'val': {
                'min': min_val,
                'max': max_val
            },
            'loc': {
                'min': min_loc,
                'max': max_loc
            },
            'top_left': top_left,
            'bottom_right': bottom_right
        }
    
    def run(self, *args, **kwargs):
        pass

