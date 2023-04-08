// https://codeforces.com/problemset/problem/1808/A
package CompetitiveCoding;
import java.util.Arrays;
import java.util.Scanner;

public class LuckiestNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for(int i = 0; i < t; i++)
        {
            int l, r;
            l = scanner.nextInt();
            r = scanner.nextInt();
            int luckiest=0, num= 0;
            for(int j = r; j >= l; j--)
            {
                String n = Integer.toString(j);
                char[] digits = n.toCharArray();
                int len = digits.length;
                Arrays.sort(digits);
                int luck =  Character.getNumericValue(digits[len-1]) - Character.getNumericValue(digits[0]);
                if (luck > luckiest)
                {
                    luckiest = luck;
                    num = j;
                }
            }
            System.out.println(num);
        }
        scanner.close();
    }
}
