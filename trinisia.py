class Cart:
    def __init__(self):
        #create an empty list to store shopping items:
        self.emptylist = {}
#         self.add = add
#         self.delete = delete
#         self.show = show   

    def addcart(self):  
        item = input ('What would you like to add to your shopping cart? ')
        amount = int(input ('How many of these would you like to add? '))
        self.emptylist[item] = amount

    def deletecart(self):
        print(f'Here is your list again:{self.emptylist}')
        delete = input ('What would you like to remove? ')
        del self.emptylist[delete]

    def showcart(self):
         print(f'These are the items in your cart:{self.emptylist}')



    def bits(self):

        #keep looping through questions til customer is ready to checkout:
        while True:
            bit = input ('Do you want to: Show, Add, Delete, or Quit? ')
        #give each bit a print statement corresponding to the command
            if bit.lower() == "quit":
                print (f'Thanks for shopping with us! These are your final items:{self.emptylist.keys()}')
                break
            elif bit.lower() == "show":
                self.showcart()

            elif bit.lower() == "add":
                self.addcart()

            elif bit.lower() == "delete":
                self.deletecart()
            else:
                print ('Try again :(')
        
#creating an instance of class. instantiation (init method builds):
add = Cart()
# delete = Cart()
# show = Cart()
add.bits()