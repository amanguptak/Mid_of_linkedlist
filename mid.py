class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def insert():
    l= [int(ele) for ele in input().split()]
    head=None
    temp=None
    for i in l:
        if i==-1:
            break
        newnode = Node(i)
        if head==None:

            head=newnode
            temp=newnode
        else:

            temp.next=newnode
            temp=newnode

    return head

def LLprint(head):
     cur=head
     while cur is not None:
            print(f"{cur.data} ->",end="")
            cur = cur.next
     print("None")

     return

def rev(head):
    if head is None or head.next is None:
        return head,head
    shead,stail=rev(head.next)
    stail.next=head
    head.next=None
    return shead,head



def midu(head):

    slow=head
    fast=head
    while fast.next!=None and fast.next.next!=None:
        fast=fast.next.next
        slow=slow.next
    return slow.data





head=insert()
LLprint(head)
#for reversing a Linked list
head , tail= rev(head)
print("reversed linked list is" )
#for mid of linlked list
LLprint(head)
value=midu(head)
print(value)
