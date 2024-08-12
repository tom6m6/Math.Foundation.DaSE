# <center><b>数学基础第二次作业</b>
### <center>10215501419 姚修齐

#### 习题1
记$B = 
\left[
    \begin{matrix}
    b_{11} & b_{12} & \cdots & b_{1n} \\
    b_{21} & b_{22} & \cdots & b_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    b_{m1} & b_{m2} & \cdots & b_{mn}\\
    \end{matrix}
\right]$
1. $\because B$是有向图的关联矩阵，$\therefore$ B的每一列中都且仅有一个元素为 $-1$ ，一个元素为 $1$ ，其余元素均为 $0$；
又 $\because x$ 属于 $B$ 的左零空间 $\forall i \in \{1, 2, \cdots, n \}$ ，$b_{1i} x_1 + b_{2i} x_2 + \cdots + b_{mi}x_m = 0$ ；
令第 $j$ 个元素为 $1$ ，第 $k$ 个元素为 $-1$ ，此时必有 $x_j = x_k = c, c \in \mathbb{R}$ 。
又 $\because$ 该有向图连通，$\therefore x = c(1, 1, \cdots, 1)^T$ ，$\therefore B$ 的左零空间维度为1，且有 $Null(B^T) = span{1}$ ，得证。

2. $dim(Col(B^T)) = rank(B) = rank(B^T) = m - 1$ ，
记$B^T_{n \times m} = (\beta _1, \beta _2, \cdots , \beta _m)$ ，由1.知 $\beta_1 + \beta_2 + \cdots + \beta_m = 0$ ，即 行向量中任一个均可以由其余 $m - 1$ 个线性表示，$\therefore$ 任意 $m - 1$ 个行向量线性无关，可张成行空间，即 $Col(B^T)$ 可由 $B^T$ 中任意 $m - 1$ 个列向量生成，得证。

3. 由2.知$dim(Col(B^T)) = dim(Col(B)) = m - 1$ ，又 $T$ 是 $G$ 的生成树，$\therefore n = m - 1$ ，$B$ 满秩，$Col(B)$可由 $T$ 的关联矩阵的 $m - 1$ 个列向量生成，得证。

4. $\because dim(Col(B)) + dim(Null(B)) = n$ ，$dim(Col(B^T)) = m - 1$ ，$\therefore dim(Null(B)) = n - m + 1$ ；
若 $B$ 中的 $m - 1$ 条边可以连通全图，那么其余 $n - m + 1$ 条边可以去掉，生成 $n - m + 1$ 个小圈，得证。

####习题2
记 $x = (1, 1, 1)^T$ ，其投影目标子空间的基底 $b = (1, -1, 1)^T$ ；
$\therefore x$ 的正交投影 $\pi _U (x) = b \dfrac {b^T x}{\parallel b \parallel ^2} = \dfrac{1}{3} (1, -1, 1)^T$ 。

