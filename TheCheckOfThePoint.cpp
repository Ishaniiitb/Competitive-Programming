// https://codeforces.com/problemset/problem/683/A

#include <iostream>

using namespace std;

int position(int a, int x, int y){
    int stat = 0;

    if (((x <= a) && (x >= 0) && ((y == 0) || (y == a))) || ((y <= a) && (y >= 0) && ((x == 0) || (x == a)))){
        stat = 1;
    }
    else if ((x < a) && (x > 0) && ((y > 0) && (y < a))){
        stat = 0;
    }
    else{
        stat = 2;
    }

    return stat;
}

int main(){
    int a = 0, x = 0, y = 0;
    scanf("%d %d %d", &a, &x, &y);

    printf("%d", position(a, x, y));
}
