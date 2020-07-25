#include <iostream>
#include <cstdio>

using namespace std;

int map[100][100];
int dx[2][3] = {{0,-1,1}, {-1,0,1}};
int dy[2][3] = {{2,-1,-1}, {1,-2,1}};

int n;
int ans = 0;

void dfs(int x, int y, int bx, int by, int type, int cnt){
  map[x][y] = 1;

  if(cnt > n){
    map[x][y] = 0;
    return;
  }

  for(int i = 0 ; i < 3 ; i++){
    int nx = x + dx[type][i];
    int ny = y + dy[type][i];
    if(nx == bx && ny == by) continue;
    if(!map[nx][ny]){
      dfs(nx,ny,x,y,!type,cnt+1);
    }else if(map[nx][ny] && cnt == n){
      ans++;
    }
  }
  map[x][y] = 0;
  return;
}


int main(void){
  scanf("%d",&n);

  dfs(50, 50, 0, 0, 0, 0);
  printf("%d\n",ans/3);
  return 0;
}
