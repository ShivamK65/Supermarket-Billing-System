from products import Products

product_list=Products()

single_product = []
single_price = list()
single_weight= list()

class CheckOutRegister:

    def _init_(self):
        #variable initialization
        self.n=n
        self.single_product = single_product
        self.single_price = single_price
        self.single_weight= single_weight

    def get_prod_detail(self,barcode):
        
        #passing value to the product.py to find element of barcode
        product=product_list.prod_list(barcode)
        #if product array is not empty
        if (product!=None):
            
            single_product.append(product[0])
            single_price.append(product[1])
            single_weight.append(product[2])
            #total_products_cost += product[2]
            print(str(product[0]) + " -> $" + str(product[1]))

    def total_item(self):
        n=len(single_product)
        #printing element of array single_product and single_price
        for i in range(int(n)):
            print('{:>12} {:>12} '.format(single_product[i],"$"+str(single_price[i])))

    def total_payable(self):
        #findig total cost in the cart
        
        n=len(single_product) #getting count of element in array
        total_products_costs=0.0
        for i in range(int(n)):
            cost=float(single_price[i])
            total_products_costs +=cost
            
        return total_products_costs;
    def clear_value(self):
        del single_product[:]
        del single_price[:]
        del single_weight[:]
        


