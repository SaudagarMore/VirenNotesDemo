/*
2d Array
------------------
*/
import java.util.Scanner;
class methodreturn{
	public static void main(String[] args) {
		Scanner sa=new Scanner(System.in);
		System.out.println("Enter The Size of Array:");
		int size=sa.nextInt();//10

		int arr[]=new int[size];//5
		int i;
		int sum=0;

		System.out.println("Enter Array Elemnts:");
		for(i=0;i<arr.length;i++){
			arr[i]=sa.nextInt();
		}

		int max=arr[0];
		int min=arr[0];
		for(i=0;i<arr.length;i++){
			if(arr[i]>max){
				max=arr[i];
			}else if(arr[i]<min){
				min=arr[i];
			}
		}
		 System.out.println("Maximun Number is:"+max);
		 System.out.println("Minimum number is:"+min);
		// int even=0;
		// int odd=0;

		// for(i=0;i<arr.length;i++){
		// 	if(arr[i]%2==0){
		// 		even++;//1
		// 	}
		// 	else{
		// 		odd++;//1
		// 	}
		// }
		// System.out.println("Total Even is:"+even);
		// System.out.println("Total Odd is:"+odd);

		// for(i=0;i<arr.length;i++){
		// 	sum=sum+arr[i];//12=12+12
		// }
		// System.out.println("Total Sum is:"+sum);
		// System.out.println("Toal Average is:"+(sum/arr.length));


		// boolean found=true;
		// System.out.println("Enter Number Which you want to find in array:");
		// int search=sa.nextInt();
		// for(i=0;i<arr.length;i++){
		// 	if(arr[i]==search){
		// 		System.out.println("Number is found on the "+i+"This Postion");
		// 		found=false;
		// 		break;
		// 	}
		// }
		// if(found==true){
		// 	System.out.println("Number not found into the array");
		// }
	}
}
