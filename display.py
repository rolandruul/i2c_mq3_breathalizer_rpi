import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class Display:

    # Initialize Adafruit SSD1306
    def __init__(self):

        self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=None)
        self.disp.begin()
        self.disp.clear()
        self.disp.display()

        # Width and height of display
        self.w = self.disp.width
        self.h = self.disp.height

        # Default font
        self.font = ImageFont.truetype('Montserrat-Light.ttf', 16)

        # Creates blank image for drawing
        self.image = Image.new('1', (self.w, self.h))

        # Get drawing object to draw on that image
        self.draw = ImageDraw.Draw(self.image)

        # Clear that image
        self.clearImage()

    # Clearing the image
    def clearImage(self):

        # Drawing black filled box to clear image
        self.draw.rectangle((0, 0, self.w, self.h), outline = 0, fill = 0)

    # Set font
    def setFont(self, font, size):
        self.font = ImageFont.truetype(font, size)

    # Displaying text
    def write(self, x, y, text):
        self.draw.text((x, y), str(text), font=self.font, fill=255)
        self.disp.image(self.image)
        self.disp.display()
