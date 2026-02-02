import java.util.Scanner;
class pracrist{
	public static void main(String[] args) {
		Scanner sa=new Scanner(System.in);
		int rev=0;
		System.out.println("Enter Any numbeR:");
		int no=sa.nextInt();
		while(no!=0){
			no=no/10;
			rev++;
		}
		System.out.println("Total digit is:"+rev);
	}
}