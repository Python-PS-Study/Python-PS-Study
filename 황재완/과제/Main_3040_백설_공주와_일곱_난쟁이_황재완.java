import java.io.*;
import java.util.Scanner;

/**
 * 실행시간: 112 ms
 * 메모리: 12880	KB
 */
public class Main {
    static boolean[] isSelected = new boolean[9];
    static int total9;
    static int nums[] = new int[9];
    static void combinations(int cnt, int start, int tot) {
        if (cnt==2) {
            if (total9 - tot == 100) {
                for (int i = 0; i < 9; i++) {
                    if (!isSelected[i]) System.out.println(nums[i]);
                }
            }
            return;
        }
        for (int i = start; i < 9; i++) {
            isSelected[i] = true;
            combinations(cnt+1, i+1, tot + nums[i]);
            isSelected[i] = false;
        }
    }
    public static void main(String args[]) throws Exception {
//        System.setIn(new FileInputStream("input.txt"));
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 9; i++) {
            nums[i] = sc.nextInt();
            total9 += nums[i];
        }
        combinations(0, 0, 0);
    }
}