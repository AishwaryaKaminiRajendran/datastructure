class node:
    def __init__(self,data):
        self.data=data
        self.nextt=None
class sll:
    def __init__(self):
        self.head=None
    
    def insertatbeg(self):
        val=int(input("enter val to insert at beg"))
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
    
    def insertatmid(self):
        n=int(input())
        temp=self.head
        pos=1
        while pos<n:
            temp=temp.nextt
            pos=pos+1
        val=int(input("enter val to insert at end"))
        newnode=node(val)
        newnode.nextt=temp.nextt
        temp.nextt=newnode
        
    def deleteatbeg(self):
        temp=self.head
        self.head=temp.nextt
        temp.nextt=None
    
    def deleteatend(self):
        temp=self.head
        while temp.nextt!=None:
            prev=temp
            temp=temp.nextt
        if temp.nextt==None:
            prev.nextt=None
            
    def deleteatmid(self):
        n=int(input())
        temp=self.head
        pos=1
        while pos<n:
            prev=temp
            temp=temp.nextt
            pos=pos+1
        prev.nextt=None
        prev.nextt=temp.nextt
        
    def search():
        m=int(input("enter value to be searched"))
        temp=self.head
        while temp.nextt!=None:
            if m==temp.data:
                print("yes")
        temp=temp.nextt
        else:
            if m==temp.data:
                print("yes")
            else:
                print("no")
        
        
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.nextt
    
s1=sll()
ch=0
while ch!=10:
    print("1.insertatbeg 2.delatbeg 3.display 4.search 5.insertatend 6.insertatmid 7.deleteatend 8.deleteatmid")
    ch=int(input())
    if ch==1:
        s1.insertatbeg()
        s1.display()
    elif ch==3:
        s1.display()
    elif ch==5:
        s1.insertatend()
        s1.display()
    elif ch==6:
        s1.insertatmid()
        s1.display()
    elif ch==2:
        s1.deleteatbeg()
        s1.display()
    elif ch==7:
        s1.deleteatend()
        s1.display()
    elif ch==3:
        s1.search()
        s1.display()
    elif ch==8:
        s1.deleteatmid()
        s1.display()
    elif ch==4:
        s1.search()
    else:
        print("invalid choice")
        
        
