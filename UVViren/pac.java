import java.util.Scanner;
class pac{
	public static void main(String[] args) {
		Scanner sa=new Scanner(System.in);
				System.out.println("Enter The Size of which you want to add into the array:");
		int size=sa.nextInt();
		int arr[]=new int[size];
		int i;
		for(i=0;i<size;i++){
			System.out.println("Enter The Array Elements:");
			arr[i]=sa.nextInt();
		}
		System.out.println("");
		pac.max_minarry(size,arr);
//		pac.Selection_sort(size,arr);
//		pac.insertArr(size,arr,sa);
//		pac.removeArr(size,arr,sa);
//		pac.BinarySearch(size,arr,sa);
	}
	public static void insertArr(int size,int arr[],Scanner ba){
		int i;
		for(i=0;i<size;i++){
			System.out.print(arr[i]+" ");
		}
		System.out.println(" ");
		System.out.println("Enter The Position Where You Want To Insert:");
		int position=ba.nextInt();

		System.out.println("Enter The Element Which you want to insert into the array:");
		int ele=ba.nextInt();
		

		for(i=size-1;i>=position-1;i--){
			arr[i+1]=arr[i];
		}
		arr[position-1]=ele;
		System.out.println("After Inserting Array:");
		for(i=0;i<=size;i++){
			System.out.print(arr[i]+" ");
		}
	}
	 public static void removeArr(int size,int arr[],Scanner sb){
	 	int i;
	 	for(i=0;i<size;i++){
	 		System.out.println(arr[i]+" ");
	 	}
	 	System.out.println("Enter The Position Wher You Want To Delete The Element:");
	 	int position=sb.nextInt();
	 	if(position>=size){
	 		System.out.println("You Cant Delete The Element:");
	 	}
	 	else{
	 		
	 		for(i=position-1;i<size-1;i++){// 4;4<9;i++
	 			arr[i]=arr[i+1];//
	 		}
	 	}
	 	System.out.println("After Removing Data:");
	 	for(i=0;i<size;i++){
	 		System.out.println(arr[i]);
	 	}
	 }
	 public static void BinarySearch(int size,int arr[],Scanner sb){
	 	System.out.println("Enter Number which you want to find into the array:");
	 	int value=sb.nextInt();
	 	boolean found=false;

	 	int first=0;
	 	int last=size;
	 	while(first<=last){
	 		int mid=(first+last)/2;
	 		if(arr[mid]==value){
	 			System.out.println("Yes Number is found");
	 			found=true;
	 			break;
	 		}
	 		else if(arr[mid]<value){
	 			first=mid+1;
	 		}
	 		else{
	 			last=mid-1;
	 		}
	 	}
	 	if(!found){
	 		System.out.println("Number not found into array:");
	 	}
	 }
	 public static void Selection_sort(int size,int arr[]){
	 	int i,j;
	 	for(i=0;i<size-1;i++){
	 	int minindex=i;
	 		for(j=i+1;j<size;j++){
	 			if(arr[j]<arr[minindex]){
	 				minindex=j;
	 			}
	 		}
	 		int temp=arr[minindex];
	 		arr[minindex]=arr[i];
	 		arr[i]=temp;
	 	}
	 	for(int m:arr){
	 		System.out.println(m);
	 	}
	 }
	 public static void max_minarry(int size,int arr[]){
	 	int i,j;
	 	int max=arr[0];
	 	int min=arr[0];

	 	for(i=0;i<size;i++){
		 		if(arr[i]>max){
		 			max=arr[i];
		 		}
		 		else if(arr[i]<min){
		 			min=arr[i];
		 		}
	 	}
	 	System.out.println(max);
	 	System.out.println(min);
	 }
}