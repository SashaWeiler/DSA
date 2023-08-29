#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;

int main() {
    node *list = NULL;

    node *n = malloc(sizeof(node)); //allocating size for the node, not the whole array like before
    if (n == NULL)
    {
        return 1;
    }

    // Think of this like creating single node in list where there is a number and the next value
    // is pointing to nothing, indicating there is no next item
    n->number = 1;
    n->next=NULL;
    list = n; // list is the address of the actual node n

    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list); // If the memory isn't available, free the list and finish the program
        return 1;
    }

    n->number=2;
    n->next = NULL;

    list->next = n;

    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list->next);
        free(list);
        return 1;
    }
    n->number = 3;
    n->next = NULL;
    list->next->next = n;
    // list pointer is pointing at the 1 node, which is pointing at the 2 node, which is pointing at the 3 node

// give a temporary pointer to a node called tmp and initialize it to what is at the beginning of the list
// keep doing this as long as tmp is not = NULL
// update pointer tmp, to be the pointer of tmp's next field
    for(node *tmp = list; tmp != NULL; tmp = tmp->next)
    {
        printf("%i\n", tmp->number); // print out the number field at that node
    }

    while (list != NULL)
    {
        node *tmp = list->next; //point not at the list itself, but the next node
        // if you free the first node, then the rest of the nodes will be in memory without being able to access them from the list
        free(list); //This is the first node in the linked list, not the whole list
        // Now that you have the next node above, it's safe to free up the first node
        list = tmp; //Reassign
    }

   return 0;
}
