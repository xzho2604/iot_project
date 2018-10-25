import matplotlib.pyplot as plt

def cal(a,b,c,d,e,f):
    x = (a**2-b**2)
    y = (c**2-d**2)
    z = (e**2-f**2)
    # print(x, y, z)
    return x-y-z

# x = cal(23.6,32.3,50,70,70,30)
# y = cal(35.7,32.3,20,70,20,30)
# a = (4 * y + x )/440
# b = (y - (a * 100))/20
# print(x, y)
# print(a, b)
# print( 40 * a - 80 * b)
# print( 100 * a + 20 * b)


fig = plt.figure()
ax = fig.add_subplot(111)
circle_a = plt.Circle(xy=(50, 70), radius=23.6, color='red',fill=False, linewidth=4)
circle_b = plt.Circle(xy=(20, 20), radius=35.7, color='yellow', fill=False, linewidth=4)
circle_c = plt.Circle(xy=(70, 30), radius=32.3, color='green', fill=False, linewidth=4)
ax.add_patch(circle_a)
ax.add_patch(circle_b)
ax.add_patch(circle_c)
x, y = 0, 0
plt.axis([-20, 100, -20, 100])
plt.axis('equal')
plt.show()
