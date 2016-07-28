#include <iostream>

int main(){
    int x;
    
    std::cin >> x;
    
    for(int i = x; i <=x+12; i++){
            if(i%2 != 0)
                   std::cout << i << "\n";
                   
                   
    
    }
    return 0;
}