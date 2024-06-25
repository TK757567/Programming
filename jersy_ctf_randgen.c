#include <stdio.h>
#include <stdlib.h>
int main () {
   int i, n;
   
   n = 206;
   

   srand(1676695692);


   for( i = 0 ; i < n ; i++ ) {
      printf("%d\n", (rand() % 256)+1);
   }
   
   return(0);
}