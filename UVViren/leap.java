/*

*/
import java.util.Scanner;
class leap{
	public static void main(String[] args) {
		Scanner sa=new Scanner(System.in);
		System.out.println("Enter Any Year:");
		int year=sa.nextInt();

		// if((year*100)%4==0){
		//  	System.out.println("this is leap year:");

		// }
		// else{
		//  	System.out.println("this is not leap year:");

		// }
		
		if(year%4==0){
			System.out.println("this is leap year:");
		}
		else{
			System.out.println("This is not leap year");
		}

	}
}