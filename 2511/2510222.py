class Link:
    def __init__(self,first,rest=None):
        self.first = first
        self.rest = rest
        assert isinstance(rest,Link) or rest == None

    def print_link(self):
        map_link(print,self)

    

def range_link(end,start=0):
    if start >= end:
        return None
    else:
        return (Link(start, range_link(end,start+1)))
    
def map_link(f,link):
    if link.rest == None:
        return Link(f(link.first))
    else:
        return Link(f(link.first),map_link(f,link.rest))
    

def link_add(s,link):
    #add s to link at an approprite place
    judge = lambda x : s==x 
    if map_link(judge,link):
        link.rest = Link(s,link.rest)
        return link
    else:
        print(f'cannot add {s} to {link}' )

#map_link(lambda x: x**2,range_link(8)).print_link()

b = range_link(9,3)
link_add(7,b).print_link()




    
