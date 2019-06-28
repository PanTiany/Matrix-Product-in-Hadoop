import random
txt_file = open('Matrix_try.txt', 'w')


def each_matrix(name,txt_file):
    for i in range(1,2001):
        for j in range(1,2001):
            tmp = random.random()    
            if(tmp > 0.9):
                line =[name,'\t', str(i),'\t', str(j),'\t',str(random.randint(0,100)),'\n'] 
                print(line)
                txt_file.writelines(line)

            else:
                pass

each_matrix('A', txt_file)

each_matrix('B', txt_file)

txt_file.close()
