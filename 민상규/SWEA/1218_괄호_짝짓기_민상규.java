
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

/*
 * 실행 시간 : 107 ms
 * 메모리 : 18,396 kb
*/
class Solution {
	static int n, answer;
	static char[] str;
	static Stack<Character> stack = new Stack<Character>();

	public static void main(String args[]) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		for (int test_case = 1; test_case <= 10; test_case++) {
			n = Integer.parseInt(in.readLine());

			stack.clear(); // 스택 초기화
			answer = 1;

			str = in.readLine().toCharArray();
			search: for (int i = 0; i < n; i++) {
				switch (str[i]) {
				case '[':
				case '{':
				case '(':
				case '<':
					stack.push(str[i]);
					break;
				case ']':
					if (stack.peek() != '[') {
						answer = 0;
						break search;
					}
					stack.pop();
					break;
				case '}':
					if (stack.peek() != '{') {
						answer = 0;
						break search;
					}
					stack.pop();
					break;
				case ')':
					if (stack.peek() != '(') {
						answer = 0;
						break search;
					}
					stack.pop();
					break;
				case '>':
					if (stack.peek() != '<') {
						answer = 0;
						break search;
					}
					stack.pop();
					break;
				}

			}

			System.out.printf("#%d %d\n", test_case, answer);
		}
	}

}