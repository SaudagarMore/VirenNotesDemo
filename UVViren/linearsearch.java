import java.util.Scanner;
import java.util.Arrays;
class linearsearch{
	public static void main(String[] args) {
		Scanner sa=new Scanner(System.in);
//		linearsearch.insert();
		linearsearch.insertarray();
//		linearsearch.removearr();
//		linearsearch.binarysearch();

	}
	public static void insert(){
		Scanner sa=new Scanner(System.in);
		int data[]=new int[50];
		System.out.println("Enter The Size of Array:");
		int size=sa.nextInt();
		int i;
		for(i=0;i<size;i++){
			System.out.println("Enter Any Number:");
			data[i]=sa.nextInt();
		}
		System.out.println("Enter The position where you want to insert:");
		int position=sa.nextInt();
		System.out.println("Enter The value which you want insert:");
		int value=sa.nextInt();
		for(i=size-1;i>=position-1;i--){
			data[i+1]=data[i];
		}
		data[position-1]=value;
		for(i=0;i<=size;i++){
			System.out.print(data[i]+" ");
		}
	}
	public static void insertarray(){
		Scanner sa=new Scanner(System.in);
		System.out.println("Enter The Size of Array:");
		int size=sa.nextInt();
		int arr[]=new int[size+1];
		int i;
		System.out.println("Enter Array Elements:");
		for(i=0;i<size;i++){
			arr[i]=sa.nextInt();
		}
		System.out.println("Enter The New Number:");
		int Number=sa.nextInt();
		arr[size]=Number;
		for(i=0;i<=size;i++){
			System.out.print(arr[i]+" ");
		}
	}
	public static void removearr(){
		Scanner sa=new Scanner(System.in);
		System.out.println("Enter The Size of Array:");
		int size=sa.nextInt();//5
		int arr[]=new int[size];
		int i;
		System.out.println("Enter Array Elements:");
		for(i=0;i<size;i++){
			arr[i]=sa.nextInt();//5
		}
		System.out.println("Enter The position which you want to remove:");
		int position1=sa.nextInt();
		if(position1>=size+1){//7>
			System.out.println("position is max than size");
		}
		else{
			for(i=position1-1;i<size-1;i++){
				arr[i]=arr[i+1];
			}
		}
		for(i=0;i<size;i++){
			System.out.println(arr[i]+" ");
		}
	}
	public static void binarysearch(){
		Scanner sa=new Scanner(System.in);
		System.out.println("Enter The Size of Array:");
		int size=sa.nextInt();//5
		int arr[]=new int[size];
		int i;
		System.out.println("Enter Array Elements:");
		for(i=0;i<size;i++){
			arr[i]=sa.nextInt();//5
		}
		System.out.println("Enter The Number which you want to search:");
		int number=sa.nextInt();
		Arrays.sort(arr);
		int low=0;
		int high=size-1;
		boolean found=false;
		while(low<=high){
			int mid=(low+high)/2;
			if(arr[mid]==number){
				System.out.println("number found");
				found=true;
				break;
			}
			else if(arr[mid]<number){
				low=mid+1;
			}
			else{
				high=mid-1;
			}
		}
		if(!found){
			System.out.println("number not found");
		}
	}
}