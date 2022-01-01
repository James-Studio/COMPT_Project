import graphviz

g = graphviz.Graph(format='png') 
# 1
g.node('A','user')
# 2
g.node('B','help')
# 3
g.node('C','Laptop')
g.node('D','Phone')
g.node('E','Desktop')
g.node('F','Tech_Information')
# 4 - 1
g.node('G','Apple_Laptop')
g.node('H','Asus_Laptop')
g.node('I','Msi_Laptop')
# 4 - 2
g.node('J','Apple_Phone')
g.node('K','Samsung')
g.node('L','Hwawei')
# 4 - 3
g.node('M','Apple_Desktop')
g.node('N','Asus_Desktop')
g.node('O','Msi_Desktop')
# 4 - 4
g.node('P','Youtuber')
g.node('Q','Report')
g.node('R','TED')
# annotate the edges
g.edges(['AB','BC','BD','BE','BF','CG','CH','CI','DJ','DK','DL','EM',
'EN','EO','FP','FQ','FR','CB','DB','EB','FB','GB','HB','IB','JB','KB','LB',
'MB','NB','OB','PB','QB','RB'])
# draw the edge 
# format : edge(tail_name, head_name, label=None, _attributes=None, **attrs)
g.edge('A','B',label="advance[is_going_to_help]")
g.edge('B','C',label="advance[is_going_to_laptop]")
g.edge('B','D',label="advance[is_going_to_phone]")
g.edge('B','E',label="advance[is_going_to_desktop]")
g.edge('B','F',label="advance[is_going_to_info]")
g.edge('C','G',label="advance[is_going_to_apple_laptop]")
g.edge('C','H',label="advance[is_going_to_asus_laptop]")
g.edge('C','I',label="advance[is_going_to_msi_laptop]")
g.edge('D','J',label="advance[is_going_to_apple_phone]")
g.edge('D','K',label="advance[is_going_to_samsung]")
g.edge('D','L',label="advance[is_going_to_hwawei]")
g.edge('E','M',label="advance[is_going_to_apple_desktop]")
g.edge('E','N',label="advance[is_going_to_asus_desktop]")
g.edge('E','O',label="advance[is_going_to_msi_desktop]")
g.edge('F','P',label="advance[is_going_to_youtuber]")
g.edge('F','Q',label="advance[is_going_to_report]")
g.edge('F','R',label="advance[is_going_to_ted]")
# go back
g.edge('C','B',label="go_back")
g.edge('D','B',label="go_back")
g.edge('E','B',label="go_back")
g.edge('F','B',label="go_back")
g.edge('G','B',label="go_back")
g.edge('H','B',label="go_back")
g.edge('I','B',label="go_back")
g.edge('J','B',label="go_back")
g.edge('K','B',label="go_back")
g.edge('L','B',label="go_back")
g.edge('M','B',label="go_back")
g.edge('N','B',label="go_back")
g.edge('O','B',label="go_back")
g.edge('P','B',label="go_back,advance")
g.edge('Q','B',label="go_back,advance")
g.edge('R','B',label="go_back,advance")

# save

g.render(directory='doctest-output', view=True)