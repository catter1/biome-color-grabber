from PIL import Image

grass = Image.open('grass.png').load()
foliage = Image.open('foliage.png').load()

def get_color(green, temperature, downfall):
    temperature = min(1,max(0,temperature))
    downfall = min(1,max(0,downfall))

    x = int(255 - (temperature * 255))
    y = int(255 - ((downfall * temperature) * 255))

    if green == "grass":
        hexcolor = '%02x%02x%02x' % grass[x, y][0:3]
        intcolor = int(hexcolor, 16)
        return '0x' + hexcolor
    if green == "foliage":
        hexcolor = '%02x%02x%02x' % foliage[x, y][0:3]
        intcolor = int(hexcolor, 16)
        return '0x' + hexcolor

    return "ERROR - Incorrect string given. (grass or foliage)"