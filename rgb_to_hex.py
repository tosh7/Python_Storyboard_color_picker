
def rgb_to_hex(red, green, blue):
    rgb = (int(255*red), int(255*green), int(255*blue))
    return '#%02x%02x%02x' % rgb