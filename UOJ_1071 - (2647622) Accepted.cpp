#include <iostream>
using namespace std;


int main(){
    int x, y, aux;
    int s = 0;

    cin >> x;
    cin >> y;

    if(x > y){
         aux = x;
         x = y;
         y = aux;
    }

    for(int i = x+1; i < y; i++){
            if(i%2 != 0){
                   s+= i;
            }
    }

    cout << s << "\n";
    return 0;
}
