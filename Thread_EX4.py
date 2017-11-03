import threading
class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()    #重构run函数必须要写
        self.n=n
    def run(self):
        print('current task: ',n)

if __name__=='__main__':
    t1=MyThread('thread 1')
    t2 = MyThread('thread 2')
    t1.start()
    t2.start()