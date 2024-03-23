#include "lists.h"

/**
 * check_cycle - draft
 * @list: draft
 *
 * Return: draft
 */
int check_cycle(listint_t *list)
{
	listint_t *t;
	listint_t *c;
	int r = 0;

	if (list == 0)
		return (r);
	while(list && r == 0)
	{
		t = list;
		c = list;
		while(t)
		{
			if (c == t->next)
			{
				r = 1;
				break;
			}
			t = t->next;
		}
		list = list->next;
	}
	return (r);
}
