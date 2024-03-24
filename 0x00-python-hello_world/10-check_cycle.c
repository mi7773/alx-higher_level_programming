#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - draft
 * @list: draft
 *
 * Return: draft
 */
int check_cycle(listint_t *list)
{
	node *c = NULL;
	node *p = NULL;
	int r = 0;

	while(list && r == 0)
	{
		node *t = p;
		while(t)
		{
			if (list == t->d)
			{
				r = 1;
				break;
			}
			t = t->n;
		}
		if (r == 0)
		{
			c = malloc(sizeof(node));
			c->d = list;
			c->n = p;
			p = c;
			list = list->next;
		}
	}
	while(p)
	{
		c = p;
		p = p->n;
		free(c);
	}
	return (r);
}
