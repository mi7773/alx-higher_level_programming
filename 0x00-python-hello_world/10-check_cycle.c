#include "lists.h"

/**
 * check_cycle - draft
 * @list: draft
 *
 * Return: draft
 */
int check_cycle(listint_t *list)
{
	listint_t *copy = list;
	listint_t *t = NULL;
	listint_t *p = NULL;
	int i = 0;
	int j = 0;
	int r = 0;

	while(copy && r == 0)
	{
		t = copy->next;
		p = list;
		j = 0;
		while(t && j < i)
		{
			if (t == p)
			{
				r = 1;
				break;
			}
			p = p->next;
			j++;
		}
		i++;
		copy = copy->next;
	}
	return (r);
}
