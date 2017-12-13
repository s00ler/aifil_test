#include <iostream>

struct Node {
        int value;
        Node *next = nullptr;
        Node(int x) {
                this->value = x;
        }
};

Node *create_list(int argc, char const *argv[]) {
        if (argc < 2)
                return nullptr;
        Node *first_node = new Node(atoi(argv[1])), *cur = first_node;
        for (size_t i = 2; i < argc; ++i) {
                cur->next = new Node(atoi(argv[i]));
                cur = cur->next;
        }
        return first_node;
}

void print_list(Node *head) {
        while (head) {
                std::cout << head->value << ' ';
                head = head->next;
        }
        std::cout << '\n';
}

Node *split_list(Node *head) {
        Node *end_finder = head, *prev = head;
        while (end_finder && end_finder->next) {
                prev = head;
                head = head->next;
                end_finder = end_finder->next->next;
        }
        if (end_finder) {
                prev = head;
                head = head->next;
        }
        prev->next = nullptr;
        return head;
}

Node *reverse_list(Node *head) {
        Node *tmp = nullptr;
        Node *prev = nullptr;
        while (head) {
                tmp = head->next;
                head->next = prev;
                prev = head;
                head = tmp;
        }
        return prev;
}

Node *merge(Node *first, Node *second) {
        Node *result = first, *head = result;
        first = first->next;
        while (second && first) {
                result->next = second;
                result = result->next;
                second = second->next;
                result->next = first;
                result = result->next;
                first = first->next;
        }
        if (second) {
                result->next = second;
                result = result->next;
        }
        return head;
}

Node *reorder_list(Node *head) {
        Node *mid = split_list(head);
        mid = reverse_list(mid);
        Node *result = merge(head, mid);
        return result;
}

int main(int argc, char const *argv[]) {
        Node *head = create_list(argc, argv);
        if (head)
                print_list(reorder_list(head));
        else
                std::cout << "Incorrect usage. Use ./task4.out <int> [<int> ...]"
                          << '\n';
        return 0;
}
