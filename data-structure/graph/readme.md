## graph 图
由 顶点的有穷非空集合和顶点之间的边的集合组成，通常表示为： G(V,E)，G表示一个图，V表示顶点的集合，E表示边的集合。

1. Vertex: 图中的元素称为顶点
1. 顶点的非空集合
1. 任意两点之间都会有关系，顶点之间的逻辑关系用边来表示，边集可以为空。

#### 各种概念
1. **Edge (无向边)**: 顶点V1 和　V2之间的边没有方向。用无序偶数对(V1, V2)表示
1. **Undirected Graph (无向图)**: 任意边都是无向边
1. **Arc (弧或有向边)**: V1 V2之间的边有方向。用<V1, V2>表示, V1是弧尾(Tail), V2是弧头(Head)
1. **Directed Graph (有向图)**: 任意边都是有向边
1. **简单图**: 没有到自身的边，也没有同一边重复出现
1. **无向完全图**: 任意顶点之间都存在边的无向图。　n个顶点有`n * (n-1) / 2`条边
1. **有向完全图**: 任意顶点之间都存在往返边的有向图。n个顶点有`n * (n-1)`条边
1. **稀疏图和稠密图**
1. **Weight (权)**: 与边或弧有关的数
1. **Network (网)**: 带权的图
1. **Subgraph (子图)**: G=(V, E), g = (v, e), v属于Ｖ子集, e属于E子集，则g是G子图
1. **Adjacent (邻接点)**: G = (V, {E}), (v1, v2) 属于 E, 则v1, v2互为邻接点
1. **incident**: 边(v1, v2) 依附(incident)于顶点v1, v2
1. **Degree (度)**: 顶点v的相关联的边的数目，记作 TD(v)
1. **InDegree (入度)**: 有向图的边<v1, v2>, v1邻接到v2, v2邻接自v1, 以v1为头的弧的数目称为v的入度 ID(v)
1. **OutDegree (出度)**: 以v为尾的弧的数目称为v的出度 OD(v), 则v的度为 `TD(v) = ID(v) + OD(v)`
1. **Path (路径)**: v1到v2的路径是一个顶点的有序列, 路径的长度等于弧的个数
1. **Cycle (回路或环)**: 除了第一个顶点或最后一个顶点重复外，其他点不重复称为简单环
1. **Connected Graph (连通图)**: 任意两顶点之间都有路径，都是连通的
1. **连通分量**: 无向图中极大连通子图
1. **强连通图**: 有向图中任意v1, v2都存在往返连接路径
1. **连通图的生成树**: 连接所有顶点，而且边为n-1
1. **有向树**: 只有一个入度为0, 其他入度均为1的有向图。一个有向图可以由若干有向树构成生成森林

### 图的抽象数据类型
```
ADT Graph
Data
    Vertexs, ArcOrEdge
Operation
    create_graph(v, vr)
    destory_graph(g)
    locate_vex(g, u) #返回u的位置
    get_vex(g, v)
    put_vex(g, v, value)
    first_adjvex(g, v) #返回v的邻接点
    next_adjvex(g, v, w) #返回下一个邻接点
    insert_vex(g, v)
    delete_vex(g, v)
    insert_arc(g, v, w)
    delete_arc(g, v, w)
    DFS_traverse(g) #深度优先遍历
    BFS_traverse(g) #广度优先遍历
```

### 图的存储结构
1. [Adjacency Matrix 邻接矩阵](https://github.com/sunhuachuang/algorithm-data-structure/blob/master/data-structure/graph/adjacency_matrix.py)
1. [Adjacency List 邻接表](https://github.com/sunhuachuang/algorithm-data-structure/blob/master/data-structure/graph/adjacency_list.py)
1. [Orthogonal List 十字链表](https://github.com/sunhuachuang/algorithm-data-structure/blob/master/data-structure/graph/orthogonal_list.py)
1. [Adjacency Multiple List 邻接多重表](https://github.com/sunhuachuang/algorithm-data-structure/blob/master/data-structure/graph/adjacency_multiple_list.py)
1. [Arc Array 边集数组](https://github.com/sunhuachuang/algorithm-data-structure/blob/master/data-structure/graph/arc_array.py)

### 图的遍历
#### 深度优先遍历
[Depth First Search](https://github.com/sunhuachuang/algorithm-data-structure/blob/master/data-structure/graph/depth_first_search.py)
#### 广度优先遍历
[Breadth First Search](https://github.com/sunhuachuang/algorithm-data-structure/blob/master/data-structure/graph/breadth_first_search.py)

### 最小生成树 Minimum Cost Spanning Tree
构造连通网的最小代价生成树称为最小生成树

1. [Prim 普里姆算法](https://github.com/sunhuachuang/algorithm-data-structure/blob/master/data-structure/graph/prim.py)
2. [Kruskal 克鲁斯卡尔算法](https://github.com/sunhuachuang/algorithm-data-structure/blob/master/data-structure/graph/kruskal.py)

### 最短路径
1. [Dijkstra 迪杰斯特拉算法](https://github.com/sunhuachuang/algorithm-data-structure/blob/master/data-structure/graph/dijkstra.py)
2. [Floyd 弗洛伊德算法](https://github.com/sunhuachuang/algorithm-data-structure/blob/master/data-structure/graph/floyd.py)
