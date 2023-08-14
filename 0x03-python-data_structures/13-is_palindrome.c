#include "lists.h"

/**
 * is_palindrome - checks if list is palindrome
 * @head: ptr to the head of the list
 * Return: 0 if not palindrome otherwise 1
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_palindrome(head, *head));
}

/**
 * check_palindrome - checks if the list is palindrome
 * @head: ptr to the head of the list
 * @last: ptr to the last node of the list
 * Return: 0 if not palindrome otherwise 1
 */
int check_palndrome(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (check_palindrome(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
