import java.util.Scanner;
class secondpage{
	public static void main(String[] args) {
		secondpage.findlargest();
//		secondpage.duplicatecheck();
//		secondpage.selectionsort();
	}
	public static void countdata(){
				Scanner sa=new Scanner(System.in);
		System.out.println("Enter The Size of Array:");
		int size=sa.nextInt();//
		int ab[]=new int[size];
		int i;int count=0;
		for(i=0;i<size;i++){//0;0<6;0++
			System.out.println("Enter Array Values:");
			ab[i]=sa.nextInt();
		}
		System.out.println("Enter The Number which you want to found:");
		int num=sa.nextInt();
		for(i=0;i<size;i++){
			if(ab[i]==num){
				count++;
			}
		}
		System.out.println("Total Number occured is:"+count);
	}
	public static void findlargest(){
		Scanner sa=new Scanner(System.in);
		System.out.println("Enter The Size of Array:");
		int size=sa.nextInt();//
		int ab[]=new int[size];
		int i;
		for(i=0;i<size;i++){//0;0<6;0++
			System.out.println("Enter Array Values:");
			ab[i]=sa.nextInt();
		}
		int max=ab[0];
		int min=ab[0];
		for(i=0;i<ab.length;i++){
			if(ab[i]>max){
				max=ab[i];
			}
			else if(ab[i]<min){
				min=ab[i];
			}
		}
		System.out.println(max);
		System.out.println(min);
	}
	public static void duplicatecheck(){
		Scanner sa=new Scanner(System.in);
		System.out.println("Enter The Size of Array:");
		int size=sa.nextInt();//
		int ab[]=new int[size];
		int i;
		int j;
		boolean found=false;
		int count=0;
		for(i=0;i<size;i++){//0;0<6;0++
			System.out.println("Enter Array Values:");
			ab[i]=sa.nextInt();
		}
		for(i=0;i<size;i++){
			for(j=i+1;j<size;j++){
				if(ab[i]==ab[j]){
					System.out.println("yes duplicate element :");
					found=true;
					break;
				}
			}
		}
		if(!found){
			System.out.println("Duplicate value not found in array");
		}
	}	
	public static void selectionsort(){
		Scanner sa=new Scanner(System.in);
		System.out.println("Enter The Size of Array:");
		int size=sa.nextInt();//
		int ab[]=new int[size];
		int i; int j;
		int minindex=0;
		for(i=0;i<size;i++){//0;0<6;0++
			System.out.println("Enter Array Values:");
			ab[i]=sa.nextInt();
		}
		for(i=0;i<size;i++){//5 6 9 8
			minindex=i; // 9
			for(j=i+1;j<size;j++){//
				if(ab[j]<ab[minindex]){ //8<9 
					minindex=j; //
				}
			}
			int temp=ab[minindex];
			ab[minindex]=ab[i];
			ab[i]=temp;
		}
		System.out.println("--------------------------");
		for(i=0;i<size;i++){
			System.out.println(ab[i]);
		}
	}
}