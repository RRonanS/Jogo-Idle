import PySimpleGUI as sg
graph_layout=[[sg.Graph(enable_events=True,key='graph',graph_top_right=(0,0),graph_bottom_left=(100,100),canvas_size=(500,400))]]
window=sg.Window('',graph_layout,return_keyboard_events=True,finalize=True)
graph=window['graph']
casas=30
a=b=0
c=d=2
linha=0
while casas>0:
    casas-=1
    linha+=1
    graph.draw_rectangle((a, b), (c, d), line_color='black', fill_color='green', line_width=1)
    a+=2
    c+=2
    if linha==10 or linha==20:
        b+=2
        d+=2
'''cons=10
while cons>0:
    cons-=1
    graph.draw_rectangle((0, 0), (2, 2), line_color='black', fill_color='green', line_width=1)
    d=0
    num=0
    for c in range(0,400,2):
        x=2
        v=0
        while True:
            if x > 500: break
            graph.draw_rectangle((v,d), (x,c), line_color='black', fill_color='green', line_width=1)
            x+=2
            v+=2
            d+=2
            num+=1
    print(num)'''



while True:
    event,values = window.read()
    if event==None:break

window.close()