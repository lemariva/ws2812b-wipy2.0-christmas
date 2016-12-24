import math as m

class LEDs:
    data = []
    
    def __init__(self, ledNumber=144):
        self.ledNumber = ledNumber        
        self.data = []      
    
    def ledsmod1(self, percent=1):
        red = self.lighter((255,0,0), percent)
        green = self.lighter((0,255,0), percent)
        blue = self.lighter((0,0,255), percent)
        gold = self.lighter((255,255,0), percent)
    
        leds = int(m.floor(self.ledNumber/4))	               	
    
        self.data = []
        for x in range(0, leds):
            self.data.append(red)
            self.data.append(green)
            self.data.append(blue)
            self.data.append(gold)        
    
    def ledsmod2(self, color, percent=1):
        self.data = []
        for x in range(0, self.ledNumber):
            self.data.append(self.lighter(color, percent))        
    
    def getData(self):
        return self.data
    
    def movR(self):
        self.data = self.data[1:] + self.data[0:1]        
    
    def movL(self):
        self.data = [self.data[-1]] + self.data[0:-1]
		
    def lighter(self, color, percent):
        
        if(percent == 1):
            return color
        if(percent == 0):
            return ([0, 0, 0])	
        #if(percent < 0.65):		# driver not working ok with percent under 0.65 
        #   percent = 0.65
    
        rcolor = color[0] - color[0] * (1-percent)
        gcolor = color[1] - color[1] * (1-percent)
        bcolor = color[2] - color[2] * (1-percent)
        newcolor = ([(rcolor), (gcolor), (bcolor)])
        return newcolor		
        
        
