import tkinter as tk
from matplotlib import pyplot as plt
import numpy as np
import random as rng

#Start
window = tk.Tk()
window.title('Julia Set Generator')
colors = ('afmhot','afmhot_r','Blues','Blues_r','bone','bone_r','BrBG','BrBG_r','BuGn','BuGn_r','BuPu','BuPu_r','cividis','cividis_r','CMRmap','CMRmap_r','cool','cool_r','coolwarm','coolwarm_r','copper','copper_r','cubehelix','cubehelix_r','flag','gist_earth','gist_earth_r','gist_heat','gist_heat_r',
            'gist_ncar_r','gist_stern','gnuplot','gnuplot2','hot','inferno','inferno_r','jet_r','magma','magma_r','nipy_spectral','nipy_spectral_r',
            'ocean','pink','PRGn','PRGn_r','PuRd','PuRd_r','RdBu','RdBu_r','RdGy','RdGy_r','RdPu_r','twilight','twilight_r','twilight_shifted','twilight_shifted_r')


window.iconphoto(False, tk.PhotoImage(file = 'jsetappicon.png')) 

#FUNCTIONS
def mandelbrot(q,max_iter):
    z=0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z**2 + q

    return max_iter

def findc():
    q = 3
    qjul = 1
    while qjul < 10 or qjul == 100:
        a = rng.uniform(float(re0.get()),float(re1.get()))
        b = rng.uniform(float(im0.get()),float(im1.get()))
        q = complex(a,b)
        qjul = mandelbrot(q,100)

        re.delete(0, len(re.get()))
    re.insert(0, str(a))
    im.delete(0, len(im.get()))
    im.insert(0, str(b))
    cset.config(text=str(qjul))

def julia(z, max_iter):
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return max_iter

def Generate():
    global c, cm, jset, x, y, zo, centerr, centeri

    plt.clf()
    
    if r.get()==0:
        a = re.get()
        b = im.get()
        c = complex(float(a), float(b))
    
    elif r.get()==1:
        a = rng.uniform(float(re0.get()),float(re1.get()))
        b = rng.uniform(float(im0.get()),float(im1.get()))
        c = complex(a,b)
        re.delete(0, len(re.get()))
        re.insert(0, str(a))
        im.delete(0, len(im.get()))
        im.insert(0, str(b))
    
    elif r.get()==2:
        k = float(rad.get())
        a = rng.uniform(float(pre.get())-k,float(pre.get())+k)
        b = rng.uniform(float(pim.get())-k, float(pim.get())+k)
        c = complex(a,b)
        re.delete(0, len(re.get()))
        re.insert(0, str(a))
        im.delete(0, len(im.get()))
        im.insert(0, str(b))

    centerr = float(centerre.get())
    centeri = float(centerim.get())
    zo = float(zoom.get().split('x')[0])
    xmin, xmax, ymin, ymax = -2/zo, 2/zo, -1.5/zo, 1.5/zo
    pixels = pixval.get().split('x')
    width = int(pixels[0])
    height = int(pixels[1])
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    max_iter = 100
    jset = np.zeros((height, width))
    
    for i in range(height):
        for j in range(width):
            z = complex(x[j]+centerr, y[i]+centeri)
            jset[i][j] = julia(z, max_iter)

    if cmaval.get() == 'random':
        cm = colors[rng.randint(0,len(colors)-1)]
    else:
        cm = cmaval.get()

    plt.imshow(jset, cmap=cm)
    plt.title(str(c))
    plt.xlabel(cm)
    plt.show()

def Down():
    plt.imsave(f"Jset(c={c})(cmap={cm})(zoom={zo})(center={centerr}+{centeri}i)(reso={pixval.get()}).png", jset, cmap = cm)

def FindCenter():
    centerre.delete(0, len(centerre.get()))
    centerim.delete(0, len(centerim.get()))
    centerre.insert(0, str(x[int(RePixel.get())]))    
    centerim.insert(0, str(y[int(ImPixel.get())]))

#Buttons
goodc = tk.Button(window, text='Good C', command = findc)
findcent = tk.Button(window, text='Find Center', command=FindCenter)


#Creating Entries
lab1 = tk.Label(window, text="Re(c)")
re = tk.Entry(window, width=20, justify='left')
lab2 = tk.Label(window, text="Im(c)")
im = tk.Entry(window, width=20, justify='left')
lab3 = tk.Label(window, text="Re Lower lim:")
re0 = tk.Entry(window, width=5, justify='center')
lab4 = tk.Label(window, text="Re Upper lim:")
re1 = tk.Entry(window, width=5, justify='center')
lab5 = tk.Label(window, text="Im Lower lim:")
im0 = tk.Entry(window, width=5, justify='center')
lab6 = tk.Label(window, text="Im Upper lim:")
im1 = tk.Entry(window, width=5, justify='center')
lab7 = tk.Label(window, text="Re:")
pre = tk.Entry(window, width=20, justify = 'left')
lab8 = tk.Label(window, text='Im:')
pim = tk.Entry(window, width=20, justify = 'left')
lab9 = tk.Label(window, text='Radius')
rad = tk.Entry(window, width=20, justify= 'left')
lab10 = tk.Label(window, text='Zoom:')
zoom = tk.Entry(window, width=5, justify = 'center')
cset = tk.Label(window, text='')
lab11 = tk.Label(window, text = 'Re(Center):')
centerre = tk.Entry(window, width=20, justify= 'left')
lab12 = tk.Label(window, text = 'Im(Center):')
centerim = tk.Entry(window, width=20, justify= 'left')
lab13 = tk.Label(window, text = 'Center:')
lab14 = tk.Label(window, text='RePixel:')
RePixel = tk.Entry(window, width=5, justify='center')
lab15 = tk.Label(window, text='ImPixel:')
ImPixel = tk.Entry(window, width=5, justify='center')