####习题4
将原矩阵变换为上三角矩阵： 
$U = \left( 
\begin{matrix}
5 & 3 & -1 & 3 \\
0 & 1 & 1 & -2 \\
0 & 0 & 3 & -1 \\
0 & 0 & 0 & 2 \\
\end{matrix}
\right)$ ，$\therefore L = \left( 
\begin{matrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
-1 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{matrix}
\right)
\left( 
\begin{matrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 1 & 0 & 1 \\
\end{matrix}
\right) = 
\left( 
\begin{matrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
-1 & 0 & 1 & 0 \\
0 & 1 & 0 & 1 \\
\end{matrix}
\right)$ , $\therefore$ 有 $LU$ 分解 $\left( 
\begin{matrix}
5 & 3 & -1 & 3 \\
0 & 1 & 1 & -2 \\
-5 & -3 & 4 & -4 \\
0 & 1 & 1 & 0 \\
\end{matrix}
\right) = 
\left( 
\begin{matrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
-1 & 0 & 1 & 0 \\
0 & 1 & 0 & 1 \\
\end{matrix}
\right)
\left( 
\begin{matrix}
5 & 3 & -1 & 3 \\
0 & 1 & 1 & -2 \\
0 & 0 & 3 & -1 \\
0 & 0 & 0 & 2 \\
\end{matrix}
\right)$ 。

####习题5
该 $Gauss$ 变换可表示为： $BA = 
\left(
\begin{matrix}
1 & 0 & 0 & \cdots & 0 \\
-\dfrac{a_{21}}{a_{11}} & 1 & 0 & \cdots & 0 \\
-\dfrac{a_{31}}{a_{11}} & 0 & 1 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
-\dfrac{a_{n1}}{a_{11}} & 0 & 0 & \cdots & 1\\
\end{matrix}
\right)
\left(
\begin{matrix}
a_{11} & a_{12} & a_{13} & \cdots & & a_{1n} \\
a_{21} & a_{22} & a_{23} & \cdots & & a_{2n} \\
a_{31} & a_{32} & a_{33} & \cdots & & a_{3n} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & a_{n3} & \cdots & & a_{nn} \\
\end{matrix}
\right)$ ；
记 $A_2$ 第 $i$ 行第 $j$ 列元素 $a' _{ij} = -\dfrac{a_{i1}}{a_{11}} a_{1j} + a_{ij}, a' _{ji} = -\dfrac{a_{j1}}{a_{11}} a_{1i} + a_{ji}$ ；
又 $\because A$ 对称，$\therefore a_{ij} = a_{ji}$ ，$\therefore a' _{ji} = a'_{ij}$ ，$\therefore A_2$ 为对称矩阵，得证。

####习题6
$\because A, B$ 为上三角矩阵，$\therefore \forall i, j \in \{1, 2, \cdots, n \}$ 满足 $i > j$ ，有 $a_{ij} = b_{ij} = 0$ ；
记 $C = AB$ ，则 $c_{ij} = \sum ^n _{k=1} a_{ik} b{kj}， c_{ij} \equiv 0$ ，即 $C$ 为上三角矩阵，得证。

####习题7
$\alpha _1 = (1, 2, 2)^T, \therefore a_1 = \parallel \alpha _1 \parallel _2 = 3$ ；
$\therefore \omega _1 = \dfrac{\alpha _1 - a_1 e_1}{\parallel \alpha _1 - a_1 e_1 \parallel _2} = \dfrac{1}{\sqrt{3}} (-1, 1, 1)^T$ ，
$\therefore H_1 = I - 2\omega _1 \omega ^T _1 = \dfrac{1}{3}
\left(
\begin{matrix}
1 & 2 & 2 \\
2 & 1 & -2 \\
2 & -2 & 1 \\
\end{matrix}
\right), 
H_1 A = 
\left(
\begin{matrix}
3 & 1 \\
0 & 0 \\
0 & 1 \\
\end{matrix}
\right)$ ；
$\alpha _2 = (0, 1)^T, \therefore a_2 = \parallel \alpha _2 \parallel _2 = 1$ ；
$\therefore \omega _2 = \dfrac{\alpha _2 - a_2 e_2}{\parallel \alpha _2 - a_2 e_2 \parallel _2} = \dfrac{1}{\sqrt{2}} (-1, 1)^T$ ，
$\therefore \widetilde{H_2} = I - 2\omega _2 \omega ^T _2 = 
\left(
\begin{matrix}
0 & 1 \\
1 & 0 \\
\end{matrix}
\right), \therefore
H_2 = 
\left(
\begin{matrix}
1 & 0 & 0 \\
0 & 0 & 1 \\
0 & 1 & 0\\
\end{matrix}
\right), 
H_2(H_1 A) = 
\left(
\begin{matrix}
3 & 1 \\
0 & 1 \\
0 & 0 \\
\end{matrix}
\right)$ ；
$Q = H_1 H_2 = \dfrac{1}{3}
\left(
\begin{matrix}
1 & 2 & 2 \\
2 & -2 & 1 \\
2 & 1 & -2\\
\end{matrix}
\right), R = 
\left(
\begin{matrix}
3 & 1 \\
0 & 1 \\
0 & 0 \\
\end{matrix}
\right)$ 。