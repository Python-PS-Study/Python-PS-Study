import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

/*
실행시간: 3424 ms
메모리: 166156 KB
*/
// 접근법: 오큰수의 변형인 왼큰수 문제이다.
public class Main {

    private static Stack<Integer> stack = new Stack<>();
    private static int[] heights;
    private static int[] res;

    public static void main(String args[]) throws Exception {

//        System.setIn(new FileInputStream("input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(in.readLine());
        heights = new int[N];
        res = new int[N];
        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        for (int i = 0; i < N; i++) {
            heights[i] = Integer.parseInt(st.nextToken());
        }
        stack.push(N-1); // 첫번째 탑은 레이저를 수신할 왼쪽의 탑이 없으므로 스택에 넣는다.
        for (int i = N-2; i >= 0; i--) {
            while(!stack.isEmpty() && heights[i] > heights[stack.peek()]) { // 스택이 비지 않고 현재 스택의 탑보다 크다면 계속 스택에서 pop
                res[stack.pop()] = i + 1; // 인덱스 번호를 1 ~ N까지 빌딩번호로 매핑
            }
            stack.push(i); // 스택의 top 보다 작다면 넣거나 크다면 스택에서 작은 값들을 처리하고 넣는다.
        }
        // 스택에 남아 있는 탑들은 자기 보다 왼쪽에 큰 탑이 없으므로 0으로 처리하는데 안해도 상관 없다.
        while(!stack.isEmpty()) {
            res[stack.pop()] = 0;
        }
        // 결과 출력
        for (int i = 0; i < N; i++) {
            System.out.print(res[i] + " ");
        }
    }
}