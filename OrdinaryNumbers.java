package CompetitiveCoding;
import java.util.Scanner;
public class OrdinaryNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for(int i = 0; i < T; i++)
        {
            int n = scanner.nextInt(), count = 0;
            for(int j = 1; j <= n; j++)
            {
                String num = Integer.toString(j);
                char[] digits = num.toCharArray();
                boolean flag = true;
                char d1 = digits[0];
                for(char d: digits)
                {
                    if (d != d1)
                    {
                        flag = false;
                        break;
                    }
                }
                if (flag)
                    count++;
            }
            System.out.println(count);
        }
    }
}
