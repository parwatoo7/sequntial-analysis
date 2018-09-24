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
            # attention - 1
            #_.l.append({"i":len(_.l),"v": v,"t": []})
            _.an(v)
            _.p = _.c
            _.c = _.gn(v)
            _.at(_.p,_.c["i"])
        else:
            # attention + 1
            _.p = _.c
            _.c = n
            t = _.gt(_.p, _.c["i"])
            if t == None:
                # attention - 2
                _.at(_.p,_.c["i"])
            elif t != None:
                # attention + 2
                _.iw(t)
                _.ns(t, _.p["t"])
        
        return _.p,_.c
        
        

