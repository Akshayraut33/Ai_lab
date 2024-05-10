

def dfs(arr,s):
    visted1[s]=1
    print(s," ")
    for i in arr[s]:
         if(visted1[i]==0):
             dfs(arr,i)

def bfs(arr,s):
     q=[]
     q.append(s)
     visited2[s]=1
     while len(q)!=0:
         pe=q.pop(0)
         print(pe)
         for i in arr[pe]:
             if(visited2[i]==0):
                 visited2[i]=1;
                 q.append(i)

arr={
    0:[1,2],
    1:[0,3],
    2:[0,4,5],
    3:[1],
    4:[2],
    5:[2],
}
visted1=[0]*len(arr)
visited2=[0]*len(arr)
print("the Bfs of given Grap is ")
bfs(arr,0)
print("the Dfs of given Grap is ")
dfs(arr,0)






