import java.util.Scanner;
class switchpractise{
	public static void main(String[] args) {
		Scanner sa=new Scanner(System.in);
		System.out.println("Enter choice :");
		String choice=sa.next();
		switch(choice){
		case "ABC":
			System.out.println("Choice 1 match");
			break;			
		case "BCA":
			System.out.println("Second choice match");
			break;
		case "BCS":
    		System.out.println("Third choice match");
    		break;		
		case "MSC":
			System.out.println("Fourth choice match");
			break;
		default:{
			System.out.println("Any choice not match");
			}
		}
	}
}