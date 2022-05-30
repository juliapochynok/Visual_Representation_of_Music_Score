import numpy as np
import matplotlib.pyplot as plt

class WarmPalette:
    '''
    This class represents warm colour palette
    '''
    yellow_green = [115, 154, 1]
    bitter_lemon = [161, 183, 82]
    yellow_ryb = [255, 255, 0]
    middle_yellow = [255, 188, 10]
    cyber_yellow = [250, 137, 9]
    selective_yellow = [244, 86, 8]
    orange_peel = [253, 47, 0]
    dark_orange = [255, 0, 4]
    pumpkin = [237, 115, 111]  
    portland_orange = [223, 43, 74]  
    red_pigment = [171, 22, 65]
    cerise = [255, 200, 200]

    def all_colours():
      '''
      This function returns list of all warm colours
      '''
      return [WarmPalette.cyber_yellow,
         WarmPalette.yellow_ryb,
         WarmPalette.orange_peel, 
         WarmPalette.yellow_green,
         WarmPalette.pumpkin,

        WarmPalette.red_pigment,
         WarmPalette.bitter_lemon,
          WarmPalette.middle_yellow,

        WarmPalette.selective_yellow, 
        WarmPalette.dark_orange,
        WarmPalette.portland_orange, 
         WarmPalette.cerise
         ]


class CoolPalette:
    '''
    This class represents cool colour palette
    '''
    tyrian_purple = [170, 2, 115]
    palatinate_purple = [130, 2, 138]
    strong_violet = [86, 2, 152]
    midnight_blue = [32, 3, 153]
    midnight_blue_second = [30, 46, 181]
    royal_blue_dark = [69, 109, 206]
    prussian_blue = [112, 255, 215]
    indigo_dye = [33, 173, 206]
    midnight_green_eagle = [2, 167, 88]
    hunter_green = [45, 186, 30]
    lincoln_green = [13, 62, 94]
    loncoln_green_second = [151, 244, 229]

    def all_colours():
      '''
      This function returns list of all cool colours
      '''
      return [CoolPalette.tyrian_purple,
         CoolPalette.midnight_blue,
        CoolPalette.prussian_blue,
         CoolPalette.hunter_green, 

         CoolPalette.palatinate_purple,
        CoolPalette.midnight_blue_second,
         CoolPalette.indigo_dye,
          CoolPalette.lincoln_green,

        CoolPalette.strong_violet, 
        CoolPalette.royal_blue_dark, 
        CoolPalette.midnight_green_eagle,
         CoolPalette.loncoln_green_second]

