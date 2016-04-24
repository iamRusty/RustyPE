#include <stdio.h>

void numberStore(int counter, int num[][20], FILE *in);
void printNum(int num[][20]);
int main(void) {
    int number[20][20];
    
    FILE *fp;
    fp = fopen("data.pe", "r");
    
    int count;
    for (count = 0; count< 20; count++)
        numberStore(count, number, fp);
    
    printNum(number);    
    fclose(fp);
    return 0;
}

void numberStore(int counter, int num[][20], FILE *in) {

}

void printNum(int num[][20]) {
    int count3, count4;
    for (count3 = 0; count3 < 20; count3++) {
        for (count4 = 0; count4 < 20; count4++)
            printf("%i ", num[count3][count4]);
        printf("\n");
    }
}