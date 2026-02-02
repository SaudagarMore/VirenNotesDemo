import java.util.Scanner;
class Decision1{
	public static void main(String[] args) {
		Scanner sa=new Scanner(System.in);
		System.out.println("Enter Three Nubers:");
		int no1=sa.nextInt();
		int no2=sa.nextInt();
		int no3=sa.nextInt();

		if(no1<=30){//99<=30 
			if(no2<=30){//6<=30
				if(no3<=30){
					System.out.println("all numbers less than 30");
				}
				else{
					System.out.println("third number is less than 30");
				}
			}
			else{
					System.out.println("Second number is less than 30");
					}
		}
		else{
								System.out.println("first number is less than 30");
		}
	}
}