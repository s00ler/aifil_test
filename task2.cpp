#include <iostream>

void split_vector(int N, int M) {
        if ((N <= M)or (M < 1) or (N < 1)) {
                std::cout << "Incorrect parameters" << '\n';
                return;
        }
        int part_size = N / M, left_shift = N % M, right_shift = 0;
        if (left_shift - right_shift > 1) {
                left_shift >>= 1;
                right_shift = left_shift + (left_shift % 2);
        }
        for (size_t i = left_shift; i < N - right_shift; i += part_size)
                std::cout << "[" << i << ", " << i + part_size - 1 << "]\n";
}

int main(int argc, char const *argv[]) {
        if (argc < 3) {
                std::cout << "Invalid usage.\n"
                          << "Right way: python task1.py < int number > < int number >"
                          << '\n';
                return 0;
        }
        split_vector(strtol(argv[1], nullptr, 0), strtol(argv[2], nullptr, 0));
        return 0;
}
