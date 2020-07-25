#include <iostream>
#include <cstdio>

using namespace std;


int main(void){
  int n;
  scanf("%d",&n);

  n = (n-1) % 8;

  if(n == 0) printf("1\n");
  else if(n == 1 || n == 7) printf("2\n");
  else if(n == 2 || n == 6) printf("3\n");
  else if(n == 3 || n == 5) printf("4\n");
  else printf("5\n");
  return 0;
}
