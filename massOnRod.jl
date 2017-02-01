
using PyPlot
t = collect(0:.001:pi)

x = cosh(t)
#x = map(cosh, t)

plot(t,x)
show()
