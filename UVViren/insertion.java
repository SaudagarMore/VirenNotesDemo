import java.util.Scanner;
class insertion{
	public static void main(String[] args) {
		Scanner sa=new Scanner(System.in);
		//declaration of array
		//1)compile time
//		int data[]={10,20,30,40,50};
		//2)run time
		int score[]=new int[5];//10 20 30 40 50
		int i;

		// for( i=0;i<data.length;i++){
		// System.out.println(data[i]);			
		// }
		System.out.println("Enter Array Values:");
		for(i=0;i<score.length;i++){
			score[i]=sa.nextInt();
		}
		boolean found=true;
		System.out.println("Enter Number Which you want to Find into array:");
		int search=sa.nextInt();
		for(i=0;i<score.length;i++){
			if(score[i]==search){
				System.out.println("number is Found on This location:"+i);
				found=false;
				break;
			}
		}
		if(found==true){
			System.out.println("Number not Found:");
		}
		// int even=0;
		// int odd=0;
		// for(i=0;i<score.length;i++){
		// 	if(score[i]%2==0){
		// 		even++;
		// 	}
		// 	else{
		// 		odd++;
		// 	}
		// }
		// System.out.println("Total even is:"+even);
		// System.out.println("Total odd is:"+odd);

		// int sum=0;
		// //foreach loop
		// for(int j:score){
		// 	sum+=j;
		// 	System.out.print(j+" ");
		// }
		// System.out.println("Total sum is:"+sum);
		// System.out.println("Average is:"+sum/score.length);
	}
}