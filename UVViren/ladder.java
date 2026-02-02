import java.util.Scanner;
class ladder{
	public static void main(String[] args) {

		Scanner sa=new Scanner(System.in);
		System.out.println("Enter Three Nubers:");
		int amount=sa.nextInt();
		int discount;
		if(amount<=9999){
			System.out.println("amount is less ");
		}
		else if(amount>=10000&&amount<=19999){
			discount=(amount*3/100);
			amount=amount-discount;
			System.out.println("Totoal Discount is:"+amount);			
		}
				else if(amount>=20000&&amount<=49999){
			discount=(amount*5/100);
			amount=amount-discount;		
			System.out.println("Totoal Discount is:"+amount);
					}
				else if(amount>=50000&&amount<=99999){
			discount=(amount*10/100);
			amount=amount-discount;		
			System.out.println("Totoal Discount is:"+amount);
		}
		else{
			System.out.println("Discount is not availabel");
		}
	}
}