import random
import matplotlib.pyplot as plt
import pandas as pd


#100번 마다 확률을 저장하는 리스트
#100, 200, 300, 400, 500... 100000
prob = []
idx = []
for i in range(100, 100001, 100):
    count = 0
    for i in range(i):
        if random.randint(1,3) == 1:
            count = count + 1
    prob.append(count/i*100)
    idx.append(i)
    
df1 = pd.DataFrame(prob,index=idx,columns='1')



# def res_pre(listall):
#     res1 = listall[0]
#     res2 = listall[1]
#     res3 = listall[2]
    
#     data = [1,2,3]
#     i = 1000
#     a1 = 0
#     a2 = 0
#     a3 = 0
#     for i in range(i):
#         a = random.choice(data)
#         if a == 1:
#             a1 = a1 + 1
#         elif a == 2:
#             a2= a2 + 1
#         elif a == 3:
#             a3= a3 +1 
            
#     res1.append(a1/i*100)
#     res2.append(a2/i*100)
#     res3.append(a3/i*100)
#     listall = [res1, res2, res3]
#     return listall


# res1 = []
# res2 = []
# res3 = []

# listall = [res1, res2, res3]
# for a in range(100):
#     listall = res_pre(listall)
    
# print(listall)

# x = range(100) 
# plt.plot(x,listall[0], x,listall[1], x,listall[2])
# plt.grid(True)
# plt.legend(['1', '2', '3'])
# plt.title('Saving a figure')
# plt.show()
