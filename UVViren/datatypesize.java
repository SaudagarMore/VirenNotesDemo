/*
1)size ->bit 8 32 64 16

*/
import java.util.Scanner;
class datatypesize{
	public static void main(String[] args) {
		Scanner sa=new Scanner(System.in);
		System.out.println("Enter First Value:");
		int num1=sa.nextInt();
		System.out.println("Enter Second Value:");
		int num2=sa.nextInt();
		int result=num1-num2;
		System.out.println("The Addition is:"+(num1+num2));
		System.out.println("The Substation is:"+result);
		System.out.println("The Multiplicaion is:"+num1*num2);
		System.out.println("The Divison is:"+num1/num2);//100/3 -> 33 
		System.out.println("The reminder is:"+num1%num2);




	// 	System.out.println("The Bit size is:"+Integer.SIZE);

	// 	System.out.println("The Byte size is:"+Integer.BYTES);
	// System.out.println("The Float size is:"+Float.SIZE);
	// System.out.println("The Doulbe size is:"+Double.SIZE);
	}
}