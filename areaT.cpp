#include <iostream>

using namespace std;

int main(){
    cout << "base: " << endl;
    int base;
    cin >> base;
    cout << "altura: " << endl;
    int altura;
    cin >> altura;
    int area = base*altura/2;
    cout << "area del triangulo: " << endl;
    cout << area << endl;
    return 0;
}