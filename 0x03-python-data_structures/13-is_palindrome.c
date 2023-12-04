#include "lists.h"

/**
 * reverseList - Reverses a linked list
 * @head: a pointer to the first node
 * Return: pointer to first node of the reversed
 */
listint_t *reverseList(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to a pointer to the first node of the list
 * Return: 1 if yes 0 for no
 */
int is_palindrome(listint_t **head)
{

	listint_t *slow;
	listint_t *fast;
	listint_t *first_half;
	listint_t *second_half;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	slow = *head;
	fast = *head;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	second_half = reverseList(slow->next);

	first_half = *head;
	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
			return (0);

		first_half = first_half->next;
		second_half = second_half->next;
	}

	return (1);
}
