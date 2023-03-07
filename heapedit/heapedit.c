#include <stdio.h>

int main(int argc, char *argv[])
{
    FILE *flag_ptr;
    char flag[64];
    void *ptrr;
    char *random_string;
    void *ptr;
    void *ptr2;
    int counter;
    int value;
    char c;

    flag_ptr = fopen ("flag.txt", "r");
    fgets(flag, 0x40, flag_ptr);
    random_string = "this is a random string."; // copy the string to stack 
    value = 0;
    counter = 0;
    while (counter < 7)
    {
        ptr = malloc(128);
        if (ptr2 == NULL)
            ptr2 = ptr;
        ptr = "Congrats! Your flag is: "; // copy the string to heap 
        strcat(ptr, flag);
        counter += 1;
    }
    ptrr = malloc(128);
    ptrr = "Sorry! This won't help you: "; // copy the string to heap
    strcat(ptrr, random_string);
    free(ptr);
    free(ptrr);
    value = 0;
    c = 0;
    puts("You may edit one byte in the program.");
    printf("Address: ");
    scanf("%d", &value);
    printf("Value: ");
    scanf("%c", &c);
    ptr2 + value = c;
    another_ptr = malloc(128);
    puts(another_ptr + 0x10);
    return (0);
}