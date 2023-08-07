#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a loop or a cycle
 * @list: list to be checked
 * Return: 1 if true and 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
	{
		return (0);
	}

	while (fast && slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
