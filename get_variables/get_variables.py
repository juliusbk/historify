from PIL import Image
import urllib, cStringIO
from math import sqrt

##### MAIN CLASS #####
class image:
    def __init__(self, url):
        #Define:
        self.size = 100

        #Download:
        self.url = url
        f = urllib.urlopen(url)
        self.original = Image.open( cStringIO.StringIO(f.read()) )

        # Now crop and resize:
        self.img = self.processed( self.original )

        #And analyze:
        self.make_histograms()
        self.brightness_RGB()

    def processed(self):
        width, height = self.original.size
        

    def make_histograms(self):
        self.hist = self.img.histogram()
        self.red = self.hist[0:256]
        self.green = self.hist[256:256*2]
        self.blue = self.hist[256*2:256*3]

    def brightness_RGB(self):
        self.mean_red = index_mean( self.red )
        self.mean_green = index_mean( self.green )
        self.mean_blue = index_mean( self.blue )
        # see http://www.nbdtech.com/Blog/archive/2008/04/27/Calculating-the-Perceived-Brightness-of-a-Color.aspx for values
        self.brightness = sqrt( 0.241*self.mean_red**2 + 0.691*self.mean_green**2 + 0.068*self.mean_blue**2 )

##### HELPER FUNCTIONS #####
def parse_id( ID ):
    """ Takes int or string """
    base = "http://93.167.225.237/CIP/preview/thumbnail/testCatalog/"
    return base + str(ID)

def mean( l ):
    return sum(l)/float(len(l))

def index_mean( l ):
    wi = sum( [ l[i]*i for i in xrange(len(l)) ] )
    return wi / float( sum(l) )

##### TESTING #####
if __name__=="__main__":
    im = image( parse_id(150) )
    print im.blue

