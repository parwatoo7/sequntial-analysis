#sequential analysis

class SA:
    def __init__(self):
        "Sequential Analysis"
        self.l = [{"i":0,"v": "","t": []}]
        self.p = None # previous nueron
        self.c = self.l[0] # the current nueron
        
    def an(self, v):
        self.l.append({"i":len(self.l),"v": v,"t": []})
    def gn(self, v):
        for i in self.l:
            if i["v"] == v:
                return i

    def at(self, p, c):
        p["t"].insert(0,{"i":c,"w":1})

    def gt(self, p, c):
        for t in p["t"]:
            if t["i"] == c:
                return t

    def iw(self, t):
        t["w"] += 1

    def ns(self, t, ts):
        "neoteric sort"
        ts.remove(t)
        ts.insert(0,t)


    def IN(self, v):
        _ = self
        n = _.gn(v)
        if n == None:
            _.an(v)
            _.p = _.c
            _.c = _.gn(v)
            _.at(_.p,_.c["i"])
        else:
            _.p = _.c
            _.c = n
            t = _.gt(_.p, _.c["i"])
            if t == None:
                _.at(_.p,_.c["i"])
            elif t != None:
                _.iw(t)
                _.ns(t, _.p["t"])
        
        return _.p,_.c
        
        
sa = SA()

data = "abcabcabc"

for i in data:
    sa.IN(i)

print(sa.l)

# output 
"""
[
    {
        'i': 0, 
        'v': '', 
        't': [
            {'i': 1, 'w': 1}
        ]
    }, 
    {
        'i': 1, 
        'v': 'a', # static value
        't': [
            {
                'i': 2, # index of a correlated value
                'w': 3 # the weight, representing the number of times correlated
            } # [a,b] happend 3 times
        ]
    }, 
    {
        'i': 2,
        'v': 'b', 
        't': [
            {'i': 3, 'w': 3} # [b,c]
        ]
    }, 
    {
        'i': 3, 
        'v': 'c', 
        't': [
            {'i': 1, 'w': 2}
        ]
    }
]
"""
