import java.util.Scanner;
import java.util.Arrays;
class methodsdemo{
	public static void main(String[] args) {
		 Scanner sa=new Scanner(System.in);
		// int num[]=new int[6];
		// int i;
		// int j=0;
		// for(i=0;i<6;i++){
		// 	System.out.println("Enter Number:"+i);
		// 	num[i]=sa.nextInt();
		// }
//		methodsdemo.duplicate(num);
//		methodsdemo.maxArr(num);
//		methodsdemo.allEven(num);
//		methodsdemo.binarysearch(num,sa);
		methodsdemo.AddArray(sa);

		// System.out.println("Enter Number which you want find:");
		// int number=sa.nextInt();
		// for(i=0;i<6;i++){
		// 	if(num[i]==number){
		// 		System.out.println("Number found index is:"+i);
		// 		j=1;
		// 		break;
		// 	}
		// }
		// if(j==0){
		// 	System.out.println("number not found into the array");
		// }
	}
	public static void duplicate(int num[]){
		int i;
		int j;
		boolean found=true;
		for(i=0;i<6;i++){
			for(j=i+1;j<6;j++){
				if(num[i]==num[j]){
					System.out.println("Matched:   "+num[i]+" "+num[j]);
					found=false;
					break;
				}
			}
		}
		if(found){
			System.out.println("duplicate Number not found in array");
		}

	}
	public static void maxArr(int num[]){
		int max=num[0];
		int i;

		for(i=0;i<6;i++){
			if(num[i]>max){
				max=num[i];
			}
		}
		System.out.println("Maximum number is:"+max);

	}
	public static void allEven(int num[]){
		int i;
		for(i=0;i<6;i++){
			if(num[i]%2==0){
				System.out.println(num[i]);
			}
		}

	}
	public static void binarysearch(int num[],Scanner sa){
		int i;
		System.out.println("Enter Number which you want to find:");
		int find=sa.nextInt();
		Arrays.sort(num);
		int start=0;
		int last=num.length;
		boolean found=true;
		while(start<=last){
			int mid=(start+last)/2;
			if(num[mid]==find){
				System.out.println("Number found:");
				found=false;
				break;
			}
			else if(num[mid]<find){
				start=mid+1;
			}
			else{
				last=mid-1;
			}
		}
		if(!found){
			System.out.println("number not found");
		}
	}
	public static void AddArray(Scanner sa){
		int num[]=new int[20];		

		System.out.println("Enter Array Size which you want to add:");
		int size=sa.nextInt();
		int i;
		System.out.println("Enter Array Elements:");
		for(i=0;i<size;i++){
			num[i]=sa.nextInt();
		}
		System.out.println("Before Inserting:");
		for(i=0;i<size;i++){
			System.out.print(num[i]+" ");
		}

		System.out.println("Enter Number which you want to insert:");
		int num1=sa.nextInt();
		System.out.println("Enter The Array Position which you want to insert:");
		int position=sa.nextInt();
		for(i=size-1;i>=position-1;i--){
			num[i+1]=num[i]; 
		}
		num[position-1]=num1;
		System.out.println("After Adding Values:");
		for(i=0;i<=size;i++){
			System.out.print(num[i]+" ");
		}
	}
}