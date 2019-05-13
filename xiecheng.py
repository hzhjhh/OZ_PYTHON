import time
m = [1]

def work1(m):

    print('你在做第%d个包子' % m[0])
    time.sleep(0.5)
    yield

def work2(m):

    print('我在吃第%d个包子' % m[0])
    time.sleep(0.5)
    m[0] +=1
    yield

if __name__ == '__main__':
    for i in range(3):
        task1 = work1(m)
        task2 = work2(m)
        # 需要使用next获取下一个数据
        next(task1)
        next(task2)
