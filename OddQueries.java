// https://codeforces.com/problemset/problem/1807/D
package CompetitiveCoding;
import java.util.Scanner;
public class OddQueries {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for(int i = 0; i < t; i++)
        {
            int n = scanner.nextInt(), q = scanner.nextInt();
            boolean[] ans = new boolean[q];
            String[] data = scanner.nextLine().split(" ");
            for(int j = 0; j < q; j++)
            {
                int l=scanner.nextInt(), r=scanner.nextInt(); String k=scanner.next();
                String[] temp = new String[n];
                for(int i1 = 0; i < n; i++)
                    temp[i1] = data[i1];
                for(int z = l; z <= r; z++)
                    temp[z-1] = k;
                int sum = 0;
                for(String num : temp)
                    sum += Integer.parseInt(num);
                if (sum % 2 == 0)
                    ans[j] = false;
                else
                    ans[j] = true;
            }
            for(boolean a : ans)
                System.out.println(a);
        }
    }
}
