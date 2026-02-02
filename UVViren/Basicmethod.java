import java.util.Scanner;
class Basicmethod{
	public static void main(String[] args) {
		// int n;
		// int j;
		// int position;
		// int number;
		Scanner sa=new Scanner(System.in);
		Basicmethod.input(sa);

		// System.out.println("Enter The Size of Aray:");
		// n=sa.nextInt();
		// int data[]=new int[50];
		// for(j=0;j<n;j++){
		// 	System.out.println("Enter The Elements of Array:");
		// 	data[j]=sa.nextInt();
		// }
		// 		for(j=0;j<n;j++){
		// 	System.out.println("Before Insert data into the array:"+data[j]+" ");
		// }
		// System.out.println("Enter Position Where you Want To Insert Element:");
		// position=sa.nextInt();
		// System.out.println("Enter Value Which you Want To Add:");
		// number=sa.nextInt();
		// for(int k=n-1;k>=position-1;k--){
		// 	data[k+1]=data[k];
		// }
		// data[position-1]=number;
		// for(j=0;j<n;j++){
		// 	System.out.println("After Insert data into the array:"+data[j]+" ");
		// }
	}
	public static void input( Scanner sa){
		System.out.println("Enter The Value:");
		int ab=sa.nextInt();
		System.out.println(ab);
	}
}