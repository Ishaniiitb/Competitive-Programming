package CompetitiveCoding;

import java.util.Scanner;

public class FromZeroToY {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int i = 0; i < t; i++) {
            int x = scanner.nextInt();
            String y = scanner.next();
            int l = y.length();
            int target = Integer.parseInt(y);
            int steps = 0;
            while(l >= 0)
            {
                int n = (int)(target / (x * Math.pow(10, l)));
                if(n == 0)
                    l--;
                else
                {
                    target -= (int)(n * x * Math.pow(10,l));
                    steps += n;
                }
            }
            steps += target;
            System.out.println(steps);
        }
    }
}
