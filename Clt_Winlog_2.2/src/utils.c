#include <windows.h>
#include <stdio.h>
#include <time.h>   // time(), localtime(), struct tm, clock_t


void nEraser(char* chaine)
{
    size_t i = 0;

    for(i = 0; i < strlen(chaine) + 1; i++)
        if(chaine[i] == '\n')
            chaine[i] = '\0';
}

void wait_time_end(float total_time)
{
    clock_t end_of_record = clock() + ((clock_t)total_time * CLOCKS_PER_SEC);
    while(clock() < end_of_record);

    return;
}
