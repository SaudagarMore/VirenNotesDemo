//check number is divisible by 5 or not
import java.util.Scanner;
class decision{
	public static void main(String[] args) {
		Scanner sa=new Scanner(System.in);
		 System.out.println("Enter First Number:");
		 int no=sa.nextInt();
		 System.out.println("Enter Second number:");
		 int no1=sa.nextInt();
		 System.out.println("Enter Third number: ");
		 int no2=sa.nextInt();

		 if(no>25){//false
		 	if(no1>25){//true
		 		if(no2>25)//true
		 		{
		 			System.out.println("Three number is max than 25");
		 		}
		 		else{
		 			System.out.println("Third is not max than 25");
		 		}
		 	}
		 	else{
		 		System.out.println("second number is not max than 25");
		 	}
		 }
		 else{
		 	System.out.println("First is not max than 25");
		 }

		// int t=no%5;
		// if(t==0){//20
		// 	System.out.println("Divisible by 5");
		// }
		// else
		// {
		// 	System.out.println("Not Divisible by 5");
		// }
	}
}