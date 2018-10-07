

def heuristic(matrix):
    #representing row major in 3D form using list comprehension
    n=3
    d_tiles=0
    t_mat= [matrix[i * n:(i + 1) * n] for i in range((len(matrix) + n - 1) // n )] 
    goal=[g[i * n:(i + 1) * n] for i in range((len(g) + n - 1) // n )] 
    k=0
    while k<=2: 
        for i in range(3):
            if t_mat[k][i]!=goal[k][i]:
                d_tiles=d_tiles+1
        k=k+1
    #i=list_open.index(matrix)
    return d_tiles
    
def moveGen(matrix,list_open,s):
    state=[]
    h=[]
    t=[]
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
        
        t.append(array)
        v=heuristic(array)
        h.insert(0,v)
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
       
        t.append(array)
        v=heuristic(array)
        h.insert(1,v)
      
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
        t.append(array)
        v=heuristic(array)
        h.insert(2,v)
       
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
        t.append(array)
        v=heuristic(array)
        h.insert(3,v)
        temp_matrix= [matrix[i * n:(i + 1) * n] for i in range((len(matrix) + n - 1) // n )] 
       
    #maintianing parent list
    for i in range(len(t)):
        parent.append(s)
        
    #sort t with respect to heuristics
    zipped_pairs = zip(h,t)
 
    z = [x for _, x in sorted(zipped_pairs)]
    #appened sorted nodes in pq
    for i in z:
        pq.append(i)
  
    return


def print_mat(closed,par):
    k=0
    for i in range(3):
        print(str(closed[par][k])+" "+str(closed[par][k+1])+" "+str(closed[par][k+2]))
        k=k+3

        

closed=[]
s=0
#original input state
m="0,1,3,4,2,5,7,8,6"
r=m.split(',')
matrix=list(map(int,r))
#goal state
g=[1,2,3,4,5,6,7,8,0]
#priority list
pq=[]
pq.append(matrix)
#has index of corresponding matrix in list_open  
parent=[]
#parent of matrix in list_open is null
parent.append(-1)
while(1):
    if g in pq:
        par_list=[]
        #calculating idex of goal fro a combination f closed and pq
        p=len(closed)+pq.index(g)
        par_list.append(p)
        par=parent[p]
        while(par!=-1):
            par_list.append(par)
            par=parent[par]
        p=par_list.index(0)
        while(p!=0):
            print_mat(closed,par_list[p])
            print('next state')
            p=p-1
        break
        
    matrix=pq.pop(0)
    closed.append(matrix)
    s=closed.index(matrix)
    moveGen(matrix,list_open,s)
 
 #seperately priting goal bcoz last element not popped out of pq
k=0
for i in range(3):
    print(str(g[k])+" "+str(g[k+1])+" "+str(g[k+2]))
    k=k+3
print('goal state')
