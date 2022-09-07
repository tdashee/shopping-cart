from builtins import staticmethod

class Basket:
    GST=0       #for storing maximum gst of all products
    def __init__(self,name,price,gst,n):
        self.prod_name=name
        self.unit_price=int(price)
        self.gst=int(gst)
        self.quantity=int(n)

    #function to calculate total price of the whole shopping cart
    @staticmethod
    def totalAmount(cart):
        total=0
        for i in cart:
            price=i.unit_price
            if price>=500:
                price-=(0.05*price)  #applying discount on product
            price=price*i.quantity   #total price of product
            t_gst=(i.gst*price)/100   # gst amount
            Basket.GST=max(Basket.GST,t_gst)
            total+=(price+t_gst)
        return total
    def __str__(self):
        # print(self.prod_name,self.unit_price,self.gst,self.qantity)
        return f"{self.prod_name},{self.unit_price},{self.gst},{self.quantity}"



if __name__ == '__main__':
    n=int(input("number of products:"))
    basket=[]
    print("enter product name, unit price, gst in %, quantity :")
    for i in range(n):
        basket.append(Basket(*(input().split())))
        # basket.append(ob)
    for i in basket:
        print(i)

    print("total amount of cart:",Basket.totalAmount(basket))
    print("maximum gst paid",Basket.GST)

# sample input:
# lw 1100 18 1
# um 900 12 2
# cig 200 28 3
# honey 100 0 4