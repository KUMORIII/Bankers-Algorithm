from ntpath import join
from turtle import clear
from django.shortcuts import render
import random
from information.models import *
import datetime
import json

# Create your views here.

def check(finish):
    for f in finish:
        if not f:
            return False
    return True

def SaveCheck(users):
    finish = [False]*len(users)
    #print(finish)
    work = []
    need = []
    allocation =[]
    for res in Resource.objects.all():
        work.append(res.available_num)
    #users = Process.objects.all()
    #for i in range(user_id):
    for u in users:
        n_vector = []
        allo_vector = []
        for res in Resource.objects.all():
            n = Need.objects.get(pro=u, res=res)
            n_vector.append(n.need_num)
            allo = Allocation.objects.get(pro=u, res=res)
            allo_vector.append(allo.allo_num)
        need.append(n_vector)
        allocation.append(allo_vector)
    while True:
        if check(finish):
            return True
        flag = False
        for i in range(len(users)):
            if finish[i]:
                continue
            cnt = 0
            for j in range(0, 3):
                if need[i][j] <= work[j]:
                    cnt += 1
            if cnt == 3:
                for j in range(0, 3):
                    work[j] += allocation[i][j]
                finish[i]=True
                flag = True
        if not flag:
            return False

def init(request):
    Need.objects.all().delete()
    Allocation.objects.all().delete()
    Max.objects.all().delete()
    res_list = []
    u_list = []
    max_matrix = []
    allo_matrix = []
    need_matrix = []
    # 初始化资源
    for res in Resource.objects.all():
        upper_limmit = random.randint(1, 50)
        res.total_num = upper_limmit
        res.available_num = res.total_num
        res.save()
    # 生成进程

    # 初始化最大需求矩阵和需求矩阵
    for u in Process.objects.all():
        max_vector = []
        u_list.append(u)
        for res in Resource.objects.all():
            max_num = random.randint(1, max(1,int(res.total_num / 2)))
            max_vector.append(max_num)
            need_num = max_num
            m = Max(pro=u, res = res, max_num = max_num)
            n = Need(pro=u, res=res, need_num = need_num)
            m.save()
            n.save()
        max_matrix.append(max_vector)
    # 随机生成分配矩阵，同时进行安全性检查
    idx = 1
    user_id = 0
    users = Process.objects.all()
    user_list = []
    while user_id < 3:
        if user_id == 0:
            u = Process.objects.get(pro_name='P1')
        elif user_id == 1:
            u = Process.objects.get(pro_name='P2')
        elif user_id == 2:
            u = Process.objects.get(pro_name="P3")
        #print(u.pro_name)
        user_list.append(u)
    #for u in Process.objects.all():
        allo_vector = []
        need_vector = []
        for res in Resource.objects.all():
            #time_left = datetime.time(0, random.randint(0,59), random.randint(0,59))
            maxx = Max.objects.get(pro = u, res = res)
            maxn = int(maxx.max_num)
            maxn = max(0, int(maxn))
            maxn = min(maxn, res.available_num)
            allo_num = random.randint(0, maxn)
            if res.available_num == 0:
                allo_num = 0
            if allo_num > 0:
                hour_left = str(random.randint(0, 23))
                min_left = str(random.randint(0, 59))
                sec_left = str(random.randint(1, 59))
            else:
                hour_left, min_left, sec_left = 0, 0, 0
            #time_matrix.append(time_left)
            allo = Allocation(res = res, pro = u, allo_num = allo_num, hour=hour_left, minute=min_left, second=sec_left, idx=idx)
            allo.save()
            idx += 1
            allo_vector.append(allo)
        if user_id > 0:
            flag = SaveCheck(user_list)
            if not flag:
                allos = Allocation.objects.filter(pro=u)
                for allo in allos:
                    allo.delete()
                    idx -= 1
                user_list.pop()
                continue
        user_id += 1
        for res in Resource.objects.all():
            n = Need.objects.get(pro=u, res=res)
            allo = Allocation.objects.get(pro=u, res=res)
            n.need_num -= allo.allo_num
            n.save()
            res.available_num -= allo.allo_num
            res.save()
            need_vector.append(n.need_num)
                
        allo_matrix.append(allo_vector)
        need_matrix.append(need_vector)
    for res in Resource.objects.all():
        res_list.append(res)
    matrix = zip(u_list, max_matrix, allo_matrix, need_matrix)
    with open('./test.txt', 'w') as f:
        f.write(f'{res_list}\n')
        f.write(f'{matrix}\n')
    return render(request, 'mainpage/mainpage.html', {'res_list':res_list, 'matrix':matrix, 'allocation':allo_matrix})

