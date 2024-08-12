#你可以把我的代码复制粘贴再运行
#使用幂法和反幂法
#使用瑞利商加速对幂法进行优化
import numpy as np
def powermethod(A,v0,eps):
    u=v0
    flag=1
    last_val=0
    n=0
    while flag:
        n=n+1
        v=A*u     
        val=v[np.argmax(np.abs(v))]        
        u=v/val   
        if (np.abs(val-last_val)<eps):
            flag=0
        last_val=val
        #print(np.asarray(u).flatten(),val)
    #print('主特征值:',val)
    #print('主特征值对应的特征向量:',np.asarray(u).flatten())
    #print('迭代次数:',n)
    return float(val),n

def raypower(A,v0,eps):
    u=v0
    flag=1
    last_val=0
    n=0
    while flag:
        n=n+1
        v=A*u
        t=((A*u).T*u)/(u.T*u)        
        val=t[0,0]
        u=v/val
        if (np.abs(val-last_val)<eps):
            flag=0
        last_val=val   
        #print(np.asarray(u).flatten(),val)
    #print('主特征值:',val)
    #print('主特征值对应的特征向量:',np.asarray(u).flatten())
    #print('迭代次数:',n)
    return float(val),n

if __name__ == '__main__':
    A=np.matrix([[5,-1,1],[-1,2,0],[1,0,3]], dtype='float')
    v0=np.matrix([[1],[1],[1]], dtype='float') #v0随机取
    eps=1e-10
    v1,n1=powermethod(A,v0,eps) #主特征值
    v3,n2=powermethod(A.I,v0,eps)
    v3=1/v3
    #print(v1,v3)
    print("|v1|/|v3|约等于",v1/v3)
    print("优化前迭代次数分别为:{}和{}".format(n1,n2))
    v11,n3=raypower(A,v0,eps)
    v31,n4=raypower(A.I,v0,eps)
    v31=1/v31
    print("|v1|/|v3|约等于",v11/v31)
    print("优化后迭代次数分别为:{}和{}".format(n3,n4))
    
#运行结果  
#|v1|/|v3|约等于 3.4823165803506173
#优化前迭代次数分别为:33和41       
#|v1|/|v3|约等于 3.4823165806525163
#优化后迭代次数分别为:19和23  