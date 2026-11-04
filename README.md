# rainy-nights-generating-fractals
quiet thoughts, endless patterns
## Mandelbrot
<p align="center">
<img src="output/mandelbrot.png" width="500">
</p>

The Mandelbrot set is defined by iterating:

$$
z_{n+1} = z_n^2 + c, \qquad z_0 = 0
$$

where $c$ is a complex number. 

A point belongs to the set if the sequence remains bounded.

## Barnsley fern
<p align="center">
<img src="output/barnsley_fern.png" width="500">
</p>

Barnsley's fern is generated using four affine transformations. Each transformation is defined as:

$$
f_i(x, y)
=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}
\begin{pmatrix}
x\\
y
\end{pmatrix}
+
\begin{pmatrix}
e\\
g
\end{pmatrix}
$$

The four transformation are:

*1. Stem (1%)*

$$
f_1 (x,y)
=
\begin{pmatrix}
0.00&0.00\\
0.00&0.16
\end{pmatrix}
\begin{pmatrix}
x\\
y
\end{pmatrix}
$$

*2. Successively smaller leaflets (85%)*

$$
f_2 (x,y)
=
\begin{pmatrix}
0.85&0.04\\
-0.04&0.85
\end{pmatrix}
\begin{pmatrix}
x\\
y
\end{pmatrix}
+
\begin{pmatrix}
0.00\\
1.60
\end{pmatrix}
$$

*3. Largest left-hand leaflet (7%)*

$$
f_3 (x,y)
=
\begin{pmatrix}
0.20&-0.26\\
0.23&0.22
\end{pmatrix}
\begin{pmatrix}
x\\
y
\end{pmatrix}
+
\begin{pmatrix}
0.00\\
1.60
\end{pmatrix}
$$

*4. Largest right-hand leaflet (7%)*

$$
f_4 (x,y)
=
\begin{pmatrix}
-0.15&0.28\\
0.26&0.24
\end{pmatrix}
\begin{pmatrix}
x\\
y
\end{pmatrix}
+
\begin{pmatrix}
0.00\\
0.44
\end{pmatrix}
$$