import java.util.Scanner;
class dowhile{
	public static void main(String[] args) {
		Scanner sa=new Scanner(System.in);
		System.out.println("Enter Emp Name:");
		String name=sa.nextLine();
		long tax=0;
		System.out.println("Enter Employee income:");
		long income=sa.nextInt();//50

		if(income<=250000){
			System.out.println("No Tax:");
		}
		else if(income>=250000&&income<=500000){
			tax=(income*10)/100;
			income=income-tax;
			System.out.println("Total Income Tax is amount after Exceeding:"+income);
		}
		else if(income>=500000&&income<=1000000){
			tax=(income*20/100);
			income=(income-tax)+30000;
			System.out.println("Total Income Tax is amount after Exceeding:"+income);
		}
		else{
			tax=(income*30/100);
			income=(income-tax)+50000;
			System.out.println("Total Income Tax is amount after Exceeding:"+income);
		}


		// if(units<=100){
		// 	bill=units*10;
		// }
		// else if(units<=200){//160
		// 	bill=(100*10)+(units-100)*15;// 100*10 ->1000+   60  1000
		// 	//160-100    ->60   100+60 ->160     1000+60*15
		// }
		// else if(units<=300){
		// 	bill=(100*10)+(100*15)+(units-200)*20;
		// }
		// else {
		// 	bill=(100*10)+(100*15)+(100*20)+(units-300)*25;
		// }
		// System.out.println("Total bill is:"+bill);

	}
}