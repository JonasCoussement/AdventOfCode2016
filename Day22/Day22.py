import re
import matplotlib.pyplot as plt

class node:
    
    def __init__(self, xid, yid, avail, used,listid):
        self.xid = xid
        self.yid = yid
        self.avail = avail
        self.used = used
        self.viable_pairs = []
        self.total = avail+used
        self.listid = listid

    def add_new_viable_pair(self,pair):
        self.viable_pairs.append(pair) 

    def __len__(self):
         return len(self.viable_pairs)

    def get_id(self):
        return self.xid, self.yid
        
def get_input():
    nodes_raw = open("Day22.txt").readlines()
    node_list = []
    max_x, max_y = 0,0
    listid = 0
    for i in range(2,len(nodes_raw)):
        xindex = nodes_raw[i].index("x")
        yindex = nodes_raw[i].index("y")
        xid = int(nodes_raw[i][xindex+1:xindex+nodes_raw[i][xindex:].index("-")])
        yid = int(nodes_raw[i][yindex+1:yindex+nodes_raw[i][yindex:].index(" ")])
        if xid > max_x:
            max_x = xid
        if yid > max_y:
            max_y = yid
        usage = re.findall("[0-9]+T",nodes_raw[i])
        used = int(usage[1][0:-1])
        avail = int(usage[2][0:-1])
        new_node = node(xid,yid,avail,used,listid)
        listid+=1
        node_list.append(new_node)
    return node_list, max_x, max_y

def add_viable_pairs(node_list):
    total_pairs = 0
    for i in range(0,len(node_list)):
        used = node_list[i].used
        if used > 0:
            for j in range(0,len(node_list)):
                avail = node_list[j].avail
                if used <= avail and i != j:
                    #print node_list[i].get_id(), node_list[j].get_id()
                    node_list[i].add_new_viable_pair(node_list[j].get_id())
            total_pairs += len(node_list[i])
    print "The total number of viable pairs in the grid amounts to ", total_pairs

def main():
    node_list, gridx, gridy = get_input()
    add_viable_pairs(node_list)
    for x in node_list:
        if x.used < 250 and x.used >0:
            plt.plot(x.xid,x.yid,'ro')
        elif x.used > 250:
            plt.plot(x.xid,x.yid,'rx')
        else:
            plt.plot(x.xid,x.yid,'_')
    plt.show()
    
main()
