#Using Newton’s Forward Interpolation Formula, find the value of \(y\) when \(x=6\) from the following table:
x0=2
y0=10
x=6
h=2
delta=10

p_first_term=x-x0/2
print(f"so the p value is : {p_first_term}")
s=p_first_term*delta
print(f"so the 2 term  value is : {s}")
The_interpolated_value=y0+s
print(f"so the interpolated value is : {The_interpolated_value}")