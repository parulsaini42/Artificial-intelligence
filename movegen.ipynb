c=0

def moveGen(matrix,list_open,s):
    state=[]
    #representing row major in 3D form using list comprehension
    n=3
    temp_matrix= [matrix[i * n:(i + 1) * n] for i in range((len(matrix) + n - 1) // n )] 
    
    #find a blank space
    for i in range(3):
        for j in range(3):
             if temp_matrix[i][j]==0:
                    a=i
                    b=j
                    break
    
    
    if a-1>=0:   
        temp_matrix[a][b]=temp_matrix[a-1][b]
        temp_matrix[a-1][b]=0
        k=0
        array=[0 for i in range(9)]
        for i in range(3):
            for j in range(3):
                array[k]=temp_matrix[i][j]
                k=k+1
        if array not in list_open:
            list_open.append(array[:])
            parent.append(s)
        temp_matrix= [matrix[i * n:(i + 1) * n] for i in range((len(matrix) + n - 1) // n )] 
    
    if b-1>=0:   
        temp_matrix[a][b]=temp_matrix[a][b-1]
        temp_matrix[a][b-1]=0
        k=0
        array=[0 for i in range(9)]
        for i in range(3):
            for j in range(3):
                array[k]=temp_matrix[i][j]
                k=k+1
        if array not in list_open:
            list_open.append(array[:])
            parent.append(s)
        temp_matrix= [matrix[i * n:(i + 1) * n] for i in range((len(matrix) + n - 1) // n )] 
        
    if b+1<=2:   
        temp_matrix[a][b]=temp_matrix[a][b+1]
        temp_matrix[a][b+1]=0
        k=0
        array=[0 for i in range(9)]
        for i in range(3):
            for j in range(3):
                array[k]=temp_matrix[i][j]
                k=k+1
        if array not in list_open:
            list_open.append(array[:])
            parent.append(s)
        temp_matrix= [matrix[i * n:(i + 1) * n] for i in range((len(matrix) + n - 1) // n )]
    
    if a+1<=2:
        temp_matrix[a][b]=temp_matrix[a+1][b]
        temp_matrix[a+1][b]=0
        k=0
        array=[0 for i in range(9)]
        for i in range(3):
            for j in range(3):
                array[k]=temp_matrix[i][j]
                k=k+1
        if array not in list_open:
            list_open.append(array[:])
            parent.append(s)
        temp_matrix= [matrix[i * n:(i + 1) * n] for i in range((len(matrix) + n - 1) // n )] 
    return

def print_mat(list_open,par):
    n=3
    t_mat= [list_open[par][i * n:(i + 1) * n] for i in range((len(list_open[par]) + n - 1) // n )] 
    k=0
    for i in range(3):
        print(str(t_mat[i][k])+" "+str(t_mat[i][k+1])+" "+str(t_mat[i][k+2]))
        
    
    
list_open=[]
s=0
#original input state
m="0,1,3,4,2,5,7,8,6"
r=m.split(',')
matrix=list(map(int,r))
#goal state
g=[1,2,3,4,5,6,7,8,0]
#dont copy by reference
list_open.append(matrix[:])
#has index of corresponding matrix in list_open  
parent=[]
#parent of matrix in list_open is null
parent.append(-1)
while(1):
    if g in list_open:
        par_list=[]
        p=list_open.index(g)
        par_list.append(p)
        par=parent[p]
        while(par!=-1):
            par_list.append(par)
            par=parent[par]
    
        p=par_list.index(0)
        print(par_list[-1])
        while(p!=-1):
            print_mat(list_open,par_list[p])
            if(p==0):
                print('GOAL')
            else:
                print('next state')
            p=p-1
        break
        
    matrix=list_open[s]
    moveGen(matrix,list_open,s)
    s=s+1
