#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int N,K;
string palin(string S){
    for(int i=0,j=N-1;i<=j;++i,--j){
        if(S[i]!=S[j]){
            if(K==0)
                return "";
            else{
                K--;
                S[i] = S[j] = max(S[i],S[j]);
            }
        }
    }
    return S;
}
string P,S;
int change(int i){
   return P[i]!=S[i]; 
}
int cost(int i,int j){
    if(i==j){
        return 1;
    }
    return 2-change(i)-change(j);
}
int main() {
    cin>>N>>K>>S;
    P = palin(S);
    if(P.size()==0){
        cout<<-1;
        return 0;
    }
    for(int i=0,j=N-1;i<=j;++i,--j){
        if(P[i]=='9')
            continue;
        if(cost(i,j) > K)
            continue;
        K -= cost(i,j);
        P[i] = P[j]  ='9';
    }
    cout<<P;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}