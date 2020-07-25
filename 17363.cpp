#include <iostream>
using namespace std;

int N,M;
char pic[101][101]={};
int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> N >> M;
  for(int i=0; i<N; i++) cin >> pic[i];
  
  for(int i=0; i<N; i++){
    for(int j=0; j<M; j++){
      if(pic[i][j] == '-') pic[i][j] = '|';
      else if(pic[i][j] == '|') pic[i][j] = '-';
      else if(pic[i][j] == '/') pic[i][j] = '\\';
      else if(pic[i][j] == '\\') pic[i][j] = '/';
      else if(pic[i][j] == '^') pic[i][j] = '<';
      else if(pic[i][j] == '<') pic[i][j] = 'v';
      else if(pic[i][j] == 'v') pic[i][j] = '>';
      else if(pic[i][j] == '>') pic[i][j] = '^';
    }
  }
  for(int i=M-1; i>=0; i--){
    for(int j=0; j<N; j++) cout << pic[j][i];
    cout << "\n";
  }
}