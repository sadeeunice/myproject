import interfaces


class LunarLander:
    
    def __init__(self, alt, velo, fuel):
        self.__altitude = alt
        
        self.__velocity = velo
        
        self.__fuel = fuel
        
    def getAltitude(self):
        
        return self.__altitude
    
    def getVelocity(self):
    
        return self.__velocity
    
    def getFuel(self):
        
        return self.__fuel
        
    def update(self, thrust_amount):
        
        if thrust_amount < self.__fuel:
            self.__fuel = self.__fuel - thrust_amount
        else:
            self.__fuel = thrust_amount
            self.__fuel = 0
        
        self.__velocity =  abs(self.__velocity)
        self.__velocity = -((self.__velocity + (thrust_amount * 4)) + 2)
            
        self.__altitude = self.__altitude + self.__velocity
    
class LanderGame:
    
    def __init__(self):
        
        self.__lander = LunarLander(200, 0, 30)
       
        self.__interface = interfaces.TextLanderInterface()
    
    def play(self): 
        
        
        while self.__lander.getAltitude() > 0:
            
            self.__interface.showInfo(self.__lander)
            
            thrust = self.__interface.getThrust()
            
            self.__lander.update(thrust)

        if self.__lander.getVelocity() < -10:
            self.__interface.showCrash()
        else:
            self.__interface.showLanding()
            
        self.__interface.close

def main():
    game = LanderGame()
    game.play()


if __name__ == '__main__':
    main()        
        

