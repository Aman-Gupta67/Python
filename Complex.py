import math
class Mycomplex:
    def __init__(self,real=0,img=0):
        self.__real=real
        self.__img=img
        def getReal(self):
            return self.__real

        def setReal(self,new_real):
            self.__real=new_real

        def getImg(self):
            return self.__img

        def setImg(self,new_img):
            self.__img=new_img

    def __str__(self):
        return str(self.__real)+"+"+str(self.__img)+"i"

    def __eq__(self,other):
        return(self.__real==other.__real) and (self.__img==other.__img)

    def __add__(self,other):
        r=self.__real+other.__real
        i=self.__real+other.__img
        return Mycomplex(r,i)

    def __mul__(self,other):
        r=self.__real*other.__real-self.__img*other.__img
        i=self.__real*other.__img+ self.__img*other.__real
        return Mycomplex(r,i)

    def __di__(self, other):
        r = (self.__real*other.__real+self.__img*other.__img)/(other.__real**2+other.__img**2)
        i = (self.__real*other.__img- self.__img*other.__real)/(other.__real**2+other.__img**2)
        return Mycomplex(r, i)

    def __mod1__(self):
        return math.sqrt(abs(self.__real**2+self.__img**2))



    def __sub__(self, other):
        r = self.__real - other.__real
        i = self.__img - other.__img
        return Mycomplex(r, i)

a=Mycomplex(2,1)
b=Mycomplex(5,6)
print(a.__add__(b))
print(a.__sub__(b))
print(a.__mul__(b))
print(a.__di__(b))
print(a.__mod1__())
print(b.__mod1__())


