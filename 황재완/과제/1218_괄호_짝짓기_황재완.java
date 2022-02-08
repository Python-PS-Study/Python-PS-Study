import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;
import java.util.StringTokenizer;

/*
실행시간: 108 ms
메모리: 18,344 kb
*/
class Solution {

    private static Map<Character, Character> hashMap = new HashMap<Character, Character>() {
        {
            put(')', '(');
            put(']', '[');
            put('}', '{');
            put('>', '<');
        }
    };
    private static  Stack<Character> stack = new Stack<>();

    public static void main(String args[]) throws Exception {

//        System.setIn(new FileInputStream("input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int T = 10;

        for (int test_case = 1; test_case <= T; test_case++) {
            int n = Integer.parseInt(in.readLine());

            char[] ps = in.readLine().toCharArray();
            for (char parenthesis : ps) {
                if (parenthesis == '(' || parenthesis == '[' || parenthesis == '{' || parenthesis == '<') {
                    stack.push(parenthesis);
                } else {
                    if (stack.peek() == hashMap.get(parenthesis)) {
                        stack.pop();
                    } else break;
                }
            }
            if (stack.empty()) {
                System.out.printf("#%d %d%n", test_case, 1);
            } else {
                System.out.printf("#%d %d%n", test_case, 0);
            }
            stack.clear();
        }

    }
}