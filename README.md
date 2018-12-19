# dijkstra with heap
some algorithm write with python3.6

dijkstra_heap.py: 用堆优化的dijkstra算法  
1.返回到每个点最短路径的权重和路径  
2.图文件存为JSON，直接读取后转换成dict,用UJSON包，200M的图文件大概需要4秒  
3.处理百万个节点、千万条边，所需时间大概为10秒  
