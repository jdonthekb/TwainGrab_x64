import tkinter as tk
from tkinter import Listbox, MULTIPLE
import json
import dtwain_module
from dtwain_module import acquire_image

save_path = 'c:/temp/image.jpg'

acquire_image(save_path)
