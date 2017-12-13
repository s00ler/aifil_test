#include <vector>
#include <iostream>

std::vector<int> factor(int value) {
        std::vector<int> result;
        int d = 2;
        while (d * d <= value) {
                if (value % d == 0) {
                        result.push_back(d);
                        value /= d;
                }
                else
                        d++;
        }
        if (value > 1)
                result.push_back(value);
        return result;
}

void print_vector(std::vector<int> vec) {
        std::cout << "[";
        for (size_t i = 0; i < vec.size(); i++) {
                if (i != 0)
                        std::cout << ", ";
                std::cout << vec[i];
        }
        std::cout << "]" << '\n';
}

void factorize_vector(int N) {
        for (size_t i = 1; i <= N; i++) {
                std::cout << i <<": ";
                print_vector(factor(i));
        }
}

int main(int argc, char const *argv[]) {
        if (argc < 2) {
                std::cout << "Right way: python task1.py <int number>" << std::endl;
                return 0;
        }
        factorize_vector(strtol(argv[1], nullptr, 0));
        return 0;
}
