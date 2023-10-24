# this method takes in three values, r, g, b for red, green, and blue
def rgb_to_hex(r, g, b):
    # each variable gives the min and max color values for each red, green, and blue
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    # returns each of the values formatted
    return '{:02X}{:02X}{:02X}'.format(r, g, b)


# test with hex_color = rgb_to_hex(255, 127, 0) # returns "FF7F00"
