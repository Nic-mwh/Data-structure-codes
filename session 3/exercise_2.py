class Queue:
    def __init__(self ,max = 100):
        self.list=[None]* max
        self.front = -1
        self.rear = -1
    def ins(self,x):
        if (self.rear+1) % len(self.list) == self.front :
            print("Queue is Full")
            return
        if  self.front == -1 :
            self.front+= 0
            self.rear+= 0
            self.list[list.rear] = x
            return
        self.rear = (self.rear+1) % len(self.list)
        self.list[self.rear] = x
    def Delete(self):
        if self.front == -1 :
            print("Queue is empty")
            return     
        if  self.front == self.rear :
            k = self.list[self.front]
            self.front = -1
            self.rear = -1
            return k
        k = self.list[self.front]
        self.front = (self.front+1) % len(self.list)
        return k


    def is_Full(self):
        return (self.rear+1) % len(self.list) == self.front
    def is_empty(self):
        return self.front == -1        
    
















def show_invalid(self):
        if self.rear >= self.front:
            for i in range(self.rear+1 , len (self.list) , 1):
                print(self.list[i])
            for i in range(self.front):
                print(self.list[i])
        else:
            for i in range(self.rear+1 , self.front , 1):
                print(self.list[i])


















#if __name__ == "__main__" :
 #   q = Queue(3)
  #  print("Queue is ok")

 #   q.enqueue("A")
  #  q.enqueue("B")
  #  q.dequeue()
  #  q.enqueue("c")
  #  q.enqueue("D")

  #  q.show_logs()





#if __name__ == "__main__" :
  #  q = Queue(3)
 #   q.enqueue(30)
 #   q.enqueue(40)
   # q.dequeue()
  #  q.enqueue(50)
  #  q.enqueue(60)
  #  q.show_logs()




#if __name__ == "__main__" :
   # q = Queue(5)

   # numbers = [100 , 200 , 300]
   # for num in numbers:
    #    q.enqueue(num)

    #for i in range(2):
     #   q.dequeue()
    #q.show_logs()


#if __name__ == "__main__":
    #q = Queue(5)

   # for i in range(3):
      #  q.enqueue(i * 10)

    #for i in range(2):
     #   q.dequeue()

   # q.show_logs()              




q = Queue(3)

for i in range(18):
    q.ins(i)
    if q.size == q.capacity:
        q.delete() 

q.report_last_five_full_times()










