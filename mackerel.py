from tkinter import *
from PIL import Image
import numpy as np
from time import sleep


def temperature(year,h):           
    if h=='m':
        delta_T=0.000000000040393*year**4-0.000000154772254*year**3+0.000146765566744*year**2+0.002578002667371*year+0.000005206079179- 0.907903496194830
    if h=='l':
        delta_T=0.000000000003363*year**4-0.000000007835048*year**3+0.000001363526822*year**2+0.001755275153093*year+0.000003547457095- 0.527997611431180
    if h=='u':
        delta_T=0.000000000077423*year**4-0.000000301709461*year**3+0.000292167606182*year**2+0.003400730473337*year+0.000006864701920- 1.287809380911568
    tem=[]
    for i in range(100):  
        d=[]
        for j in range(150):
            T=data1[i][j]
            if T==-1000 or T==32768:
                d.append(T)
            else:
                T_change=T/100+delta_T
                d.append(T_change)
        tem.append(d)
    return tem

def update(grid,year,h):
    temp_grid=temperature(year,h)    
    rows = len(grid)
    cols = len(grid[0])
    new_grid=grid.copy()
    for row in range(rows):
        for col in range(cols):
            if grid[row][col]>0:

                row1,col1=choose_best(row,col,temp_grid)
                if grid[row1][col1]<0:
                    continue
                elif row!=row1 or col!=col1:

                    new_grid[row][col]-=1
                    new_grid[row1][col1]+=1                
                            
    for col in range(cols):
        for row in range(rows):
            grid[row][col] = new_grid[row][col]
    
def tem_cond(t):    
    if t==-1000 or t==32768:
        return -99999
    
    f=(1/(2.5*np.sqrt(2*np.pi)))*np.exp(-np.square(t-10.2)/(2*2.5*2.5))    
      
    return 6.25*f

def choose_best(r,c,temp_grid):
    best_r=[r]
    best_c=[c]    
    best_t=tem_cond(temp_grid[r][c])
    for i in [r-1,r,r+1]:
        for j in [c-1,c,c+1]:
            if tem_cond(temp_grid[i][j])>best_t:
                best_t=tem_cond(temp_grid[i][j])
                best_r.clear()
                best_c.clear()
                best_r.append(i)
                best_c.append(j)
#                 best_r,best_c=i,j
            elif tem_cond(temp_grid[i][j])==best_t:
                best_r.append(i)
                best_c.append(j)
#             else:
#                 continue
    n=np.random.randint(len(best_r))
    return [best_r[n],best_c[n]]
#     return [best_r,best_c]
         
                
def make_disp_grid(canvas,fishMap):
    rows = len(fishMap)
    cols = len(fishMap[0])
    cell_width = int(canvas.cget('width')) / cols
    cell_height = int(canvas.cget('height')) / rows

    disp_grid = [['' for col in range(cols)] for row in range(rows)]
    for row in range(rows):
        for col in range(cols):
            x1 = col * cell_width
            y1 = row * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height
            
            w=0.01
            c='#0072e0'
            if int(fishMap[row][col])==-1:
                disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='white',width=w,outline='white')
            elif int(fishMap[row][col])==-2:
                disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='black',width=w,outline='#363636')
            elif int(fishMap[row][col])==0:
                disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#0072e0',width=w,outline=c)
#                 disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#008999',width=w,outline=c)
            elif int(fishMap[row][col])==1:
                disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#FFD700',width=w,outline=c)
#                 disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#FFBBFF',width=w,outline=c)
#                 disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#999079',width=w,outline=c)
            elif int(fishMap[row][col])==2:
                disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#FFA500',width=w,outline=c)
#                 disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#FF83FA',width=w,outline=c)
#                 disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#996079',width=w,outline=c)
            elif int(fishMap[row][col])==3:
                disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#FF8C00',width=w,outline=c)
#                 disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#FF00FF',width=w,outline=c)
#                 disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#993079',width=w,outline=c)
            elif int(fishMap[row][col])==4:
                disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#D2691E',width=w,outline=c) 
#                 disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#C71585',width=w,outline=c) 
#                 disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#990079',width=w,outline=c) 
            elif int(fishMap[row][col])==5:
                disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#A0522D',width=w,outline=c) 
#                 disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#B03060',width=w,outline=c) 
#                 disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#790089',width=w,outline=c) 
            elif int(fishMap[row][col])>5:
                disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#B22222',width=w,outline=c)
#                 disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#8B008B',width=w,outline=c) 
#                 disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#590089',width=w,outline=c) 

    return disp_grid 

def display(canvas, Map, disp_grid):
    
#     for row in range(len(grid)):
#         for col in range(len(grid[0])):
#             color = 'green'
#             if grid[row][col] == '-':
#                 color = 'black'
#             canvas.itemconfig(disp_grid[row][col], fill=color)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            w=0.01
            c='#0072e0'
            if int(Map[row][col])==0:
                canvas.itemconfig(disp_grid[row][col],fill='#0072e0',width=w,outline=c)
