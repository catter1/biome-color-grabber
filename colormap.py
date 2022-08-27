from PIL import Image

grass = Image.open('grass.webp').load()
foliage = Image.open('foliage.webp').load()

def get_color(green, temperature, downfall):
    if temperature > 1: temperature = 1
    if temperature < 0: temperature = 0
    if downfall > 1: downfall = 1
    if downfall < 0: downfall = 0

    x = int(255 - (temperature * 255))
    y = int(255 - ((downfall * temperature) * 255))

    if green == "grass":
        hexcolor = '%02x%02x%02x' % grass[x, y]
        intcolor = int(hexcolor, 16)
        color = str(intcolor)
        return '0x' + hexcolor
    if green == "foliage":
        hexcolor = '%02x%02x%02x' % foliage[x, y]
        intcolor = int(hexcolor, 16)
        color = str(intcolor)
        return '0x' + hexcolor

    return "ERROR - Incorrect string given. (grass or foliage)"