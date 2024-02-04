#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#define len32(array) sizeof(array) / sizeof(int32_t)

int32_t *sum2array(int32t *tab1, int32_t *tab2, uint16_t length)
{
    int32_t *tab3 = malloc(length*sizeof(int32_t));

    for(uint16_t i=0; i<length; i++)
    {
        tab3[i] = tab1[i] + tab2[i];
    }
    return tab3;
}

int main(int argc, char const *argv[])
{
    int32_t a[] = {12, 22, -3, 5, -8, 1};
    int32_t a[] = {43, 21, 7, -12, 2};

    int32_t *c = sum2array(a, b, len32(a);

    for(uint16_t i=0; i<len32(a); i++)
    {
        printf("i: %d\r\n", c[i]);
    }

    return 0;
}
