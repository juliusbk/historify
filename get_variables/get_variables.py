from PIL import Image
import urllib, cStringIO
from math import sqrt
import pickle

##### MAIN CLASS #####
class image:
    def __init__(self, url):
        #Define:
        self.size = 100

        #Download:
        self.url = url
        f = urllib.urlopen(url)
        self.original = Image.open( cStringIO.StringIO(f.read()) )

        # Now resize and crop:
        self.img = self.processed()

        #And analyze:
        self.make_histograms()
        self.brightness_RGB()

    def processed(self):
        width, height = self.original.size
        if width<height:
            new_width = self.size
            new_height = int(round(self.size*height/float(width)))
            left = 0
            right = self.size
            upper = int((new_height-self.size)/2.0)
            lower = self.size + upper
        else:
            new_width = int(round(self.size*width/float(height)))
            new_height = self.size
            left = int((new_width-self.size)/2.0)
            right = self.size + left
            upper = 0
            lower = self.size
        
        img = self.original.resize((new_width, new_height))
        img = img.crop( (left, upper, right, lower) )

        return img

    def make_histograms(self):
        self.hist = self.img.histogram()
        self.red = self.hist[0:256]
        self.green = self.hist[256:256*2]
        if len(self.green)==0:
            self.green = self.red
            self.blue = self.red
        else:
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

def index_mean( l ):
    wi = sum( [ l[i]*i for i in xrange(len(l)) ] )
    return wi / float( sum(l) )

def get_all_in_range(first=100, last=681):
    l = [] #list of tuples: id, brightness, red, green, blue
    for i in range(first, last+1):
        print "Getting image", i-first+1, "out of", last-first
        im = image( parse_id(i) )
        l.append( (i, im.brightness, im.mean_red, im.mean_green, im.mean_blue) )
    f = open("images_info.pickle", "w")
    pickle.dump(l, f)

##### TESTING #####
if __name__=="__main__":
    get_all_in_range()
