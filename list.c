#include <stdio.h>
#include <stdlib.h>
int main() {
   int *list = malloc(3 * sizeof(int)); //list is a pointer, and assign space for 3 integers
   if (list == NULL) //Something bad happened, exit the program
   {
        return 1;
   }
   list[0] = 1;
   list[1] = 2;
   list[2] = 3;

//Below is used for allocating a new list
   //int *tmp = malloc(4 * sizeof(int)); //make a new list with length 4
   int *tmp = realloc(list, 4 * sizeof(int));
   if (tmp == NULL)
   {
        free(list);
        return 1;
   }

// Using realloc allows for you to not need to insert the items again
//    for (int i = 0; i < 3; i++)
//    {
//         tmp[i] = list[i]; //copy list into temporary chunk of memory tmp
//    }

   tmp[3] = 4; // add to tmp

   free(list); //free the original list

   list = tmp; //now use list which is a better name than tmp for a list

   for (int i = 0; i < 4; i++)
   {
        printf("%i\n", list[i]);
   }

   free(list);

   return 0;
}
