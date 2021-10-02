#include <iostream>
#include <cassert>

int sumNPerfectCubes(int n) {

    int sum = 0;
    for(int i = 0; i <= n; i++) {
        sum += i*i*i;
    }
    return sum;

}

int main() {

    std::cout << sumNPerfectCubes(10) << "\n"; // 3025
    return 0;

}

