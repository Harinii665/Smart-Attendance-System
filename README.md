		# Smart-Attendance-System
		Overview
		  The Smart Attendance System is a face recognition-based attendance management solution built using Python, OpenCV, and Face Recognition libraries. It automates the process of capturing, training, and 
		  recognizing student or employee attendance efficiently.
		
		Features
		  Capture Photos: Enables users to capture and store face images for training.
		
		Train Data: Processes captured images to create face embeddings for recognition.
		
		Recognize Face: Identifies faces in real-time and marks attendance.
		
		Show Attendance: Exports attendance records into an Excel file for easy access.
		
		Technologies Used
		
		Programming Language: Python
		
		GUI Framework: Tkinter
		
		Computer Vision: OpenCV, Face Recognition
		
		Data Processing: Pandas, JSON, NumPy
		
		Text-to-Speech: pyttsx3
		
		Storage: JSON (for attendance logs), Excel (for exported records)



  import java.util.*;

public class LeftFactoring {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); sc.nextLine();
        for (int i = 0; i < n; i++) {
            String[] parts = sc.nextLine().split("->");
            String lhs = parts[0].trim(), rhs[] = parts[1].split("\\|");
            String prefix = findCommonPrefix(rhs);
            if (!prefix.isEmpty()) {
                System.out.println(lhs + "->" + prefix + lhs + "'");
                System.out.println(lhs + "'->" + String.join("|", Arrays.stream(rhs)
                        .map(r -> r.startsWith(prefix) ? r.substring(prefix.length()) : r)
                        .toArray(String[]::new)));
            }
        }
    }

    private static String findCommonPrefix(String[] rhs) {
        String prefix = rhs[0];
        for (String r : rhs) while (r.indexOf(prefix) != 0) prefix = prefix.substring(0, prefix.length() - 1);
        return prefix;
    }
}
		
		5] import java.util.*;
		import java.io.*;
		public class exp5 {
		static char nonTerminals[], terminals[];
		static int nonTermLen, termLen;
		static String grammar[][], first[], follow[];
		public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter the non-terminals:");
		String nt = br.readLine();
		nonTermLen = nt.length();
		nonTerminals = nt.toCharArray();
		System.out.println("Enter the terminals:");
		String t = br.readLine();
		termLen = t.length();
		terminals = t.toCharArray();
		System.out.println("Specify the grammar (Enter 9 for epsilon production):");
		grammar = new String[nonTermLen][];
		for (int i = 0; i < nonTermLen; i++) {
		System.out.println("Enter the number of productions for " + nonTerminals[i]);
		int n = Integer.parseInt(br.readLine());
		grammar[i] = new String[n];
		System.out.println("Enter the productions:");
		for (int j = 0; j < n; j++)
		grammar[i][j] = br.readLine();
		}
		first = new String[nonTermLen];
		for (int i = 0; i < nonTermLen; i++)
		first[i] = calculateFirst(i);
		System.out.println("First Set:");
		printSets(first);
		follow = new String[nonTermLen];
		for (int i = 0; i < nonTermLen; i++)
		follow[i] = calculateFollow(i);
		System.out.println("Follow Set:");
		printSets(follow);
		}
		static String calculateFirst(int index) {
		String temp = "";
		for (String production: grammar[index]) {
		char firstChar = production.charAt(0);
		if (Character.isLowerCase(firstChar) || firstChar == '9')
		temp += firstChar;
		else
		temp += calculateFirst(getIndex(firstChar));
		TITLE: Implementation of First and Follow functions using JAVA programming.
		
		}
		return temp;
		}
		static String calculateFollow(int index) {
		String temp = "";
		if (index == 0)
		temp = "$";
		for (int j = 0; j < nonTermLen; j++) {
		for (String production: grammar[j]) {
		for (int k = 0; k < production.length(); k++) {
		if (production.charAt(k) == nonTerminals[index]) {
		if (k == production.length() - 1) {
		if (j < index)
		temp += follow[j];
		} else {
		int nextIndex = getIndex(production.charAt(k + 1));
		if (nextIndex != -1) {
		temp += first[nextIndex];
		if (first[nextIndex].contains("9") && k + 1 == production.length() - 1)
		temp += follow[j];
		} else
		temp += production.charAt(k + 1);
		}
		}
		}
		}
		}
		return temp;
		}
		static void printSets(String[] set) {
		for (String s: set)
		System.out.println(removeDuplicates(s));
		}
		static int getIndex(char c) {
		for (int i = 0; i < nonTermLen; i++) {
		if (nonTerminals[i] == c)
		return i;
		}
		return -1;
		}
		static String removeDuplicates(String str) {
		char[] chars = str.toCharArray();
		Set < Character > charSet = new LinkedHashSet < > ();
		for (char c: chars)
		charSet.add(c);
		StringBuilder sb = new StringBuilder();
		for (Character character: charSet)
		sb.append(character);
		return sb.toString();
		}
		}
		
		Sample output:
		Enter the non-terminals:
		EAB
		Enter the terminals:
		ilj
		Specify the grammar (Enter 9 for epsilon production):
		Enter the number of productions for E
		1
		Enter the productions:
		AB
		Enter the number of productions for A
		1
		Enter the productions:
		il
		Enter the number of productions for B
		1
		Enter the productions:
		j
		First Set:
		i
		i
		j
		Follow Set:
		$
		j
		$
		5]import java.util.*;
		
		public class FirstFollow {
		    static Map<String, List<String>> prod = new HashMap<>();
		    static Map<String, Set<String>> first = new HashMap<>();
		    static Map<String, Set<String>> follow = new HashMap<>();
		    static Set<String> nts = new HashSet<>();
		
		    static Set<String> getFirst(String X) {
		        if (!X.matches("[A-Z]")) return Set.of(X);
		        if (first.containsKey(X)) return first.get(X);
		
		        Set<String> res = new HashSet<>();
		        for (String rhs : prod.get(X)) {
		            boolean allEps = true;
		            for (int i = 0; i < rhs.length(); i++) {
		                String s = rhs.charAt(i) + "";
		                Set<String> f = getFirst(s);
		                res.addAll(f); res.remove("@");
		                if (!f.contains("@")) { allEps = false; break; }
		            }
		            if (allEps) res.add("@");
		        }
		        return first.put(X, res) == null ? res : first.get(X);
		    }
		
		    static void getFollow(String start) {
		        nts.forEach(nt -> follow.put(nt, new HashSet<>()));
		        follow.get(start).add("$");
		        boolean changed;
		        do {
		            changed = false;
		            for (var e : prod.entrySet()) {
		                String A = e.getKey();
		                for (String rhs : e.getValue()) {
		                    for (int i = 0; i < rhs.length(); i++) {
		                        String B = rhs.charAt(i) + "";
		                        if (!nts.contains(B)) continue;
		                        Set<String> temp = new HashSet<>();
		                        boolean eps = true;
		                        for (int j = i + 1; j < rhs.length(); j++) {
		                            String C = rhs.charAt(j) + "";
		                            Set<String> f = getFirst(C);
		                            temp.addAll(f); temp.remove("@");
		                            if (!f.contains("@")) { eps = false; break; }
		                        }
		                        if (i == rhs.length() - 1 || eps)
		                            temp.addAll(follow.get(A));
		                        if (follow.get(B).addAll(temp))
		                            changed = true;
		                    }
		                }
		            }
		        } while (changed);
		    }
		
		    public static void main(String[] args) {
		        Scanner sc = new Scanner(System.in);
		        int n = Integer.parseInt(sc.nextLine());
		        String ntsStr = sc.nextLine();
		        for (char c : ntsStr.toCharArray()) nts.add(c + "");
		
		        for (int i = 0; i < n; i++) {
		            String[] p = sc.nextLine().split("->");
		            prod.putIfAbsent(p[0], new ArrayList<>());
		            prod.get(p[0]).addAll(List.of(p[1].split("\\|")));
		        }
		
		        nts.forEach(nt -> getFirst(nt));
		        getFollow(ntsStr.charAt(0) + "");
		
		        nts.forEach(nt -> System.out.println("FIRST(" + nt + ") = " + first.get(nt)));
		        nts.forEach(nt -> System.out.println("FOLLOW(" + nt + ") = " + follow.get(nt)));
		    }
		}
		9] import java.util.Scanner;
		public class Exp9 {
		static int[] stack;
		static int top, n;
		public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		top = -1;
		System.out.println("Enter the size of stack[MAX=100]: ");
		n = scanner.nextInt();
		if (n <= 0) {
		System.out.println("Invalid stack size.");
		return;
		}
		stack = new int[n];
		System.out.println("\n\tStack Operations:");
		System.out.println("\t--------------------------");
		System.out.println("\t1. Push");
		System.out.println("\t2. Pop");
		System.out.println("\t3. Display");
		System.out.println("\t4. EXIT");
		int choice;
		do {
		System.out.println("\nEnter your choice: ");
		choice = scanner.nextInt();
		switch (choice) {
		case 1:
		push(scanner);
		break;
		case 2:
		pop();
		break;
		case 3:
		display();
		break;
		case 4:
		TITLE: Implementation of Stack Allocation Strategy using JAVA programming.
		
		System.out.println("\nEXIT");
		break;
		default:
		System.out.println("Please enter a valid choice.");
		}
		} while (choice != 4);
		scanner.close();
		}
		static void push(Scanner scanner) {
		if (top >= n - 1) {
		System.out.println("\nStack overflow");
		} else {
		System.out.println("Enter a value to be pushed: ");
		int x = scanner.nextInt();
		top++;
		stack[top] = x;
		}
		}
		static void pop() {
		if (top == -1)
		System.out.println("\nStack underflow");
		else {
		System.out.println("\nThe popped element is " + stack[top]);
		top--;
		}
		}
		static void display() {
		if (top >= 0) {
		System.out.println("\nThe elements in the stack are:");
		for (int i = top; i >= 0; i--)
		System.out.println(stack[i]);
		System.out.println("\nSelect next choice");
		} else
		System.out.println("\nThe stack is empty.");
		}
		}
		Sample Output:
		Enter the size of stack[MAX=100]: 10
		Stack Operations:
		--------------------------
		1. Push
		2. Pop
		3. Display
		4. EXIT
		
		Enter your choice:
		1
		Enter a value to be pushed:
		5
		Enter your choice:
		1
		Enter a value to be pushed:
		8
		Enter your choice:
		1
		Enter a value to be pushed:
		3
		Enter your choice:
		3
		The elements in the stack are:
		3
		8
		5
		Select next choice
		Enter your choice:
		2
		The popped element is 3
		Enter your choice:
		3
		The elements in the stack are:
		8
		5
		Select next choice
		Enter your choice:
		4
		EXIT
		
		10. Implementation of Intermediate Code Generation.
		
		import java.util.ArrayList;
		import java.util.List;
		import java.util.Scanner;
		import java.util.Stack;
		class Instruction {
		String op;
		String arg1;
		String arg2;
		String result;
		Instruction(String op, String arg1, String arg2, String result) {
		this.op = op;
		this.arg1 = arg1;
		this.arg2 = arg2;
		this.result = result;
		}
		@Override
		public String toString() {
		return result + " = " + arg1 + " " + op + " " + arg2;
		}
		}
		class IntermediateCodeGenerator {
		private List<Instruction> instructions;
		private Stack<String> operands;
		private int tempCount;
		IntermediateCodeGenerator() {
		instructions = new ArrayList<>();
		operands = new Stack<>();
		tempCount = 0;
		}
		public List<Instruction> generate(String expression) {
		Stack<Character> operators = new Stack<>();
		StringBuilder operand = new StringBuilder();
		for (int i = 0; i < expression.length(); i++) {
		char token = expression.charAt(i);
		if (Character.isWhitespace(token)) {
		continue;
		}
		if (Character.isLetterOrDigit(token)) {
		TITLE: Implementation of Intermediate Code Generation using JAVA programming.
		
		operand.append(token);
		if (i == expression.length() - 1 || !Character.isLetterOrDigit(expression.charAt(i + 1))) {
		operands.push(operand.toString());
		operand.setLength(0);
		}
		} else if (token == '(') {
		operators.push(token);
		} else if (token == ')') {
		while (!operators.isEmpty() && operators.peek() != '(') {
		processOperator(operators.pop());
		}
		operators.pop();
		} else if (isOperator(token)) {
		while (!operators.isEmpty() && precedence(token) <= precedence(operators.peek())) {
		processOperator(operators.pop());
		}
		operators.push(token);
		}
		}
		while (!operators.isEmpty()) {
		processOperator(operators.pop());
		}
		return instructions;
		}
		private void processOperator(char operator) {
		String operand2 = operands.pop();
		String operand1 = operands.pop();
		String result = newTemp();
		instructions.add(new Instruction(String.valueOf(operator), operand1, operand2, result));
		operands.push(result);
		}
		private String newTemp() {
		return "t" + tempCount++;
		}
		private boolean isOperator(char token) {
		return token == '+' || token == '-' || token == '*' || token == '/';
		}
		private int precedence(char operator) {
		switch (operator) {
		case '+':
		case '-':
		return 1;
		case '*':
		case '/':
		return 2;
		
		default:
		return -1;
		}
		}
		}
		public class exp10 {
		public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter an arithmetic expression:");
		String expression = scanner.nextLine();
		IntermediateCodeGenerator icg = new IntermediateCodeGenerator();
		List<Instruction> code = icg.generate(expression);
		System.out.println("Intermediate Code:");
		for (Instruction instr : code) {
		System.out.println(instr);
		}
		scanner.close();
		}
		}
		
		Sample output:
		
		a*b+c/d-e/f+g*h
		Intermediate Code:
		t0 = a * b
		t1 = c / d
		t2 = t0 + t1
		t3 = e / f
		t4 = t2 - t3
		t5 = g * h
		t6 = t4 + t5
		
		10]import java.util.*;
		class ICG {
		    static int val(char ch){
		        switch(ch){
		            case '+':
		            case '-': return 1;
		            case '*':
		            case '/': return 2;
		            case '^': return 3;
		            case '(' :return 4;
		            default : return -1;
		        }
		    }
		    public static void main(String[] args) {
		        Scanner sc=new Scanner(System.in);
		        System.out.print("Arithmetic Exp : ");
		        String exp=sc.nextLine();
		        String ans="";
		        Stack<Character> s1=new Stack<>();
		        for(int i=0;i<exp.length();i++){
		            char ch=exp.charAt(i);
		            if(val(ch)==-1 && ch!=')') ans+=ch;
		            else if(s1.isEmpty() || val(ch)>val(s1.peek())) s1.push(ch);
		            else{
		                while(!s1.isEmpty() && val(ch) <=val(s1.peek()) && s1.peek()!='('){
		                    ans+=s1.pop();
		                }
		                if(ch==')') s1.pop();
		                else s1.push(ch);
		            }
		        }
		        while(!s1.isEmpty())
		        ans+=s1.pop();
		        int j=0;
		        Stack<String> s2 =new Stack<>();
		        for(int i=0;i<ans.length();i++){
		            char ch=ans.charAt(i);
		            if(val(ch)==-1) s2.push(ch+"");
		            else{
		                String o2=s2.pop();
		                String o1=s2.pop();
		                System.out.println("t"+j+"="+o1+ch+o2);
		                s2.push("t"+j);
		                j++;
		            }
		        }
		    }
		}
		
		output:
		
		Arithmetic Exp : a*b+c/d-e/f+g*h
		t0=a*b
		t1=c/d
		t2=t0+t1
		t3=e/f
		t4=t2-t3
		t5=g*h
		t6=t4+t5
		
		1] import java.util.*;
		public class Main
		{
		public static void main(String args[])
		
		{
		
		Scanner sc = new Scanner(System.in);
		System.out.println("1. Enter the string");
		System.out.println ("2. Exit");
		System.out.println("Enter a choice");
		int n = sc.nextInt();
		while (n != 2)
		
		{
		
		System.out.println("Enter the string :");
		String s = sc.next();
		if (s.endsWith("abc"))
		
		{
		
		System.out.println(s + " " + "is Accepted");
		}
		else
		{
		
		System.out.println(s + " " + "is Not Accepted");
		}
		System.out.println("1. Enter the string\n2. Exit");
		System.out.println("Enter a choice");
		n = sc.nextInt();
		}
		}
		}
		
		2] import java.util.*;
		public class Exp2
		{
		public static void main(String[] args)
		{
		ArrayList<String> keywords = new ArrayList<>(Arrays.asList(
		"if", "else", "while", "for", "int", "float", "double", "char", "String", "boolean" ));
		ArrayList<String> operators = new ArrayList<>(Arrays.asList(
		"+", "-", "*", "/", "=", ">", "<", "!", "&", "|" ,"++","--" ));
		ArrayList<String> delimiters = new ArrayList<>(Arrays.asList(
		"(", ")", "{", "}", "[", "]", ",", ";"));
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter program with single spaces");
		String input = sc.nextLine();
		String[] arr = input.split(" ");
		int len = arr.length;
		String[] ans = new String[len];
		for (int i = 0; i < len; i++)
		
		{
		
		if (keywords.contains(arr[i]))
		
		{
		
		ans[i] = "keyword";
		}
		
		else if (operators.contains(arr[i]))
		{
		
		ans[i] = "operator";
		}
		
		else if (delimiters.contains(arr[i]))
		{
		
		ans[i] = "delimiter";
		}
		
		else if (isIdentifier(arr[i]))
		{
		
		ans[i] = "identifier";
		}
		
		else if (isLiteral(arr[i]))
		{
		
		ans[i] = "literal";
		}
		else
		
		    
		TITLE: Implementation of Lexical Analyzer using JAVA programming.
		
		{
		
		ans[i] = "unknown";
		}
		}
		for (int i = 0; i < len; i++)
		
		{
		
		System.out.println(arr[i] + ": " + ans[i]);
		}
		}
		private static boolean isIdentifier(String str)
		{
		if (Character.isDigit(str.charAt(0)))
		{
		return false;
		}
		for (char c : str.toCharArray())
		{
		if (!Character.isLetterOrDigit(c) && c != '_')
		{
		return false;
		}
		}
		return true;
		}
		private static boolean isLiteral(String str)
		{
		try
		{
		Integer.parseInt(str);
		return true;
		}
		catch (NumberFormatException e1)
		{
		try
		{
		Double.parseDouble(str);
		return true;
		}
		catch (NumberFormatException e2)
		
		{
		return false;
		}
		}
		}
		}
		
		Sample output:
		Enter program with single spaces
		java 123 { main int
		java: identifier
		123: literal
		{: delimiter
		main: identifier
		int: keyword
		
		3 and 4 
		3. Implement Elimination of Left Recursion.
		
		import java.util.Scanner;
		public class LeftRecursionElimination
		{
		public static void main(String[] args)
		
		{
		
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter Number of Productions: ");
		int num = scanner.nextInt();
		scanner.nextLine(); // Consume newline
		System.out.println("Enter the grammar as A -> Aa / b:");
		for (int i = 0; i < num; i++)
		{
		String production = scanner.nextLine().trim();
		eliminateLeftRecursion(production);
		}
		scanner.close();
		}
		public static void eliminateLeftRecursion(String production)
		{
		String[] parts = production.split("->");
		char nonTerminal = parts[0].charAt(0);
		String[] choices = parts[1].split("/");
		System.out.println("GRAMMAR: " + production); // Checking for left recursion
		if (choices[0].startsWith("" + nonTerminal))
		{
		String beta = choices[0].substring(1); // Extracting beta from the first choice
		System.out.println(nonTerminal + " is left recursive.");
		// Printing reduced grammar
		System.out.println(nonTerminal + " -> " + choices[1].trim() + nonTerminal + "'");
		System.out.println(nonTerminal + "' -> " + beta + nonTerminal + "' / epsilon");
		}
		else
		{
		System.out.println(nonTerminal + " is not left recursive.");
		}
		}
		}
		TITLE: Implement Elimination of Left Recursion using JAVA programming.
		
		Sample Output:
		
		Enter Number of Productions: 1
		Enter the grammar as A -> Aa / b:
		E->E+T/T
		GRAMMAR: E->E+T/T
		E is left recursive.
		E -> TE'
		E' -> +TE' / epsilon
		
		4. Implementation of Finding a Left Factoring.
		
		import java.util.*;
		public class LeftFactoring
		{
		public static void main(String[] args)
		{
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number of productions:");
		int n = sc.nextInt();
		sc.nextLine();
		String[] productions = new String[n];
		System.out.println("Enter the productions:");
		for (int i = 0; i < n; i++) {
		productions[i] = sc.nextLine();
		}
		eliminateLeftFactoring(productions);
		}
		private static void eliminateLeftFactoring(String[] productions)
		{
		boolean leftFactored = false;
		for (String production : productions)
		{
		String[] parts = production.split("->");
		String lhs = parts[0].trim();
		String[] rhs = parts[1].split("\\|");
		String prefix = findCommonPrefix(rhs);
		if (!prefix.isEmpty()) {
		leftFactored = true;
		System.out.println(lhs + "->" + prefix + lhs + "'");
		List<String> newRhs = new ArrayList<>();
		for (String r : rhs) {
		if (r.startsWith(prefix)) {
		String suffix = r.substring(prefix.length()).trim();
		if (suffix.isEmpty()) {
		suffix = "";
		}
		newRhs.add(suffix);
		} else {
		newRhs.add(r);
		}
		}
		System.out.println(lhs + "'->" + String.join("|", newRhs));
		}
		}
		if (!leftFactored) {
		System.out.println("Given productions do not have left factoring");
		}
		TITLE: Implementation of Finding a Left Factoring using JAVA programming.
		
		}
		private static String findCommonPrefix(String[] rhs) {
		String prefix = rhs[0];
		for (int i = 1; i < rhs.length; i++) {
		while (rhs[i].indexOf(prefix) != 0) {
		prefix = prefix.substring(0, prefix.length() - 1);
		if (prefix.isEmpty()) {
		return "";
		}
		}
		}
		return prefix;
		}
		}
		
		Sample output:
		
		Enter the number of productions:
		1
		Enter the productions:
		S->Sa|Sb|Sc
		S->SS'
		S'->a|b|c



     	      6] import java.util.*;

			public class Main {
			    static Map<Character, List<String>> grammar = new HashMap<>();
			    static String input;
			    static int i = 0;
			
			    static boolean parse(char nonTerminal) {
			        int backtrack = i;
			        for (String prod : grammar.get(nonTerminal)) {
			            i = backtrack;
			            boolean success = true;
			            for (char symbol : prod.toCharArray()) {
			                if (symbol == '@') continue;
			                else if (Character.isUpperCase(symbol)) success &= parse(symbol);
			                else if (i < input.length() && input.charAt(i) == symbol) i++;
			                else { success = false; break; }
			            }
			            if (success) return true;
			        }
			        return false;
			    }
			       public static void main(String[] args) {
			        Scanner sc = new Scanner(System.in);
			        System.out.println("Enter number of productions:");
			        int n = sc.nextInt();
			        sc.nextLine();
			        System.out.println("Enter productions (Use '@' for epsilon, e.g., A->aA|@):");
			        for (int j = 0; j < n; j++) {
			            String[] rule = sc.nextLine().split("->");
			            grammar.put(rule[0].charAt(0), Arrays.asList(rule[1].split("\\|")));
			        }
			        System.out.println("Enter the string to check:");
			        input = sc.next() + "$";
			        System.out.println(parse('E') && i == input.length() - 1 ? "String is accepted" : "String is rejected");
			    }
			}
			
			output::
			
			Enter number of productions:
			5
			Enter productions (Use '@' for epsilon, e.g., A->aA|@):
			E->TA
			A->+TA|@
			T->FB
			B->*FB|@
			F->(E)|i
			Enter the string to check:
			i+i*i
			String is accepted
		7] import java.util.*;

	public class Shift_Reduce {
	    public static void main(String[] args) {
	        Scanner sc = new Scanner(System.in);

        System.out.print("No.of production : ");
        int n = sc.nextInt();
        sc.nextLine(); 
        String lhs[]=new String[n];
        String rhs[]=new String[n];

        System.out.println("Grammar : ");
        for (int i = 0; i < n; i++) {
            String[] p = sc.nextLine().split("->");
            lhs[i]=p[0];
            rhs[i]=p[1];
        }
        
        System.out.print("String : ");
        String inp = sc.nextLine();

        System.out.println("\nStack\tInputBuffer\tAction");
        String stk="";
        while (true) {
            char ch = inp.charAt(0);
            stk += ch;
            inp=inp.substring(1);
            System.out.println(stk + "\t\t" + inp+"\t\tShift " + ch);

            for (int j = 0; j < n; j++) {
                int idx = stk.indexOf(rhs[j]);
                if (idx != -1) {
                    stk = stk.substring(0, idx) + lhs[j];
                    System.out.println(stk+"\t\t"+inp+"\t\tReduce " + lhs[j] + "->" + rhs[j]);
                    j = -1; 
                }
            }

       if (stk.equals(lhs[0]) && inp.length()==0) {
                System.out.println("Accepted");
                break;
            }
            if (inp.length()==0) {
                System.out.println("Not Accepted");
                break;
            }
        }
    }
		}
		
		output:
		
		No.of production : 4
		Grammar : 
		E->E+E
		E->E*E
		E->(E( )
		E->i
		String : i*i+i
		
		Stack	InputBuffer	Action
		i		*i+i		Shift i
		E		*i+i		Reduce E->i
		E*		i+i		Shift *
		E*i		+i		Shift i
		E*E		+i		Reduce E->i
		E		+i		Reduce E->E*E
		E+		i		Shift +
		E+i				Shift i
		E+E				Reduce E->i
		E				Reduce E->E+E
		Accepted
			

		8] 
		import java.util.*;
		
		public class Operator_Parser {
		    public static void main(String[] args) {
		        Scanner sc = new Scanner(System.in);
		
		        System.out.print("No. of terminals: ");
		        int n = sc.nextInt();
		        sc.nextLine();
		
		        System.out.print("Terminals: ");
		        String t = sc.nextLine();
		
		        String[][] p = new String[n][n];
		
		        System.out.println("Precedence Table: ");
		        for (int i = 0; i < n; i++) {
		            for (int j = 0; j < n; j++) {
		                p[i][j] = sc.next();
		            }
		        }
		
		        System.out.println("OPERATOR PRECEDENCE TABLE:");
		        System.out.print("\t");
		        for (int i = 0; i < n; i++) {
		            System.out.print(t.charAt(i) + "\t");
		        }
		        System.out.println();
		        for (int i = 0; i < n; i++) {
		            System.out.print(t.charAt(i) + "\t");
		            for (int j = 0; j < n; j++) {
		                System.out.print(p[i][j] + "\t");
		            }
		            System.out.println();
		        }
		        
		        System.out.print("String : ");
		        String inp=sc.next()+"$";
		        String stk="$";
		        System.out.println("STACK\t\tINPUT\t\tACTION");
		        while(true){
		            String c1=stk.charAt(stk.length()-1)+"";
		            String c2=inp.charAt(0)+"";
		            if(c1.equals("E")) c1=stk.charAt(stk.length()-2)+"";
		            int i1=t.indexOf(c1);
		            int i2=t.indexOf(c2);
		            
		            if (i1 == -1 || i2 == -1) {
		                System.out.println("Rejected.");
		                break;
		            }
		            
		            if(p[i1][i2].equals("A")) {
		                System.out.println("Accepted.");
		                break;
		            }
		            
		            if(p[i1][i2].equals("<")){
		                stk+=c2;
		                inp=inp.substring(1);
		                System.out.println(stk+"\t\t"+inp+"\t\tSHIFT"+c2);
		            }else{
		                stk=stk.substring(0,stk.length()-1);
		                if(!c1.equals("i")) stk=stk.substring(0,stk.length()-2);
		                stk+="E";
		                System.out.println(stk+"\t\t"+inp+"\t\tREDUCE");
		            }
		        }
		    }
		}
		
		
		output:
		
		No. of terminals: 3
		Terminals: +i$
		Precedence Table: 
		> < >
		> < >
		< < A
		OPERATOR PRECEDENCE TABLE:
			+	i	$	
		+	>	<	>	
		i	>	<	>	
		$	<	<	A	
		String : i+i$
		STACK		INPUT		ACTION
		$i		+i$$		SHIFTi
		$E		+i$$		REDUCE
		$E+		i$$		SHIFT+
		$E+i		$$		SHIFTi
		$E+E		$$		REDUCE
		$E		$$		REDUCE
		Accepted.
\
     
