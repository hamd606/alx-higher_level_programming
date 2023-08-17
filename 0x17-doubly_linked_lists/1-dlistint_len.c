#include "lists.h"

/**
 * dlistint_len - Prints the length of a dlistint
 * @h: input list (dlistint object)
 * Return: the length of h as a size_t
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t len = 0;

	while (h != NULL)
	{
		len++;
		h = h->next;

	}

	return (len);

}

