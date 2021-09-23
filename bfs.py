#tring to find most close seller to you from your contacts and frinends contacts
#tring to find most close seller to you from your contacts and frinends contacts
from collections import deque
graph={}

def person_is_seller(person):
    if person:
        return person[1]
    else:
        return False

def search(name):
    search_queue=deque()
    search_queue+=graph[name]
    searched=[]
    while search_queue:
        person=search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f"{person[0]} is a seller!")
                return True
            else:
                if person:
                    search_queue+=graph[person]
                    searched.append(person)
    print("not found")
    return False


if __name__ == '__main__':
    graph[("you",False)]=[("ali",False),("ahmed",False)]
    graph[("ali",False)]=[("Amr",False)]
    graph[("Amr",False)]=[("said",True)]
    graph[("ahmed",False)]=[()]
    graph[("said",True)]=[()]
    search(("you",False))
