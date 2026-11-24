from qr_mark.qr_gen import QrGen


class QrSettings:

    def __init__(self, count=8, output="./out/mark_%03d.png", size=25, x=None, y=None):
        self.count = count
        self.output = output
        self.x = x
        self.y = y
        if x is not None and y is not None:
            self.size = x * y
        else:
            self.size = size

    def fix_size_from_x_y(self):
        if self.x is not None and self.y is not None:
            self.size = self.x * self.y

    def compare(self, other) -> bool:
        return (self.x == other.x
                and self.y == other.y
                and self.count == other.count
                and self.output == other.output
                and self.size == other.size)

    def get_size_rect(self):
        if self.x is None and self.y is None and self.size is None:
            raise Exception("invalid size, no size provided")

        if self.x is None and self.y is None:
            return QrGen.get_square_size(self.size)

        if self.x is None:
            rect = [int(self.size / self.y), self.y]
            if rect[0] * self.y != self.size:
                raise Exception("invalid size, can't determine X")
            return rect

        if self.y is None:
            rect = [self.x, int(self.size / self.x)]
            if rect[1] * self.x != self.size:
                raise Exception("invalid size, can't determine Y")
            return rect

        return [self.x, self.y]

    def get_output(self, _id):
        return str(self.output % _id)
