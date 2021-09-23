#tring to find most close seller to you from your contacts and frinends contacts
from collections import deque
graph={}
graph["you"]=["ali","ahmed"]
graph["ali"]=["tom"]
graph["tom"]=[]
graph["ahmed"]=["emad","khaled"]
graph["khaled"]=[]
graph["emad"]=[]

def person_is_seller(person):
    return person[-1]=='i'

def search(name):
    search_queue=deque()
    search_queue+=graph[name]
    searched=[]
    while search_queue:
        person=search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f"{person} is a seller!")
                return True
            else:
                search_queue+=graph[person]
                searched.append(person)
    return False


if __name__ == '__main__':
    search("you")
