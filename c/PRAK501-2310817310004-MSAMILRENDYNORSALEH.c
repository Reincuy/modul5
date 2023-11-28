#include <stdio.h>

int MaxBilangan(int a, int b, int c, int d) {
    int max1 = (a > b) ? a : b;
    int max2 = (c > d) ? c : d;
    return (max1 > max2) ? max1 : max2;
}    

int main() {
        int a, b, c, d;
        scanf("%d %d %d %d", &a, &b, &c, &d);
        int hasil = MaxBilangan(a, b, c, d);
        printf("%d", hasil);
        return 0;
}