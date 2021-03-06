// ConsoleApplication2.cpp : Defines the entry polong long  for the console application.
//

#include "stdafx.h"
#include <iostream>


class Node {
public:
	long long  m_score;
	Node *m_prev;
	Node *m_next;
	
	Node(long long  score) {
		m_score = score;
		m_next = this;
		m_prev = this;
	}

	~Node() {
		m_next->m_prev = m_prev;
		m_prev->m_next = m_next;
		m_next = NULL;
		m_prev = NULL;
	}
	
	Node* insert_not_mult_23(Node* newnode) {
		Node* one_forward = this->m_next;
		Node* two_forward = one_forward->m_next;
		one_forward->m_next = newnode;
		two_forward->m_prev = newnode;
		newnode->m_prev = one_forward;
		newnode->m_next = two_forward;
		return newnode;
	}

	Node* insert_mult_23_part1(Node* newnode) {
		Node* seven_backward = this->m_prev->m_prev->m_prev->m_prev->m_prev->m_prev->m_prev;
		Node* temp_prev = seven_backward->m_prev;
		Node* temp_next = seven_backward->m_next;
		temp_prev->m_next = temp_next;
		temp_next->m_prev = temp_prev;
		seven_backward->m_score += newnode->m_score;
		return seven_backward;
	}
};


int  num_players = 446;
long long  * player_list = new long long [num_players];
long long  last_marble = 7152200;


int  main()
{
	Node * x = new Node(0);
	Node * y = new Node(2);
	Node * z = new Node(1);
	x->m_next = y;
	y->m_next = z;
	z->m_next = x;
	z->m_prev = y;
	y->m_prev = x;
	x->m_prev = z;



	for (int  i = 0; i < num_players; i++) {
		player_list[i] = 0;
	}


	long long  current_marble_score = 3;

	while (current_marble_score <= last_marble) {
		Node* temp = new Node(current_marble_score);
		if (temp->m_score % 23 != 0) {
			y = y->insert_not_mult_23(temp);
		}

		else {
			y = y->insert_mult_23_part1(temp);
			player_list[current_marble_score % num_players] += y->m_score;
			y = y->m_next;
		}
		current_marble_score += 1;
	}
	
	for (long long  i = 1; i < 30; i++) {
		std::cout << x->m_score << "  ";
		x = x->m_next;
	}
	std::cout << std::endl;

	long long  current_largest_score = 0;
	for (long long  i = 0; i < num_players; i++) {
		if (player_list[i] > current_largest_score)
			current_largest_score = player_list[i];
	}
	


	std::cout << "Max score: " << current_largest_score << std::endl;

    return 0;
}

