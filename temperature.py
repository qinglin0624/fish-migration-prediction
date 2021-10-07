from tkinter import *


def make_disp_grid(canvas, rows, cols):    
    cell_width = int(canvas.cget('width')) / cols
    cell_height = int(canvas.cget('height')) / rows    
    disp_grid = [['' for col in range(cols)] for row in range(rows)]
    for row in range(rows):
        for col in range(cols):
            x1 = col * cell_width
            y1 = row * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height            
            if int(data2[row][col])==-1000:
                disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#87CEFA',outline='#F0FFFF')
            elif int(data2[row][col])==32768:
                disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='black',outline='#363636')
            elif int(data2[row][col])>=21:
                disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#8B0000',outline='#CD2626')
            elif 21>int(data2[row][col])>=18:
                disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#8B1A1A',outline='#CD2626')
            elif 18>int(data2[row][col])>=15:
                disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#CD2626',outline='#EE2C2C')
            elif 15>int(data2[row][col])>=12:
                disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#FF3030',outline='#FF7F50')
            elif 12>int(data2[row][col])>=9:
                disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#FF4500',outline='#FFDAB9')
            elif 9>int(data2[row][col])>=6:
                disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#FFA07A',outline='#FFEFDB')
            elif 6>int(data2[row][col])>=3:
                disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#FFE4B5',outline='#FFFAFA')
            elif 3>int(data2[row][col])>0:
                disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#FFFFF0',outline='#FFFFF0')
            elif int(data2[row][col])<=0:
                disp_grid[row][col] = canvas.create_rectangle(x1,y1,x2,y2,fill='#F0FFFF',outline='#BFEFFF') 

    return disp_grid

if __name__=='__main__':
    
    Year = open('2020.txt', 'r')
    store=Year

    data = []
    rowth=0
    for line in store:
        rowth+=1
        if rowth!=1: 
            line.strip('\n')
            change=line.replace('-32768',' 32768')
            row=change.split()
            data.append(row)
    Year.close()

    data1=[]
    for i in range(0,50):
        c=[]
        for j in range(120,195):
            #c.append(data[i][j])
            c.append(int(data[i][j]))
        data1.append(c)
        #data1.append(c)
    data2=[]
    year=2070
    for i in range(0,50):
        c=[]
        for j in range(0,75):
            if data1[i][j]==32768 or data1[i][j]==-1000:
                T=data1[i][j]
                c.append(T)
                c.append(T)
                continue
            delta_T=0.000000000040393*year**4-0.000000154772254*year**3+0.000146765566744*year**2+0.002578002667371*year+0.000005206079179- 0.907903496194830
            T=delta_T+data1[i][j]/100
            c.append(T)
            c.append(T)
        data2.append(c)
        data2.append(c)
    
    
    window = Tk()
    window.title('Map')
    f = Frame(window)
    f.pack()
    canvas = Canvas(f, bg='gray', width=750, height=500,bd=0.1)
    canvas.pack()
    
    make_disp_grid(canvas, 100, 150)    
    window.mainloop()