
class Products():
    def _init_(self):
       # initializing variable
        pName=""
        pPrice=0
        pWeight=0
        
        
    def prod_list(self,barcode):
        productsfile=open("products.txt")
        product=None
        for line in productsfile:
            if barcode in line:
                product=line
        detail=list()#array list of name,price and weight of item
        if(product!=None):
            productdetail=product.split(",")
            pName=productdetail[1]
            pPrice=productdetail[2]
            pWeight=productdetail[3]
            #==========inserting every time at 0,1,2 position of detail array====
            detail.insert(0,pName) 
            detail.insert(1,pPrice)
            detail.insert(2,pWeight)
            return detail; 
            
        else:
            #if item of barcode is not in database
            print("item you scan is not listed in store")
        
        
