#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @next: points to the next node
 * @n: number of nodes
 * Description: singly linked list node structure
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);
listint_t *add_nodeint(listint_t **head, const int n);
int check_cycle(listint_t *list);
void free_listint(listint_t *head);

#endif /* LISTS_H */
