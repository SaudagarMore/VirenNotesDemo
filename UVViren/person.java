import java.util.Scanner;
class person{
        public static void main(String[] args) {
            //create array
            Scanner sa=new Scanner(System.in);
            int n;
            System.out.println("Enter size of Array:");
            n=sa.nextInt();
            int d;
            boolean present=true;

            int array[]=new int[n];//

            for (d=0;d<array.length;d++){
                System.out.println("Enter Array Values:");
                array[d]=sa.nextInt();
            }
            System.out.println("Enter Number which want to find into the array:");
            int Number=sa.nextInt();

            for(d=0;d<array.length;d++){
                if(array[d]==Number){//
                    System.out.println(" number is present or found into the array");
                    present=false;
                }
            }
            if(present){
                System.out.println("Number not found into the array");
            }

 }
}