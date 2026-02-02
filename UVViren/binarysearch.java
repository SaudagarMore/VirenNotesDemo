import java.util.Scanner;
class binarysearch{
	public static void main(String[] args) {
				Scanner sa=new Scanner(System.in);
		int arry[]=new int[50];
		int i;
		int low=0;
		boolean found=false;

		System.out.println("Enter The Size of array:");
		int size=sa.nextInt();
		int high=size-1;
		for(i=0;i<size;i++){
		arry[i]=sa.nextInt();
			}
			System.out.println("Enter Value Which you want to find:");
			int value=sa.nextInt();

			while(low<=high){
				int mid=(low+high)/2;
				if(arry[mid]==value){
					System.out.println("Value Found");
					found=true;
					break;
				}
				else if(arry[mid]<=value){
					low=mid+1;
				}
				else{
					high=low-1;
				}
			}
			if(!found){
				System.out.println("not found");
			}

	}
}