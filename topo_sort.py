#tring to find most close seller to you from your contacts and frinends contacts
#breadth first search
from collections import deque
graph={}
visited=[]
def topo(name):
    visited.append(name)
    for child in graph[name]:
       if not child in visited:
           topo(child)
    print(name)
if __name__ == '__main__':
    
    graph["eat"]=["brush"]
    graph["brush"]=["wake"]
    graph["shower"]=["wake"]
    graph["play"]=["eat","shower"]
    graph["wake"]=[]
    topo("play")
    
    #graph representation
    '''
    eat=>brush=>wake<=shower<=play=>eat
    
    '''
