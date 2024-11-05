//解けてない

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>


int main() {
    char c[3000] = "MzAgMzEgMzAgMzAgMzAgMzAgMzEgMzEgMjAgMzAgMzEgMzAgMzEgMzEgMzAgMzAgMzEgMjAgMzAgMzEgMzAgMzAgMzAgMzAgMzEgMzAgMjAgMzAgMzEgMzAgMzAgMzEgMzEgMzEgMzEgMjAgMzAgMzEgMzAgMzEgMzAgMzAgMzEgMzAgMjAgMzAgMzEgMzAgMzAgMzAgMzEgMzEgMzEgMjAgMzAgMzEgMzEgMzEgMzEgMzAgMzEgMzEgMjAgMzAgMzEgMzEgMzEgMzAgMzEgMzAgMzAgMjAgMzAgMzEgMzAgMzEgMzAgMzAgMzEgMzAgMjAgMzAgMzAgMzEgMzEgMzAgMzAgMzAgMzAgMjAgMzAgMzEgMzEgMzAgMzEgMzAgMzEgMzAgMjAgMzAgMzEgMzEgMzAgMzAgMzAgMzAgMzEgMjAgMzAgMzEgMzEgMzAgMzEgMzEgMzEgMzAgMjAgMzAgMzEgMzEgMzEgMzAgMzAgMzEgMzEgMjAgMzAgMzEgMzAgMzEgMzEgMzEgMzEgMzEgMjAgMzAgMzEgMzEgMzAgMzEgMzEgMzAgMzAgMjAgMzAgMzEgMzEgMzAgMzEgMzEgMzEgMzEgMjAgMzAgMzEgMzEgMzEgMzAgMzEgMzEgMzAgMjAgMzAgMzEgMzEgMzAgMzAgMzEgMzAgMzEgMjAgMzAgMzEgMzAgMzEgMzEgMzEgMzEgMzEgMjAgMzAgMzEgMzAgMzAgMzAgMzAgMzEgMzEgMjAgMzAgMzAgMzEgMzEgMzAgMzEgMzAgMzAgMjAgMzAgMzEgMzEgMzEgMzAgMzAgMzEgMzAgMjAgMzAgMzEgMzEgMzAgMzAgMzEgMzAgMzAgMjAgMzAgMzEgMzEgMzAgMzEgMzAgMzAgMzEgMjAgMzAgMzEgMzEgMzAgMzEgMzEgMzEgMzAgMjAgMzAgMzEgMzEgMzAgMzAgMzAgMzAgMzEgMjAgMzAgMzEgMzEgMzAgMzEgMzEgMzAgMzAgMjAgMzAgMzEgMzAgMzEgMzEgMzEgMzEgMzEgMjAgMzAgMzEgMzAgMzAgMzAgMzAgMzAgMzAgMjAgMzAgMzEgMzEgMzAgMzEgMzEgMzEgMzAgMjAgMzAgMzEgMzEgMzAgMzAgMzEgMzAgMzAgMjAgMzAgMzEgMzAgMzEgMzEgMzEgMzEgMzEgMjAgMzAgMzEgMzAgMzAgMzAgMzEgMzEgMzEgMjAgMzAgMzAgMzEgMzEgMzAgMzAgMzAgMzAgMjAgMzAgMzEgMzEgMzAgMzEgMzEgMzAgMzAgMjAgMzAgMzEgMzEgMzAgMzAgMzEgMzAgMzAgMjAgMzAgMzEgMzEgMzEgMzEgMzEgMzAgMzE=";
    char m[100];
    int cur = 0;

    for (int i=0; i<3000; i++){
        if(!(c[i] == 'M' || c[i] == 'z' || c[i] == 'g')){
            m[cur] = c[i];
            cur++;
        }
    }

    printf("%s",m);

    return 0;
}