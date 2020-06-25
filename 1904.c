#include <stdio.h>

int main(){
    int n;
    scanf("%d",&n);
    int arr[1000001]= {0};
    arr[1] = 1;
    arr[2] = 2;
    for(int i=3;i<n+1;i++){
        arr[i] = (arr[i-1]+arr[i-2])%15746;
    }
    printf("%d",arr[n]);
}