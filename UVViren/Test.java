
import java.util.Scanner;
class Test{
	public static void main(String[] args) {
		Scanner sa=new Scanner(System.in);
		System.out.println("Enter Any numbeR:");
		int no=sa.nextInt();

		System.out.println("Original value is:"+no);
		System.out.println("Right Shift Value:"+(no>>5));
    	System.out.println("left Shift Value:"+(no<<6));
//5<<5 ->5*2->10*2->20*2->40*2->80*2->160
	}
}