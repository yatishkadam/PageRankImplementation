import math

d=0.85
outlinks={}
inlinks={}
NewPageRank={}
Pagerank={}
content_list = []

#get info from the document
def length(file):
    with open(file) as f:
        for i, l in enumerate(f):
            pass
    f.close()
    return i + 1
def get_inlinks(file_name):
    N= length(file_name)
    f = open(file_name, "r+")
    line = f.readlines()
    for i in line[0:N]:
        content = str(i).strip()
        content_list = content.split()
        inlinks[content_list[0]] = list(set(content_list[1:]))
    f.close()
get_inlinks("G1.txt")

def get_outlinks():
    #creating a dictionary of outlinks from a node
    for key in inlinks.iterkeys():
        outlinks.update({key:[]})
    for key,val in inlinks.iteritems():
        for x in val:
            if str(x) in inlinks:
                outlinks[x].append(key)
get_outlinks()

#P represnts the set of pages
#P is of type list'''
P=inlinks.keys()
Plen=len(P)
# L gives the number of outlinks a page has
# is of type dict
L={}
#funtion to get the number of outgoing links for a page
#takes in a dict
#gives a dict
for x in P:
    inlinks_list = inlinks[x]
    for word in inlinks_list:
        if word in L:
            L[word] += 1
        else:
            L[word] = 1
# S represents the set of pages which have no outlinks
# S is of type list
S = []
S= (list(set(inlinks.keys()) - set(L.keys())))
print "sink pages", len(S)
# function calculate PageRank
def PageRank():
    counter=0
    perplexity=0
    for k in P:
        Pagerank[k]=(1.0/Plen)
    while counter < 4 :
        print perplexity
        prev_perplexity = perplexity
        sinkPR=0
        #calculate the sink for each page
        #loops for each page in dic and assigns
        for p in S:
            sinkPR=sinkPR+Pagerank[p]
        for p in P:
            NewPageRank[p]=(1-d)/Plen
            NewPageRank[p]+=d*sinkPR/Plen
            #pagerank of the page P +    (d        *    sinkvalue of p  /    number of links in P)
            try:
                for x in inlinks[p]:
                    NewPageRank[p]+= d * Pagerank[x]/(L[x])
            except:
                pass
                #pagerank of the page p +   ( d    *       pagerank of each link pointing to p / number of links pointing to p
        for p in P:
            Pagerank[p]=NewPageRank[p]


        #calculate perplexity
        H_PR = 0
        for i in P:
            H_PR += Pagerank[i] * math.log(float(Pagerank[i]), 2)

        perplexity = math.pow(2, -H_PR)
        if abs(prev_perplexity - perplexity) < 1  :
            counter +=1
        else:
            counter=0

#print pages according to their rank
def print_pages_ranked():
    page_rank = sorted((list(set(Pagerank.values()))), reverse=True)

    f=open("PageRankG1.txt",'w+')
    for x in page_rank[0:50]:
        for k, v in Pagerank.iteritems():
            if x == v:
                f.write(str(k)+' '+ str(x)+'\n')

    f.close()


#main function which calls the required functions in a sequence
def mainfunc():
    PageRank()
    print_pages_ranked()

mainfunc()

