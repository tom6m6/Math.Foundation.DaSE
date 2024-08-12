'''

迭代1次后的函数值是0.5483225357352826 此时在[-0.41604038  0.13139973]
迭代2次后的函数值是0.0015494982987473648 此时在[-0.00177646 -0.02265656]
迭代3次后的函数值是5.219734036052285e-06 此时在[-0.00011553 -0.00131399]
迭代4次后的函数值是1.7546426992072408e-08 此时在[-6.74554262e-06 -7.61794296e-05]
迭代5次后的函数值是5.897435933282354e-11 此时在[-3.91229201e-07 -4.41645324e-06]
最优值是
[-3.91229201e-07 -4.41645324e-06]

'''
import numpy as np

def hessian(x):
    return np.array([ [6-2*x[1] , (-2)*x[0] ],
              [(-2)*x[0] , 6 ] ]) 
def f1(x):
    return  np.array([ 6*x[0]-2*x[0]*x[1],6*x[1]-x[0]*x[0] ])

def f(x):
    return 3*(x[0]**2)+3*(x[1]**2)-((x[0]**2)*(x[1]))

def wolfe(x,dir,t,c1=0.5,c2=0.618):
  #看看当前是否满足wolfe条件
  #当前在x 方向dir 步长t
  #系数c1 c2
  #要保证 0<c1<c2<1
  cond1=( f(x)+c1*t*np.dot(f1(x),dir)>=f(x+t*dir) )
  cond2=( np.dot(f1(x+t*dir),dir)>=c2*np.dot(f1(x),dir) )
  return (cond1 and cond2)

def newton_method(x0,eps=1e-8):
    x=x0 
    dir=(np.dot(np.linalg.inv(hessian(x)),f1(x)))*(-1) #方向
    iter=0 #迭代次数
    redu=0.9 #缩小系数

    iter1=0

    while float(np.dot((-1)*dir,f1(x)))>eps and iter<6666:
        iter=iter+1
        iter1=0

        #使用迭代法非精确线搜索步长直到可能值满足wolfe条件
        t=20 #初始步长
        while(wolfe(x,dir,t)==0 and iter1<=100):
            t=redu*t
            iter1=iter1+1
            

        x=x+t*dir
        print("迭代{}次后的函数值是{} 此时在{}".format(iter,f(x),x))
        dir=(np.dot(np.linalg.inv(hessian(x)),f1(x)))*(-1)
        if iter==6666:
            print('迭代了太多次没有结果\n')
    return x 

if __name__=="__main__":
    x0=np.array([1.5,1.5])
    xans=newton_method(x0)
    print("最优值在")
    print(xans)