import numpy
import scipy   
from room import Room
from inventory import Inv
from inventory import Item

class Normalize():
    # this is how random values are generated. They are generated on a normal distribution, with a mean as the 'base' spec and the standard deviation set to 15% of the mean by default but changeable. If an item with a certain rarity predetermined is generated, the returned result will specifically obey that. Values less than 0 are also eliminated.
    def __init__(self, mean, alt_deviation, rarity):
        self.mean = mean
        self.deviation = .15*self.mean
        try:
            if alt_deviation >= 0:
                self.deviation = alt_deviation
            else:
                pass
        except:
            pass
        self.rarity = 0
        try:
            if rarity >= 0:
                self.rarity = rarity
            else:
                pass
        except:
            pass
    def draw_norm(self):
        draw_loop = True
        while draw_loop == True:
            output_return = numpy.random.normal(loc=self.mean, scale=self.deviation, size=None)
            if output_return >= self.rarity:
                draw_loop = False
            else:
                pass
        return output_return
class Rarity_Check(Normalize):
    def __init__(self, mean, alt_deviation, check_spec, rarity):
        Normalize.__init__(self, mean, alt_deviation, rarity)
        self.value = check_spec
    def check_rarity(self):
        output = scipy.stats.norm(self.mean, self.deviation).cdf(self.value) 
        return output
