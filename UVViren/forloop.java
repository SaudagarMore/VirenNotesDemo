import java.util.Scanner;
class forloop{
	public static void main(String[] args) {
		forloop.checkpalindrome(121);
		forloop.perfect(6);

	}
	public static void checkpalindrome(int n){
		int rev=0;
		int copy=n;
		if(n>0){
			while(n>0){
			rev=rev*10+(n%10);
			n/=10;
		}
		System.out.println(rev);
		if(rev==copy){
			System.out.println("palindrome");
		}
		else{
			System.out.println("not palindrome");
		}

		}
				else{
			System.out.println("invlaid number");
		}
	}
	public static void perfect(int num){
		int sum=0;
		int j=1;
		for(int m=1;m<num;m++){
					System.out.print(m+"             ");
			if(num%m==0){
				System.out.println("Divisior is:"+m);
				sum+=m;
			}
		}
			if(sum==num){
				System.out.println("Yes It is perfect number");
			}
			else{
				System.out.println("no it is not perfect number");
	}
}
}