re0.insert(0,'-2.0')
re1.insert(0,'2.0')
im0.insert(0,'-1.5')
im1.insert(0,'1.5')
zoom.insert(0, '1x')
centerre.insert(0,'0')
centerim.insert(0,'0')


#Creating Options
pixval = tk.StringVar()
pix = tk.OptionMenu(window, pixval ,'400x300','534x400','667x500','1334x1000','2668x2000')
pixval.set('400x300')

cmaval = tk.StringVar()
cma = tk.OptionMenu(window, cmaval, 'random', 'afmhot','afmhot_r','Blues','Blues_r','bone','bone_r','BrBG','BrBG_r','BuGn','BuGn_r','BuPu','BuPu_r','cividis','cividis_r','CMRmap','CMRmap_r','cool','cool_r','coolwarm','coolwarm_r','copper','copper_r','cubehelix','cubehelix_r','flag','gist_earth','gist_earth_r','gist_heat','gist_heat_r',
            'gist_ncar_r','gist_stern','gnuplot','gnuplot2','hot','inferno','inferno_r','jet_r','magma','magma_r','nipy_spectral','nipy_spectral_r',
            'ocean','pink','PRGn','PRGn_r','PuRd','PuRd_r','RdBu','RdBu_r','RdGy','RdGy_r','RdPu_r','twilight','twilight_r','twilight_shifted','twilight_shifted_r')
cmaval.set('random')



#Creating RadioButtons
r = tk.IntVar()
opt1 = tk.Radiobutton(window, text="Re(c)+Im(c)", variable=r, value=0)
opt2 = tk.Radiobutton(window, text="Random Range", variable=r, value=1)
opt3 = tk.Radiobutton(window, text="Around point", variable=r, value=2)




#PLacing Objects (2 IN AN COMMAND)
opt1.grid(row=0, column=0, sticky='nsew')
re.grid(row=1, column=1, sticky='nsew')
lab1.grid(row=1, column=0, sticky='nsew')
im.grid(row=2,column=1, sticky='nsew')
lab2.grid(row=2, column=0, sticky='nsew')
opt2.grid(row=3, column=0, sticky='nsew')
lab3.grid(row=4, column=0, sticky='nsew')
re0.grid(row=4, column=1, sticky='nsew')
lab4.grid(row=5, column=0, sticky='nsew')
re1.grid(row=5, column=1, sticky='nsew')
lab5.grid(row=6, column=0, sticky='nsew')
im0.grid(row=6, column=1, sticky='nsew')
lab6.grid(row=7, column=0, sticky='nsew')
im1.grid(row=7, column=1, sticky='nsew')
opt3.grid(row=8, column=0, sticky='nsew')
lab7.grid(row=9, column=0, sticky='nsew')
pre.grid(row=9, column=1, sticky='nsew')
lab8.grid(row=10, column=0, sticky='nsew')
pim.grid(row=10, column=1, sticky='nsew')
lab9.grid(row=11, column=0, sticky='nsew')
rad.grid(row=11, column=1, sticky='nsew')
lab10.grid(row=12, column=0, sticky='nsew')
zoom.grid(row=12, column=1, sticky='nsew')
lab13.grid(row=13, column=0, sticky='nsew')
findcent.grid(row=13, column=1, sticky='nsew')
lab14.grid(row=14, column=0, sticky='nsew')
RePixel.grid(row=14, column=1, sticky='nsew')
lab15.grid(row=15, column=0, sticky='nsew')
ImPixel.grid(row=15, column=1, sticky='nsew')
lab11.grid(row=16, column=0, sticky='nsew')
centerre.grid(row=16, column=1, sticky='nsew')
lab12.grid(row=17, column=0, sticky='nsew')
centerim.grid(row=17, column=1, sticky='nsew')
goodc.grid(row=18, column=0, sticky='nsew')
cset.grid(row=18, column=1, sticky='nsew')
pix.grid(row=19,column=0, sticky='nsew')
cma.grid(row=20,column=0, sticky='nsew')


gen = tk.Button(window, text='Generate!', command=Generate)
gen.grid(row=19, column=1, sticky='nsew')
down = tk.Button(window, text="Download", command=Down)
down.grid(row=20, column=1, sticky='nsew')

for i in range(21):
    tk.Grid.rowconfigure(window, i, weight=1)
for i in range(2):
    tk.Grid.columnconfigure(window, i, weight=1)
window.mainloop()
