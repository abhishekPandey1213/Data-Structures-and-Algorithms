class Node:
    def __init__(self,info):
        self.info=info
        self.link= None
class SingleLinkedList:

    def __init__(self,head=None):
        
        self.head=None
    def display_list(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            print("List is : ")
            p=self.head
            while p is not None:
                print(p.info, " ",end= ' ')
                p=p.link
            print()
            
    def count_nodes(self):
        p=self.head
        n=0
        while p is not None:
            n += 1
            p=p.link
        print("Number of Nodes in the list is ",n)
    def search(self,x):
        position = 1
        p=self.head
        while p is not None:
            if p.info==x:
                print(x,"Found in the list at position",position)
                return True
            
            position += 1
            p=p.link
        else:
            print(x,"Not Found in the list")
            return False
            
        
            
    def insert_in_begining(self,data):
        temp = Node(data)
        temp.link= self.head
        self.head=temp
    def insert_at_end(self,data):
        temp= Node(data)
        if self.head is None:
            self.head = temp
            return
        
        p=self.head
        while p.link is not None:
            p=p.link
        p.link=temp
            
                
        
            
    def create_list(self):
        n = int(input(" Enter the no of nodes to be inserted"))
        if n==0:
            return
        for i in range(n):
            data=int(input("Enter the element to be inserted"))
            self.insert_at_end(data)
    def insert_after(self,data,x):
        p=self.head
        while p is not None:
            if p.info ==x:
                break
            p = p.link
        if p is None:
            print(x,"Not present in the list")
        else:
            temp= Node(data)
            temp.link=p.link
            p.link=temp
    def insert_before(self,data,x):
        # If list is empty
        if self.head is None:
            print("List is empty")
            return
        # x is in first node,new node is to be inserted before first node
        if x == self.head.info:
            temp=Node(data)
            temp.link=self.head
            self.head=temp
            return
        #Find reference to the predecessor of node containing x
        p = self.head
        while p.link is not None:
            if p.link.info ==x:
                break
            p=p.link
        if p.link is None:
            print(x," not present in the list")
        else:
            temp =Node(data)
            temp.link=p.link
            p.link=temp
    def insert_at_position(self,data,k):
        if k==1:
            temp = Node(data)
            temp.link=self.head
            self.head=temp
            return
        p=self.head
        i=1
        while i <k-1 and p is not None: # find the predecessor of the node k-1
            p=p.link
            i +=1
        if p is None:
            print("You can insert only at positio ",i)
        else:
            temp=Node(data)
            temp.link=p.link
            p.link=temp
    def delete_node(self,x):
        if self.head is None:
            print("List is empty")
            return
        # Deletion of first node
        if self.head.info==x:
            self.head=self.head.link
            return
        #Deletion in between or end
        p=self.head
        while p.link is not None:
            if p.link.info==x:
                break
            p=p.link
        if p.link is not None:
            print("Element ",x,"not in the list")
        else:
            p.link=p.link.link
            
        
            
    def delete_first_node(self):
        if self.head is None:
            return
        self.head=self.head.link
    def delete_last_node(self):
        if self.head is None:
            return
        if self.head.link is None:
            self.head= None
            return
        p=self.head
        while p.link.link is not None:
            p=p.link
        p.link=None
    def reverse_list(self):
        pass
    def bubble_sort_exdata(self):
        pass
    def bubble_sort_exlinks(self):
        pass
    def has_cycle(self):
        pass
    def find_cycle(self):
        pass
    def remove_cycle(self):
        pass
    def insert_cycle(self,data):
        pass
    def merge2(self,list2):
        pass
    def _merge2(self,p1,p2):
        pass
    def merge_sort(self):
        pass
    def _merge_sort_rec(self,listStart):
        pass
    
    def _divide_list(self,p):
        pass

######################################################################################################
    
list1 = SingleLinkedList()
list1.create_list()

while True:
    print(" 1. Display list.")
    print(" 2.Count the no. of nodes")
    print("3.Search for an element")
    print("4.Insert in empty list/Inser in the begining of the List")
    print("5.Insert a node at the end of the list")
    print("6.Insert a node after a specified node")
    print("7. Insert a node before a specified node")
    print("8.Insert a node at a given position")
    print("9.Delete first node")
    print("10. Delete last node")
    print("11. Delete any node")
    print("12.Reverse the list")
    print("13.Bubble sort by exchanging the data")
    print("14.Bubble sort by exchanging the links")
    print("15. MergeSort")
    print("16. Insert a cycle")
    print("17.Detect a cycle")
    print("18.Remove a cycle")
    print("19.Quit")

    option = int(input("Enter your choice(1-19)"))

    if option ==1:
        list1.display_list()
    elif option ==2:
        list1.count_nodes()
    elif option ==3:
        data = int(input("Enter data to be searched"))
        list1.search(data)
    elif option ==4 :
        data = int(input("Enter element to be inserted"))
        list1.insert_in_begining(data)
    elif option ==5:
        data = int(input("Enter element to be inserted at end"))
        list1.insert_at_end(data)
    elif option ==6:
        data = int(input("Enter element to be inserted"))
        x=int(input("Enter an element after which to insert"))
        list1.insert_after(data,x)
    elif option == 7:
        data = int(input("Enter element to be inserted"))
        x=int(input("Enter an element before which to insert"))
        list1.insert_before(data,x)
    elif option==8:
        data = int(input("Enter element to be inserted"))
        x=int(input("Enter an position at which element is insert"))
        list1.insert_at_position(data,x)
    elif option == 9:
        data = int(input("Enter an element to be deleted"))
        list1.delete_node(data)
    elif option ==10:
        list1.delete_first_node()
    elif option==11:
        list1.delete_last_node()
    elif option ==12:
        list1.reverse_list()
    elif option ==13:
        list1.bubble_sort_exdata()
    elif option ==14:
        list1.bubble_sort_exlinks()
    elif option ==15:
        list1.merge_sort()
    elif option ==16:
        data=int(input("Enter an element at which cycle has to be inserted :"))
        list1.insert_cycle(data)
    elif option ==17:
        if list1.has_cycle():
            print("List has a cycle")
        else:
            print("List does not have a cycle")
        
    elif option ==18:
        list1.remove_cycle()
    elif option ==19:
        break
    else:
        print("Wrong option")
    print()
        
        
        
        
        
        
        
    
    
    
    
    
    
