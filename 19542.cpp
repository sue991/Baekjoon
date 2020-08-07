#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#define pb push_back

using namespace std;

int n,s,d;
int leaf_lev = 0;
int level[100001], child[100001], dist[100001];
vector<vector<int> > vec(100001);

int dfs(int node, int lev){
  for(int i = 0 ; i < vec[node].size() ; i++){
    int next = vec[node][i];
    if(level[next] == -1){
      level[next] = lev + 1;
      leaf_lev = max(leaf_lev,lev+1);
      child[node] = max(child[node], dfs(next,lev+1));
    }
  }
  return child[node] + 1;
}

int main(void){
  scanf("%d %d %d",&n,&s,&d);

  for(int i = 1 ; i < n ; i++){
    int u,v;
    scanf("%d %d",&u,&v);
    vec[u].pb(v);
    vec[v].pb(u);
  }

  memset(level,-1,sizeof(level));
  memset(dist,-1,sizeof(dist));
  memset(child,0,sizeof(child));

  level[s] = 0;
  dfs(s,0);

  int ans = 0;

  for(int i = 1 ; i <= n ; i++){
    if(i == s) continue;
    if(child[i] >= d) ans++;
  }
  printf("%d\n",2 * ans);
  return 0;
}
