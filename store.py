# Python program for customer portal of a store

d= {'Bread':{'q':5,'p':15},'Sugar':{'q':10,'p':30},'Chips':{'q':10,'p':20},'Eggs ':{'q':20,'p':10}}

prod= list(d.keys())
cart= {}
#c= list(cart.keys())
#print(c)
flag= 1


# Show items in store

def menu():
    print("\n\n\n\n============================ Store =====================================\n\n")
    print("  S.No.\t\tProducts\t\tQuantity\t\tPrice\n")
    global d
    global prod
    for i in range(len(prod)):
        print('   ',i+1,'\t\t',prod[i],'\t\t\t ',d[prod[i]]['q'],'\t\t\t  ',d[prod[i]]['p'])
    print("\n\n=========================================================================\n\n")



# Show cart

def display_cart():
    global cart
    c= list(cart.keys())
    print("\n\n\n\n============================ Cart ==========================================\n\n")
    print("  S.No.\t\tProducts\t\tQuantity\t\tTotal Price\n")
    for i in range(len(c)):
        print('   ',i+1,'\t\t',c[i],'\t\t\t ',cart[c[i]]['q'],'\t\t\t  ',cart[c[i]]['p'])
    print("\n\n==============================================================================\n\n")


# Menu for management system

while(flag!=0):
    try:
        print("\n\n=========================================\n")
        print("\n\tWelcome to the Store!!\n\n")
        print("1. Proceed for shopping\n2. Proceed to cart\n3. Exit")
        print("\n==========================================\n\n")
        ch= int(input("Please select one of the options (1-3): "))
        c= list(cart.keys())
        if ch==1:
            menu()
            print("Select an item (1-%d):"%len(prod),end="")
            item= int(input())
            if prod[item-1]:
                quantity= int(input("Enter quantity you want: "))
                
                if quantity>d[prod[item-1]]['q']:
                    print("\nSorry!! We don't have enough stock.")
                else:
                    
                    if prod[item-1] in c:
                        lst=[]
                        for a in list(cart[prod[item-1]].values()):
                            lst.append(a)
                        cart[prod[item-1]]= {'q':quantity+lst[0],'p':d[prod[item-1]]['p']*quantity+lst[1]}
                        d[prod[item-1]]['q']-= quantity
                    else:
                        cart[prod[item-1]]= {'q':quantity,'p':d[prod[item-1]]['p']*quantity}
                        d[prod[item-1]]['q']-= quantity
                
            else:
                print("\nIncorrect value!!Please try again.")


        elif ch==2:
            display_cart()


        elif ch==3:
            flag=0
            print("\n\n\tThank you for coming!!!\n\n")


        else:
            print("\nIncorrect value!!Please try again.")

    except (ValueError, IndexError):
            print("\nIncorrect value!!Please try again.")








"""
        Developed By:        Jivesh Singh
        College:             SRM University, Delhi-NCR
        Registration No.:    10316210048
        E-mail      :        jiveshs98@hotmail.com

"""
