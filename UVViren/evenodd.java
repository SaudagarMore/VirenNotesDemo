import java.util.Scanner;
class evenodd{
	public void checkprime(int j){
		boolean flag=true;
		if(j<=1){
			flag=false;
		}
		else {
			for(int m=2;m<j;m++){
				if(j%m==0){
					flag=false;
					break;
				}
			}
			if(flag){
				System.out.println("Thsi is prime");
			}
			else{
				System.out.println("not prime");
			}
		}

	}
	public static void main(String[] args) {
		Scanner sa=new Scanner(System.in);
		evenodd even=new evenodd();
		even.checkprime(7);
		
		// System.out.println("Enter Any numbeR");
		// int no =sa.nextInt();
		// int even=0;
		// int odd=0;
		// int div=0;
		// int t=0;
		// for(int j=0;j<=no;j++){
		// 	t=j;
		// 	if(j%2==0){
		// 		even++;
		// 	}
		// 	else if(j%2!=0){
		// 		odd++;
		// 	}
		// 	if(t%5==0){
		// 		div++;
		// 	}
		// }
		// System.out.println("Total Even is:"+even);
		// System.out.println("Total odd is:"+odd);
		// System.out.println("Total divisile by 5 is:"+div);
	}
}