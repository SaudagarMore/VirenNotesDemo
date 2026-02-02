import java.util.Scanner;
class Array2d{
	public static void main(String[] args) {
		int st[][]={{10,20,30,40},{50,60,70,80}};

		int i,j;
		for(i=0;i<2;i++){
			for(j=0;j<4;j++){
				System.out.print(st[i][j]+" ");
			}
			System.out.println("");
		}
		int  ab[][]=new int[2][3];
		Scanner sa=new Scanner(System.in);
		for(i=0;i<2;i++){
			for(j=0;j<3;j++){
				System.out.println("Enter Array Values:");
				ab[i][j]=sa.nextInt();
			}
		}
		for(i=0;i<2;i++){
			for(j=0;j<3;j++){
				System.out.print(ab[i][j]+" ");
			}
			System.out.println("");
		}
		System.out.println("Enter Number which you want to find:");
		int search=sa.nextInt();
		boolean found=true;
		for(i=0;i<2;i++){
			for(j=0;j<3;j++){
				if(ab[i][j]==search){
					System.out.println("Number Found the location is:"+i+" "+j);
					found=false; break;
				}
			}
		}
		if(found==true){System.out.print("Number not Found");}
	}
}