#                 canvas.itemconfig(disp_grid[row][col],fill='#008999',width=w,outline=c)
            elif int(Map[row][col])==1:
                canvas.itemconfig(disp_grid[row][col],fill='#FFD700',width=w,outline=c)
#                 canvas.itemconfig(disp_grid[row][col],fill='#FFBBFF',width=w,outline=c)
#                 canvas.itemconfig(disp_grid[row][col],fill='#999079',width=w,outline=c)
            elif int(Map[row][col])==2:
                canvas.itemconfig(disp_grid[row][col],fill='#FFA500',width=w,outline=c)
#                 canvas.itemconfig(disp_grid[row][col],fill='#FF83FA',width=w,outline=c)
#                 canvas.itemconfig(disp_grid[row][col],fill='#996079',width=w,outline=c)
            elif int(Map[row][col])==3:
                canvas.itemconfig(disp_grid[row][col],fill='#FF8C00',width=w,outline=c)
#                 canvas.itemconfig(disp_grid[row][col],fill='#FF00FF',width=w,outline=c)
#                 canvas.itemconfig(disp_grid[row][col],fill='#993079',width=w,outline=c)
            elif int(Map[row][col])==4:
                canvas.itemconfig(disp_grid[row][col],fill='#D2691E',width=w,outline=c) 
#                 canvas.itemconfig(disp_grid[row][col],fill='#C71585',width=w,outline=c) 
#                 canvas.itemconfig(disp_grid[row][col],fill='#990079',width=w,outline=c)
            elif int(Map[row][col])==5:
                canvas.itemconfig(disp_grid[row][col],fill='#A0522D',width=w,outline=c) 
#                 canvas.itemconfig(disp_grid[row][col],fill='#B03060',width=w,outline=c)
#                 canvas.itemconfig(disp_grid[row][col],fill='#790089',width=w,outline=c) 
            elif int(Map[row][col])>5:
                canvas.itemconfig(disp_grid[row][col],fill='#B22222',width=w,outline=c) 
#                 canvas.itemconfig(disp_grid[row][col],fill='#8B008B',width=w,outline=c)
#                 canvas.itemconfig(disp_grid[row][col],fill='#590089',width=w,outline=c) 
    
    canvas.update()

    
def populate(leftTop,RightBottom):
    width=RightBottom[1]-leftTop[1]
    height=RightBottom[0]-leftTop[0]
    mean=((leftTop[0]+RightBottom[0])/2,(leftTop[1]+RightBottom[1])/2)
    
    for r in range(leftTop[0],RightBottom[0]):
        for c in range(leftTop[1],RightBottom[1]):
            if fishMap[r][c]==0:
                count=1
                if abs(c-mean[1])<width/3 and abs(r-mean[0])<height/3:
                    count+=1
                if abs(c-mean[1])<width/6 and abs(r-mean[0])<height/6:
                    count+=1
                fishMap[r][c]=count

                
                
                
                
                
if __name__ == '__main__':            
                
    Year = open('2020.txt', 'r')
    store=Year

    data0 = []
    rowth=0
    for line in store:
        rowth+=1
        if rowth!=1: 
            line.strip('\n')
            change=line.replace('-32768',' 32768')
            row=change.split()
            data0.append(row)
    Year.close()

    data1=[]
    for i in range(0,50):
        c=[]
        for j in range(120,195):
            c.append(int(data0[i][j]))
            c.append(int(data0[i][j]))
        data1.append(c)
        data1.append(c)

    fishMap=disp_grid = [[0 for col in range(150)] for row in range(100)]
    for r in range(len(data1)):
        for c in range(len(data1[0])):
            if int(data1[r][c])==-1000:
                fishMap[r][c]=-1
            elif int(data1[r][c])==32768:
                fishMap[r][c]=-2

    populate((58,100),(67,110))
    populate((64,112),(66,114))
    populate((66,114),(68,116))
    populate((70,118),(72,120))
    populate((72,120),(74,122))
    # populate((64,105),(78,128))


    window = Tk()
    window.title('Map')

    f = Frame(window)
    f.pack()

    canvas = Canvas(f, bg='white', width=750, height=500,bd=0.1)
    canvas.pack()

    year=0
    total_year=50
    grid=fishMap.copy()
    dg=make_disp_grid(canvas,grid)
    while year<=30:

        display(canvas,grid,dg)
        sleep(0.1)
        update(grid,year+2020,'m')
        # ‘m’: mean value, 'l': lower 95% value, 'u': upper 95% value
        year=year+1
        oval1 = canvas.create_oval(530,300,570,340,outline='#DDA0DD',width=1.5)
        oval2 = canvas.create_oval(530,325,570,365,outline='#DDA0DD',width=1.5)
        oval3 = canvas.create_oval(500,260,660,420,outline='#DDA0DD',width=1.5)
        print(year)
    canvas.mainloop()    