import java.util.Scanner;
class StringPractical{
	public static void main(String[] args) {
//		String ab;///STring declaration
		//initialization
		// String ab1="Java is high level programming language";
		// String str=new String("Spring Boot");
		// String sb=new String(ab1);

		// String st=sb;//
		// String mn=" ";//empty //null
		// String pl=null;// 

		
		// System.out.println(ab1);
		// System.out.println(str);
		// System.out.println(sb);
		// System.out.println(st);
		Scanner sa=new Scanner(System.in);
		String sb;
//		sa.nextLine();
		// System.out.println("Enter Any String:");
		// sb=sa.nextLine();
//1)		//charAt()    ->
		 int i;
		// for(i=0;i<sb.length();i++){
		// 	System.out.println(i+"index character is:"+sb.charAt(i));
		// }
//2)     length() 
//		System.out.println(sb.length());


//3)  		//getBytes()

		String ds="C CPP Java PHP";		

		// byte []bt=ds.getBytes();// php
		// for(i=0;i<bt.length;i++){
		// 	System.out.print(bt[i]+" ");
		// }
//4 contains()
//	System.out.println(ds.contains("Javascript"));
	//equals()    /isequalignorecase()
// 	String h1="cpp";
// 	String h2="cpp";//P p
// //	System.out.println(h1.equals(h2));//cpp ==react
// //5 isEmpty
// 	String st="Java React Spring ";
// 	System.out.println(st.isEmpty());

// //6 replace 
// 	String st1="Java React Spring angular ";
// 	System.out.println(st1);
// 	System.out.println(st1.replace('a','h'));
// //trim()

// 	String sa1="                      Python                 ";
// 	System.out.println(sa1.length());
// 	String sa2=sa1.trim();
// 	System.out.println("After Removing White Spaces:"+sa2.length());
//Substring()
	// String n1="Python is high level programming langauge";
	// String n2="Java supports to oops";

	// System.out.println(n1.length());
	// System.out.println(n1.substring(25));
	// System.out.println(n2.substring(5,21));
//    whitepsace,commas,colon	
	// String data="JAva Python Php C CPP";
	// String rt[]=data.split(" ");// Java,python,php,c,cpp

	// for (String m : rt){
	// 	System.out.println(m);
	// }
//	System.out.println(rt);

	//System.out.println(data.split(","));

// String p="JAVA";
// String k="python";
// System.out.println(p.toLowerCase());
// System.out.println(k.toUpperCase());
//int indexOf(int ch)
//String sd="Hibernate is JAva Framework";
// System.out.println(sd.indexOf("a"));//
//String indexOf()
// String kl="JAva";
// System.out.println(sd.indexOf(kl));

//int indexOf(String substring, int fromIndex)
// String pa="is";
// System.out.println(sd.indexOf("is",5));
String d1="HTML";
String d2="HTml";
// if(d1.equals(d2)){
// 	System.out.println("Both Are Equals");
// }
// else{
// 	System.out.println("Both Are Not Equals");
// }
// if(d1.equalsIgnoreCase(d2)){
// 	System.out.println("Both Are Equals");
// }
// else{
// 	System.out.println("Both Are Not Equals");
// }

		String s1 = new String("hello");//101
		String s2 = new String("hello");//102

		String s3="hello";
		String s4=s3;
		if(s4==s3){
			System.out.println("same location");
		}
		else {
			System.out.println("different location");
		}  } 

}