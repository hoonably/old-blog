---
layout: blog
title: "네트워크 플로우 (Network-Flow)"
subtitle: ""
date: 2024-07-26 01:40:00 +09:00
categories: Algorithm
author: "hoonably"
# meta: "Springfield"
---

## 💡 네트워크 플로우?


네트워크 플로우 문제는 주어진 유량 네트워크에서 소스(source)에서 싱크(sink)로 보낼 수 있는 **최대 유량**을 찾는 문제다.

네트워크는 노드(node)와 간선(edge)으로 구성된 그래프로 표현되며, 각 간선은 용량(capacity)을 가진다.



## 💡 용어


​	•	**노드(Node)**: 그래프에서 유량이 흐르는 지점.

​	•	**간선(Edge)**: 두 노드를 연결하는 선으로, 유량이 흐르는 통로. 각 간선은 용량(capacity)이라는 최대 유량을 가진다.

​	•	**소스(Source)**: 유량이 시작되는 지점.

​	•	**싱크(Sink)**: 유량이 도착하는 지점.

​	•	**잔여 용량(Residual Capacity)**: 현재 유량을 고려했을 때 간선이 추가로 유량을 보낼 수 있는 여유.

## 💡 네트워크 플로우 기본 문제


<img width="972" alt="image" src="https://github.com/user-attachments/assets/197b77bc-b255-4694-a4de-37edb5d57fa3">



## 💡 포드-풀커슨 알고리즘 (Ford-Fulkerson Algorithm)


​	•	**방식**: 가능한 경로를 반복적으로 찾아 유량을 보내며, 더 이상 유량을 보낼 수 없을 때까지 반복

​	•	**시간 복잡도**: `O((V+E)F)` - 여기서 V는 노드 수, E는 간선 수, F는 최대 유량

```c++
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int INF = 0x3f3f3f3f;  // 1061109567
// const ll INF = 0x3f3f3f3f3f3f3f3f;

/*--
네트워크 플로우

포드-풀커슨
O((V+E)F)
V: 노드 수, E: 간선 수, F: 최대 유량
*/

const int vertexSZ = 1000;  // in out 분할이라면 2배
const int SZ = vertexSZ+5, bias = vertexSZ/2;
int SRC = vertexSZ+1, SINK = vertexSZ+2;

struct FordFulkerson {
    using FlowType = int;

    vector<int> graph[SZ];
    FlowType capacity[SZ][SZ], flow[SZ][SZ];
    bool visited[SZ];

    void addEdge(int _from, int _to, FlowType _cap, FlowType _caprev = 0) {
        graph[_from].push_back(_to);
        graph[_to].push_back(_from);
        capacity[_from][_to] += _cap;
        capacity[_to][_from] += _caprev;
    }

    bool DFS(int now, int T, FlowType& minFlow) {
        if (now == T) return true;
        visited[now] = true;
        for (int next : graph[now]) {
            if (!visited[next] && capacity[now][next] > flow[now][next]) {
                FlowType residual = capacity[now][next] - flow[now][next];
                if (DFS(next, T, minFlow)) {
                    minFlow = min(minFlow, residual);
                    flow[now][next] += minFlow;
                    flow[next][now] -= minFlow;
                    return true;
                }
            }
        }
        return false;
    }
    FlowType maxFlow(int S = SRC, int T = SINK) {
        memset(flow, 0, sizeof(flow));
        FlowType totalFlow = 0;
        FlowType minFlow;
        while (true) {
            memset(visited, false, sizeof(visited));
            minFlow = INF;
            if (!DFS(S, T, minFlow)) break;
            totalFlow += minFlow;
        }
        return totalFlow;
    }

    void initGraph() { // 테스트케이스를 위한 그래프 초기화
        for (int i = 0; i < SZ; i++) graph[i].clear();
        memset(capacity, 0, sizeof(capacity));
        memset(flow, 0, sizeof(flow));
    }
}nf;
```



## 💡 디닉 알고리즘 (Dinic’s Algorithm)


디닉 알고리즘은 포드-풀커슨 알고리즘의 개선된 버전으로,

