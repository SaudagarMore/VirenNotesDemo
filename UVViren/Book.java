//package imported
import java.util.Scanner;
//book calss declare
class Book{
	//main method
	public static void main(String[] args) {
		//bood variables
		int bid;
		String Bname;
		String Bauthor;
		double bprice;
		int bedition;
		int bproductionyear;
		String Bcompnayname;
		boolean isjavabook;
		//Scanner class
		Scanner sc=new Scanner(System.in);
		//input logic
		System.out.println("Enter Book Id:");
		bid=sc.nextInt();
		sc.nextLine();
		
		System.out.println("Enter Book Name:");
		Bname=sc.nextLine();
		
		System.out.println("Enter Book Price:");
		bprice=sc.nextFloat();
		sc.nextLine();

		System.out.println("Enter Book Author:");
		Bauthor=sc.nextLine();
		
		System.out.println("Enter Book Ediiton:");
		bedition=sc.nextInt();

		System.out.println("Enter Book prodcution year:");
		bproductionyear=sc.nextInt();
		sc.nextLine();

		System.out.println("Enter Book  Compnay:");
		Bcompnayname=sc.nextLine();

		System.out.println("is this java book:");
		isjavabook=sc.nextBoolean();

		//book display
		System.out.println("Book Id is:"+bid);
		System.out.println("Book Name:"+Bname);
		System.out.println("Book Author:"+Bauthor);
		System.out.println("book Price is:"+bprice);
		System.out.println(" Book Ediiton:"+bedition);
		System.out.println("Book prodcution year:"+bproductionyear);
		System.out.println(" Book  Compnay:"+Bcompnayname);
		System.out.println("is this java book:"+isjavabook);

	}
}

product
--------------------
pid  ->int/string
pname ->string 
pcost ->int/float
pdiscount ->float
psellername ->string
productiondate->date/time string long/double /- /
pamount  ->long/double
totalproductsell ->double /long
productexpiry ->string
aboutproduct ->string
-----------------------------------------------
operators
------------------

