def calculate(request):
    global order
    finish = [False, False, False]
    work = []
    need = []
    allocation = []

    for res in Resource.objects.all():
        work.append(res.available_num)
    for u in Process.objects.all():
        n_vector = []
        allo_vector = []
        for res in Resource.objects.all():
            n = Need.objects.get(pro=u, res=res)
            n_vector.append(n.need_num)
            allo = Allocation.objects.get(pro=u, res=res)
            allo_vector.append(allo.allo_num)
        need.append(n_vector)
        allocation.append(allo_vector)
    order = []
    with open('test.txt', 'w+') as f:
        f.seek(0)
        f.truncate() 
    dfs(0, finish, work, need, allocation)
    answer=[]
    raw_answer = []
    with open('test.txt', 'r') as f:
        orders=f.readlines()
    for order in orders:
        #print(order)
        order = order.replace('\n', '')
        order = order.split(' ')
        order = list(order)
        order.pop()
        flag = True
        for o in order:
            if flag:
                a = o
                flag = False
            else:
                a = a + '→' + o
        answer.append(order)
        raw_answer.append(a)
    #print(f'answer: {answer}')
    final_answer=efficiency_sort(answer)
    print(f'raw:{raw_answer}')
    print(f'final:{final_answer}')
    result = zip(raw_answer, final_answer)
    return render(request, 'mainpage/TimeOutAlert.html', {'result': result})
    
def dfs(layer, finish, work, need, allocation):
    global order
    if layer == 3:
        order_str = "".join(order)
        with open('test.txt', 'a') as f:
            f.write(f'{order_str}\n')
        return
    for i in range(0, 3):
        #print(i)
        if finish[i] == False:
            flag = True
            for j in range(0, 3):
                if need[i][j] > work[j]:
                    flag = False
                    break
            if flag:
                for j in range(0, 3):
                    work[j] += allocation[i][j]
                finish[i]=True
                if i== 0:
                    order.append('P1 ')
                elif i==1:
                    order.append('P2 ')
                elif i==2:
                    order.append('P3 ')
                dfs(layer+1, finish, work, need, allocation)
                order.pop()
                for j in range(0, 3):
                    work[j] -= allocation[i][j]
                finish[i]=False

def back(request):
    res_list = []
    u_list = []
    max_matrix = []
    allo_matrix = []
    need_matrix = []
    for res in Resource.objects.all():
        res_list.append(res)
    for u in Process.objects.all():
        u_list.append(u)
        max_vector = []
        allo_vector = []
        need_vector = []
        for res in Resource.objects.all():
            m = Max.objects.get(pro=u, res=res)
            allo = Allocation.objects.get(pro=u, res=res)
            need = Need.objects.get(pro=u, res=res)
            max_vector.append(m.max_num)
            allo_vector.append(allo)
            need_vector.append(need.need_num)
        max_matrix.append(max_vector)
        allo_matrix.append(allo_vector)
        need_matrix.append(need_vector)
    matrix = zip(u_list, max_matrix, allo_matrix, need_matrix)
    return render(request, 'mainpage/mainpage.html', {'res_list': res_list, 'matrix': matrix, 'allocation': allo_matrix})

def efficiency_sort(answer):
    weight = []
    final_answer=[]
    sort_answer = []
    for order in answer:
        wait_time = 0
        w_turn_time = 0
        for pro_name in order:
            #print(pro_name)
            pro = Process.objects.get(pro_name=pro_name)
            allocation = Allocation.objects.filter(pro=pro)
            service_time = 0
            for allo in allocation:
                service_time = max(service_time, int(allo.hour)*3600+int(allo.minute)*60+int(allo.second))
            wait_time = wait_time + service_time
            w_turn_time += wait_time / (service_time+ 1e-9)
        score = w_turn_time / 3
        weight.append(score)
    weight = sorted(range(len(weight)), key=lambda k: weight[k])
    for i in range(len(weight)):
        sort_answer.append(answer[weight[i]])
    for answers in sort_answer:
        flag = True
        for answer in answers:
            if flag:
                s = answer
                flag = False
            else:
                s = s + '→' + answer
        final_answer.append(s)
    return final_answer

def recycle(request, pro_id, res_id):
    pro = Process.objects.get(pro_id=pro_id)
    res = Resource.objects.get(res_id=res_id)
    allo = Allocation.objects.get(pro=pro, res=res)
    res.available_num += allo.allo_num
    back(request)