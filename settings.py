import pathlib
import os

BASE_DIR = pathlib.Path(__file__).resolve().parent
IMAGES_DIR = os.path.join(BASE_DIR, 'images')

TEMPLATE_MATCHING = {
    'methods': ['cv.TM_CCOEFF', ],
}
