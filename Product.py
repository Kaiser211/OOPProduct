class Product(object):
    def __init__(self,price, itemName,weight,brand):
        print "creating Product"
        self.price=price
        self.itemName=itemName
        self.weight=weight
        self.brand=brand
        self.status="for sale"
        self.tax=self.price*0.06

    def Sell(self):
          self.status="Sold"
          print self.status
    
    def addTax(self):
        print self.price+self.tax

    def retun(self,reason):
        self.reason=reason
        if reason=="defective":
            self.status="defective"
            self.price=0
        elif reason=="new box":
            self.status=="for sale"
        elif reason=="open box":
            self.status=="used"
            self.price=self.price*0.80
        
    def displayInfo(self):
        print  self.price  
        print  self.itemName
        print  self.weight
        print  self.brand
        print  self.status
        print  self.tax

p1=Product(1,"d",2,"h")
p1.Sell()
p1.addTax()
p1.retun("open box")
p1.displayInfo()