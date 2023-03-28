import math

class Marker:

    def __init__(self, x, y, c="red"):

        self.x = ' cx="' + str(x) + '"'
        self.y = ' cy="' + str(y) + '"'

        match c:
            case 'green':
                pass
            case 'pink':
                c = "deeppink"
        self.c = ' stroke="' + str(c) + '"'

        self.posx = x
        self.posy = y

    def svg(self):
        svg_file = f'<circle ' + self.x + self.y + ' r="5" fill="none"' + self.c + ' stroke-width="2"/>'
        return svg_file

    def collision(self, other_mark):
        distance = math.dist((self.posx, self.posy), (other_mark.posx, other_mark.posy))

        if distance < 10:
            return True
        else:
            return False