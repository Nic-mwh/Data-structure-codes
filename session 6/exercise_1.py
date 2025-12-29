class node :
    def __init__(self , d):
        self.Data = d
        self.next = None

class linked_list :
    def __init__(self):
        self.head = None


    def Del_first(self):
        if self.head is None:
            print("error")
            return
        c = self.head
        self.head = c.next
        del c


    def Del_last(self):
        if self.head is None:
            print("error")
            return
        if self.head.next is None:
            self.Del_first()
            return
        c = self.head
        while c.next.nxt:
            c = c.next
        del c.next
        c.next = None

    def Del_after(self , x):
        if self.head is None:
            print("error")
            return
        if self.head.next:
            print("error")
            return
        c = self.head
        while c.next.next:
            if c.Data == x:
                a = c.next
                c.next = a.next
                del a
                return
            c=c.next
            print("not found")


    def Del_befor(self , x):
        if self.head is None:
            print("error")
            return
        if self.head.Data == x:
            print("error x1")
            return
        if self.head.next is None:
            print("error 1")
            return
        if self.head.Data.next == x:
            self.Del_first()
            return
        if self.head.next.next is None:
            print("error 2")
            return
        c = self.head
        while c.next.next:
            if c.next.next.Data == x:
                a = c.next
                c.next = a.next
                del a
                return
            c = c.next
            print("not found")

    def Del_all(self):
        while self.head:
            self.Del_first()


    def Del_x(self , x):
        if self.head is None:
            print("error")
            return
        if self.head.Data == x:
            self.Del_first()
            return
        c = self.head
        while c.next:
            if c.next.Data == x:
                a = c.next
                c.next = a.next
                del a
                return
            c = c.next
            print("not found")
                                             


