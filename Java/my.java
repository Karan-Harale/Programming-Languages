// Java program for Compute maximum power
// to which K can be raised so that
// given condition remains true
class GFG
{

// Function to return the largest
// power
static int calculate(int n, int k,
					int m, int power)
{

	// If n is greater than given M
	if (n > m)
	{
		if (power == 0)
			return 0;
		else
			return power - 1;
	}

	// If n == m
	else if (n == m)
		return power;

	else
		// Checking for the next power
		return calculate(n * k, k, m,
						power + 1);
}

// Driver Code
public static void main (String[] args)
{
	int N = 3, K = 3, M = 8;

	System.out.println(calculate(N, K, M, 0));
}
}

// This code is contributed by AnkitRai01
