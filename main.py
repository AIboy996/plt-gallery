import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.linspace(0,5,100)
y = np.sin(x)
ax.plot(x,y,label='$y=\\sin(x)$')
ax.set_title("Sine")
ax.legend()
display(fig, target='container', append=False)

def twitch():
    ax.clear()
    A = np.random.randint(1,6)*np.random.choice([1,-1])
    omega,phi = np.random.randint(-10,10,2)
    x = np.linspace(0,5,500)
    y = A*np.sin(omega*x+phi)
    ax.plot(
        x,
        y, 
        label=f"$y={'' if A==1 else A}\\sin({'' if omega==1 else omega}x{'+' if phi>=0 else ''}{phi})$"
    )
    ax.set_title("Sine")
    ax.legend()
    display(fig, target='container', append=False)