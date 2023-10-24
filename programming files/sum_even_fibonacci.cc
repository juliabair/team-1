#include <iostream>

int main()
{
    // Define first two Fibonacci Numbers
    int a = 0, b = 1;
    int sum_even = 0;
    // Summing even Fibonacci Numbers up to 4000000
    while (b < 4000000) {
        // Check for even number
        if (b % 2 == 0) {
            // Sum if even
            sum_even += b;
        }
        // Update Fibonacci Sequence
        int temp = b;
        b = a + b;
        a = temp;
    }
    // Print the sum
    std::cout << sum_even << std::endl;

    return 0;
}

// answer should be 4613732
