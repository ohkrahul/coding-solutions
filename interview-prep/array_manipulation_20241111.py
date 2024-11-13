'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
Link: https://practice.geeksforgeeks.org/problems/array-manipulation
'''
```java
import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Solution {

    // Complete the arrayManipulation function below.
    static long arrayManipulation(int n, int[][] queries) {
        long[] arr = new long[n + 2];

        for (int[] query : queries) {
            arr[query[0]] += query[2];
            arr[query[1] + 1] -= query[2];
        }

        long max = 0;
        long sum = 0;
        for (long num : arr) {
            sum += num;
            max = Math.max(max, sum);
        }

        return max;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nm = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nm[0]);

        int m = Integer.parseInt(nm[1]);

        int[][] queries = new int[m][3];

        for (int i = 0; i < m; i++) {
            String[] queriesRowItems = scanner.nextLine().split(" ");
            for (int j = 0; j < 3; j++) {
                int queriesItem = Integer.parseInt(queriesRowItems[j]);
                queries[i][j] = queriesItem;
            }
        }

        long result = arrayManipulation(n, queries);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
```