import tkinter
def score(x,y):

    if(x=='-' and y!='-') or (x!='-' and y=='-'):
        #Return i-2 for each element of the first row and first col
        return -2
    elif(x==y=='-'):
        #First case in 0
        return 0
    elif(x==y):
        #Match
        return +2
    else:
        #Mistmatch
        return -1

def zeros(ls,lt):
    tab = []    #Initialise an empty tab
    for i in range(ls):
        tab.append([])  #2D Tab
        for j in range(lt):
            tab[i].append(0)    #Put Zeros everywhere
    return tab



#sim = zeros(len(row)+1,len(col)+1)
#print(sim)

def similarity(s,t):
    g = tkinter.Tk()

    sim = zeros(len(s)+1,len(t)+1)
    retrace_table = zeros(len(s)+1,len(t)+1)
    seq1 = ' '
    seq2 = ' '
    max_score = 0


    for i in range(1, len(s)+1):    #len(sim) instead of len(s)+1??
        sim[i][0] = sim[i-1][0] +score(s[i-1],'-')

        cases= tkinter.Label(g,text=sim[i][0])
        cases.grid(row=i,column=0)

        retrace_table[i][0] = 3

    for j in range(1, len(t)+1):
        sim[0][j] = sim[0][j-1] + score(t[j-1],'-')

        cases = tkinter.Label(g, text=sim[0][j])
        cases.grid(row=0, column=j)

        retrace_table[0][j] = 3

    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            match_mis = sim[i-1][j-1] + score(s[i-1],t[j-1])

            indel = sim[i-1][j]+score(s[i-1],'-')

            delete = sim[i][j-1]+score('-',t[j-1])

            sim[i][j] = max(match_mis,indel,delete)

            #cases = tkinter.Label(g, bg="red", text=sim[i][j])
            cases = tkinter.Label(g, text=sim[i][j])
            cases.grid(row=i, column=j)

            if(sim[i][j]==match_mis):
                retrace_table[i][j] = 1
            elif(sim[i][j]==indel):
                retrace_table[i][j] = 2
            elif(sim[i][j]==delete):
                retrace_table[i][j] = 3



    print(retrace_table[0])
    print(retrace_table[1])
    print(retrace_table[2])
    print(retrace_table[3])
    print(retrace_table[4])
    print(retrace_table[5])
    print(retrace_table[6])

    i,j = len(s),len(t)

    while i>0 or j>0:
        if(retrace_table[i][j] == 1):
            seq1 += s[i-1]
            seq2 += t[j-1]
            i -= 1
            j -= 1
        elif(retrace_table[i][j] == 2):
            seq1 += s[i - 1]
            seq2 += '-'
            i-=1
        elif(retrace_table[i][j] == 3):
            seq1 += '-'
            seq2 += t[j - 1]
            j -= 1

    print('Seq1 = ', end="")
    for i in reversed(seq1):
        print(i, end="")
    print('\n')
    print('Seq2 = ', end="")
    for i in reversed(seq2):
        print(i, end="")
    print('\n')

    g.mainloop()
    return sim


row = ['G','A','T','A','C','T']
col = ['C','A','A','G','A','C']


finalTab =similarity(row,col)
#print(finalTab)
print('Score = ',end="")
print(finalTab[len(row)][len(col)])
