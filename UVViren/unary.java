import java.util.Scanner;
class unary{
	public static void main(String[] args) {
		Scanner sa=new Scanner(System.in);
		// int a=10;
		// int b=a--;//
		int a=20;
		int c=a--;
		int d=++a;
		int m1=++d;
		int z=--c;
		int s=a++;
		int k=--m1;

		System.out.println(a);
		System.out.println(c);
		System.out.println(d);
		System.out.println(m1);
		System.out.println(z);
		System.out.println(s);
		System.out.println(k);

	}
}