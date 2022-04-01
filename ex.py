class ex1:
    def __init__(self,list1,list2):
        self.list1=list1
        self.list2=list2
    def make_ex1(self,list1,list2):
        list3=[]
        for i in range (0,len(list1)):
            if i%2==0:
                list3.append(list1[i])
            else:
                list3.append(list2[i])
            print(list3[i])

class ex2:
    def __init__(self,list1):
        self.list1=list1
    def make_ex2(self,list1):
        index=list1[4]
        list1.pop(4)
        list1.insert(2,index)
        list1.append(index)
        print(list1)

class ex3:
    def __init__(self,list1):
        self.list1=list1
    def make_ex3(self,list1):
        index=int(len(list1)/3)
        list11=[]
        list12 = []
        list13 = []
        for i in range(0,index):
            list11.append(list1[i])
            list12.append(list1[i+index])
            list13.append(list1[i+2*(index)])
        list11.reverse()
        list12.reverse()
        list13.reverse()
        print(list11)
        print(list12)
        print(list13)

class ex4:
    def __init__(self,list1):
        self.list1=list1
    def make_ex4(self,list1):
        dict={}
        for i in range(0,len(list1)):
            dict[list[i]]=list1.count(list1[i])
        print(dict)

class ex6:
    def __init__(self,set1,set2):
        self.set1=set1
        self.set2=set2
    def make_ex6(self,set1,set2):

        set1=set1-set(set1&set2)


        print(set1)

class ex7:
    def __init__(self,set1,set2):
        self.set1=set1
        self.set2=set2
    def make_ex7(self,set1,set2):
        cmp=set(set1&set2)
        if len(set1^cmp)==0:
            set1.clear()
        print(set1)

class ex8:
    def __init__(self,list1,set1):
        self.list1=list1
        self.set1=set1
    def make_ex8(self,list1,set1):
        to_rem=[]
        for i in range(0,len(list1)):
            if list1[i] in set1.values():
                to_rem.append(list1[i])

        list1=list(set(list1)-set(to_rem))
        print(list1)

class ex9:
    def __init__(self,set1):
        self.set1=set1
    def make_ex9(self,set1):
        list1=[]
        for i in range(0,len(set1)):
            list1.append(list(set1.values())[i])
        list1=list(set(list1))
        print(list1)

class ex10:
        def __init__(self, list1):
            self.list1 = list1
        def make_ex10(self,list1):
            list1=list(set(list1))
            list1=tuple(list1)
            print(min(list1)," ",max(list1))