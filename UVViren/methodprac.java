class methodprac{
	//static /non static
public void PersonDetails(int pid,String panme,int page,float expense,long income){
		if(pid==1001){
			System.out.println(pid+" "+panme+" "+page+" "+expense+" "+income);
		}
		else{
			System.out.println("Emp not matched");
		}
	}
public static void ShowArray(int ab[]){
	int j;
	System.out.println(" ");
	for(j=0;j<ab.length;j++){
		if(ab[j]%2!=0){
			System.out.print(ab[j]+" ");
		}
	}
}

	public static int Calci(int no1,int no2){
		return no1*no2;//   600 
		}
		public static String Myname(String Name){
			return Name;
		}

	public static void main(String[] args) {
		methodprac person=new methodprac();//object created...
		int nm[]={10,20,65,98,47,63};
		methodprac.ShowArray(nm);
//		System.out.println(methodprac.ShowArray(nm));

		person.PersonDetails(1001,"Viren More",27,10000.00f,24000);
//		int result=methodprac.Calci(20,30);
//		System.out.println(result);
		System.out.println(methodprac.Calci(30,50));
		System.out.println(methodprac.Myname("Viren More"));
	}
}
