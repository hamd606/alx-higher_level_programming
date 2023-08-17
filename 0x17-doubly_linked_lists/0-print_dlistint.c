#include "lists.h"

/**
 * print_dlistint - Prints the length of a dlistint
 * @h: input list (dlistint object)
 * Return: the length of h as a size_t
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t len = 0;

	while (h != NULL)
	{
		len++;
		printf("%d\n", h->n);
		h = h->next;

	}

	return (len);

}

