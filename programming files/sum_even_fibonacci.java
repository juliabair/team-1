// summing even numbers in the fibonacci sequence
public class sum_even_fibonacci {

    // main function
    public static void main(String[] args) {
        // initializing two integers
        int a = 0, b = 1;
        //sum even initialized to 0
        int sumEven = 0;

        // going through this loop and doing the fibinaci sequence for each one
        while (b < 4000000) {
            if (b % 2 == 0) {
                sumEven += b;
            }
            int temp = b;
            b = a + b;
            a = temp;
        }
        // printing the number
        System.out.println(sumEven);
    }
}

// answer should be 4613732
