import java.util.Scanner;
class Array{
	public static void main(String[] args) {
		Scanner sa=new Scanner(System.in);
		int arraysumavg[]=new int[7];
		int s;int sum=0;
		for(s=0;s<arraysumavg.length;s++){
			System.out.println("Enter Values:");
			arraysumavg[s]=sa.nextInt();
		}
		for(s=0;s<arraysumavg.length;s++){
			sum+=arraysumavg[s];
		}
		System.out.println("Total sum is:"+sum);//
		System.out.println("Total avg is:"+(sum/arraysumavg.length));//7
	}
}