**레벨 그래프(Level Graph)**를 사용하여 **블로킹 플로우(Blocking Flow)**를 반복적으로 찾는 알고리즘이다.

​	•	**기본 개념**: **BFS**를 사용하여 레벨 그래프를 만들고, **DFS**를 사용하여 블로킹 플로우를 찾음

​	•	**시간 복잡도**: `O(V^2 * E)`



이 방법 외에 다음에는 Edge 구조체를 사용하는 방법을 알려줄건데, 구조체가 더 빠르다.

하지만, 배열을 이용하는 방법이 편할 때가 있다.

[백준 숫자판 만들기](https://www.acmicpc.net/problem/2365) 문제처럼, setCap함수를 사용하여 Cap을 이분탐색으로 찾아주는 문제가 있다.

이 외에도, 개별 flow를 출력해야 한다면 구조체 사용보다 용이하다.

```c++
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int INF = 0x3f3f3f3f;  // 1061109567
// const ll INF = 0x3f3f3f3f3f3f3f3f;

/*--
네트워크 플로우

디닉 알고리즘 O(V^2E)

flow와 cap을 따로 관리하기 때문에 Edge 구조체 사용보다 느림.

But, 나중에 개별 flow를 출력해야한다면 용이
ex) 숫자판 만들기 https://www.acmicpc.net/problem/2365
*/

const int vertexSZ = 1000;  // in out 분할이라면 2배
const int SZ = vertexSZ+5, bias = vertexSZ/2;
int SRC = vertexSZ+1, SINK = vertexSZ+2;

struct NetworkFlow{  // use Dinic

	using FlowType = int;

	FlowType flow[SZ][SZ], capacity[SZ][SZ];
	vector<int> graph[SZ];

	// 마지막 인자를 안쓰면 유방향, cap과 같게 쓰면 무방향(양쪽 cap 같음)
	void addEdge(int from, int to, int cap, int caprev = 0) {
		graph[from].emplace_back(to);
		graph[to].emplace_back(from);
		capacity[from][to] += cap;
		capacity[to][from] += caprev;
	}

	int level[SZ], work[SZ];
	bool BFS(int S, int T){
		memset(level, 0, sizeof(level));
		queue<int> q; q.push(S); level[S] = 1;
		while(!q.empty()){
			int now = q.front(); q.pop();
			for(int &next : graph[now]){
				if(!level[next] && capacity[now][next]-flow[now][next]>0) {
					q.push(next), level[next] = level[now] + 1;
				}
			}
		}
		return level[T];
	}
	FlowType DFS(int now, int T, FlowType f){
		if(now == T) return f;
		for(; work[now] < (int)graph[now].size(); work[now]++){
			int next = graph[now][work[now]];
			if(level[next] != level[now] + 1 || capacity[now][next]-flow[now][next]==0) continue;
			FlowType ret = DFS(next, T, min(f, capacity[now][next]-flow[now][next]));
			if(!ret) continue;
			flow[now][next]+=ret;
			flow[next][now]-=ret;
			return ret;
		}
		return 0;
	}
	FlowType maxFlow(int S = SRC, int T = SINK){
		memset(flow, 0, sizeof(flow));
		FlowType ret = 0, minFlow;
		while(BFS(S, T)){
			memset(work, 0, sizeof(work));
			while((minFlow = DFS(S, T, INF))) ret += minFlow;
		}
		return ret;
	}

	void init(){  // for Test Case
		memset(capacity, 0, sizeof(capacity));
		for(int i=0; i<SZ; i++) graph[i].clear();
	}

	// 중간 연결 cap를 모두 Mid로 설정하고 이분탐색으로 찾기 위해서 c로 변경시켜주는 함수
	// SRC와 SINK와의 연결은 건드리지 않는게 포인트
	void setCap(int N, int c){
		for (int i=1; i<=N; i++)
			for (int j=1; j<=N; j++)
				capacity[i][j+bias]=c;
	}

	// Flow를 출력
	void printFlow(int N){
		for (int i=1; i<=N; i++){
			for (int j=1; j<=N; j++){
				cout << flow[i][j+bias] << ' ';
			}
			cout << '\n';
		}		
	}
}nf;
```





## 💡 디닉 알고리즘 (Dinic’s Algorithm) 구조체 사용


위의 디닉 알고리즘보다 더 빠른 방식이 바로 Edge 구조체를 사용하는 방식이다.

**Edge 구조**: 두 번째 코드에서는 Edge 구조체를 사용하여 각 간선을 저장

각 간선은 목적지 **노드 (to)**, **역간선의 인덱스 (rev)**,  **용량 (cap)**을 포함한다.

이전 방식의 **capacity**와 **flow**를 별도로 업데이트하는 것보다 효율적이다.

이는 특히 많은 간선을 다루는 경우 성능 향상을 가져올 수 있다.

```c++
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int INF = 0x3f3f3f3f;  // 1061109567
// const ll INF = 0x3f3f3f3f3f3f3f3f;

/*--
네트워크 플로우

디닉 알고리즘 O(V^2*E)

Edge 구조체 사용으로 매우 빠름

단, cap에 현재 flow를 직접 저장하기 때문에, 실시간으로 바뀌어서
flow를 수정하면서 문제를 푸는 문제에서는 일일이 수정해줘야 해서 불편
*/

const int vertexSZ = 1000;  // in out 분할이라면 2배
const int SZ = vertexSZ+5, bias = vertexSZ/2;
int SRC = vertexSZ+1, SINK = vertexSZ+2;

struct NetworkFlow{  // use Dinic

    using FlowType = int;

    struct Edge{ int to, rev; FlowType cap; };
    vector<Edge> graph[SZ];
    int level[SZ], work[SZ];

    // 마지막 인자를 안쓰면 유방향, cap과 같게 쓰면 무방향(양쪽 cap 같음)
    void addEdge(int _from, int _to, FlowType _cap, FlowType _caprev = 0){
        graph[_from].push_back({_to, (int)graph[_to].size(), _cap});
        graph[_to].push_back({_from, (int)graph[_from].size()-1, _caprev});
    }

    void initGraph(){ // for Test Case
        for (int i=0; i<SZ; i++) graph[i].clear();
    }

    bool BFS(int S, int T){  // make level graph
        memset(level, 0, sizeof(level));
        queue<int> q; q.push(S); level[S] = 1;
        while(!q.empty()){
            int now = q.front(); q.pop();
            for(const auto &next : graph[now]){
                if(!level[next.to] && next.cap) q.push(next.to), level[next.to] = level[now] + 1;
            }
        }
        return level[T];
    }
    FlowType DFS(int now, int T, FlowType flow){  // find Blocking Flow
        if(now == T) return flow;
        for(; work[now] < (int)graph[now].size(); work[now]++){
            auto &next = graph[now][work[now]];
            if(level[next.to] != level[now] + 1 || !next.cap) continue;
            FlowType ret = DFS(next.to, T, min(flow, next.cap));
            if(!ret) continue;
            next.cap -= ret;
            graph[next.to][next.rev].cap += ret;
            return ret;
        }
        return 0;
    }
    FlowType maxFlow(int S = SRC, int T = SINK){
        FlowType ret = 0, minFlow;
        while(BFS(S, T)){
            memset(work, 0, sizeof(work));
            while((minFlow = DFS(S, T, INF))) ret += minFlow;
        }
        return ret;
    }
} nf;

```





## 💡 풀어볼 문제들


- [도시 왕복하기 1](https://www.acmicpc.net/problem/17412)  : 기본 Network Flow 문제

- [열혈강호 4](https://www.acmicpc.net/problem/11378) : Brunch 생성 후 이어주기

- [도시 왕복하기 2](https://www.acmicpc.net/problem/2316) : in, out 정점 분할

- [격자 0 만들기](https://www.acmicpc.net/problem/11495) : 간선 양이 매우 많아 Dinic 알고리즘이 100배 빠름



## 💡 네트워크 플로우의 활용 예시


​	•	**물류**: 특정 지점에서 다른 지점으로 물건을 최대한 많이 보내는 문제

​	•	**통신망**: 네트워크의 대역폭을 최대한 활용하여 데이터를 전송하는 문제

​	•	**전력망**: 발전소에서 도시로 전력을 최대한 효율적으로 보내는 문제







