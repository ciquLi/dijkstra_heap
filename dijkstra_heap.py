import time
import heapq

def dijkstra(G,start):     ###dijkstra算法
    INF = 999999999
    dis = dict((key,INF) for key in G)    # start到每个点的距离
    dis[start] = 0
    ###堆优化
    t1 = time.time()
    dis_un = {}    #未访问的点的距离
    pq = []    #存放排序后的值
    for node,d in dis.items():    #最小堆
        entry = [d,node]
        dis_un[node] = entry
        heapq.heappush(pq,entry)
    t2 = time.time()
    print('建立堆所用时间: ',t2-t1)
    
    t3 = time.time()
    path = dict((key,[start]) for key in G)    #记录到每个点的路径

    while len(pq)>0:
        v_dis,v = heapq.heappop(pq)    #未访问点中距离最小的点和对应的距离
        p = path[v].copy()    #到v的最短路径
        for node in G[v]:    #与v直接相连的点
            new_dis = dis[v] + float(G[v][node])
            if new_dis < dis[node]:    #如果与v直接相连的node通过v到src的距离小于dis中对应的node的值,则用小的值替换
                dis[node] = new_dis    #更新所有点的距离
                dis_un[node][0] = new_dis    #更新未访问的点到start的距离
                temp = p.copy()
                temp.append(node)    #更新node的路径
                path[node] = temp    #将新路径赋值给temp
    t4 = time.time()
    print('Dijkstra算法所用时间:',t4-t3)
    return dis,path
    


if __name__ == '__main__':
    
    G = {1:{1:0, 2:10, 4:30, 5:100},
         2:{2:0, 3:50},
         3:{3:0, 5:10},
         4:{3:20, 4:0, 5:60},
         5:{5:0},
         }
    distance,path = dijkstra(G,1)
