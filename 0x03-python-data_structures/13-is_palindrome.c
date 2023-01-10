#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: The head of node
 * Return: 1 if it is a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	unsigned int len = 1;
	listint_t *temp;

	if (head == NULL || *head == NULL)
		return (1);
	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	listint_t *prev = NULL;
	listint_t *current = slow->next;

	while (current != NULL)
	{
		listint_t *next = current->next;

		current->next = prev;

		prev = current;
		current = next;
	}
	slow->next = prev;
	listint_t *p = *head;
	listint_t *q = slow->next

	while (q != NULL)
	{
		if (p->n != q->n)
		{
			return (0);
		}
		p = p->next;
		q = q->next;
	}
	return (1);
}
