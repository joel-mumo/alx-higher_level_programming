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

	if (head == NULL || (*head)->next == NULL)
		return (0);

	temp = *head;
	while (temp)
	{
		temp = temp->next;
		len++;
	}

	return (1);
}
