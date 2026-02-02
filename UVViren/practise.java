//count digit in the number
import java.util.Scanner;
class practise{
	public static void power(int no1,int no2){
		Scanner sa=new Scanner(System.in);
		// System.out.println("Enter any numbeR:");
		// int num=sa.nextInt();
		// practise pa=new practise();
//		pa.table(num);

		int j=1;
		int result=1;
		while(j<=no2){//   7<=6->true
			result=result*no1;//9=3*3//729
			j++;//2
		}
		System.out.println("The poower is:"+result);
	}
	public static void main(String[] args) {
		Scanner sa=new Scanner(System.in);
//		practise.power(3,6);
//		practise.swap(20,40);
		practise.calci(1);
	}
	public static void swap(int a,int b){
			System.out.println("Before swap:"+a+" "+b);
		int t=a;
		a=b;
		b=t;
		System.out.println("aFter swap:"+a+" "+b);
	}
	public void table(int no){
		if(no>=20&&no<=50&&no%5==0){
			for(int j=1;j<=10;j++){
				System.out.println(no*j);
			}
		}
	}	
	public static void calci(int m){
		int sum=0;
		do{
			sum+=m;
			m++;
		}while(m<=10);
		System.out.println("The Sum is:"+sum);
	}
}
/*
---------------
 2->
 3 ->4
 3*3*3*3 ->
 9*3*3
 27*3
 81
 3*4 ->81
*/