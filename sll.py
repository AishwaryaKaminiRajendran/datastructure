class node:
    def __init__(self,data):
        self.data=data
        self.nextt=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self):
        val=int(input("enter val to insert"))
        newnode=node(val)
        newnode.nextt=self.head
        self.head=newnode
    def insertatend(self):
        val=int(input("enter val to insert at end"))
        newnode=node(val)
        if self.head is None:
            self.head=newnode
            return
        temp=self.head
        while(temp.nextt):
           temp=temp.nextt
        temp.nextt=newnode
        
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.nextt
s1=sll()
ch=0
while ch!=6:
    print("1.insertatbeg 2.delatbeg 3.display 4.search 5.insertatend 6.exit")
    ch=int(input())
    if ch==1:
        s1.insertatbeg()
        s1.display()
    elif ch==3:
        s1.display()
    elif ch==5:
        s1.insertatend()
        1.display()
    else:
        print("invalid choice")
        
        
