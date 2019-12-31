from abc import ABCMeta,abstractmethod
# 引入abcmeta和abstramethod来定义抽象类和抽象方法
class Observer(metaclass=ABCMeta):
    """观察者的基类"""
    @abstractmethod
    def update(self,observable,object):
        pass


class Observable:
    """被观察者的基类"""
    def __init__(self):
        self.__observers=[]
    
    def addObserver(self,Observer):
        self.__observers.append(Observer)

    def removeObserver(self,Observer):
        self.__observers.remove(Observer)

    def notifyObservers(self,object=0):
        for i in self.__observers:
            i.update(self,object)

"""以上均为基类"""

class WaterHeater(Observable):
    """热水器类 继承自被观察者"""
    def __init__(self):
        super().__init__()
        self.__temperature=25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self,temperature):
        self.__temperature=temperature
        print("当前温度是："+str(self.__temperature)+" C")
        self.notifyObservers()


class WashingMode(Observer):
    """继承自观察者,该模式适用于洗澡"""
    def update(self,observable,object):
        if  isinstance(observable,WaterHeater) and observable.getTemperature()>=50 and observable.getTemperature()<70:
            print("水已经烧开，可以用来洗澡了")


class DrinkingMode(Observer):
    """继承自观察者,该模式适用于喝水"""
    def update(self,observable,object):
        if  isinstance(observable,WaterHeater) and observable.getTemperature()>=100:
            print("水已经烧开，可以用来喝水了")
    

def testWaterHeater():
    heater=WaterHeater()
    washingObser=WashingMode()
    drinkingObser=DrinkingMode()
    heater.addObserver(washingObser)
    heater.addObserver(drinkingObser)
    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)

testWaterHeater()