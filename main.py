from pyscript import Element, display
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.linspace(0,5,100)
y = np.sin(x)
ax.plot(x,y,label='$y=\\sin(x)$')
ax.set_title("Sine")
ax.legend()
display(fig, target='container', append=False)

def plot():
    x = eval(Element('x').value)
    y = eval(Element('y').value)
    kwargs = eval(Element('kwargs').value)
    ax.clear()
    ax.plot(x,y,**kwargs)
    display(fig, target='container', append=False)