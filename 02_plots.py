import matplotlib.pyplot as plt
name = "kunal"
colour = 'blue'
background = 'red'

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, color=colour)   # line color
plt.gca().set_facecolor(background, )  # background color

plt.show()
