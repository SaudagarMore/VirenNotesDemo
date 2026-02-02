/*
Employee
----------------
*/
import java.util.Scanner;
class input{
public static void main(String arg[]){
Scanner sa=new Scanner(System.in);
int eid;
String Ename;
long empsal;
short eage;
double empexp;
boolean isemp;

System.out.println("Enter Emp ID:");
eid=sa.nextInt();
//sa.nextLine();
System.out.println("Enter Name:");
Ename=sa.nextLine();//Viren More
System.out.println("Ente Employee Salary:");
empsal=sa.nextLong();
System.out.println("Ente Emp Age:");
eage=sa.nextShort();
System.out.println("Ente Employee Expenses:");
empexp=sa.nextDouble();
System.out.println("Is This Employee of Developer Role.?");
isemp=sa.nextBoolean();

System.out.println("----------------------------------------------------");
System.out.println("The Emp id is:"+eid);
System.out.println("The Emp Name is"+Ename);
System.out.println("The Emp Salary is:"+empsal);
System.out.println("The Emp Age is:"+eage);
System.out.println("The Emp Expenses is:"+empexp);
System.out.println("The Emp Devloper is or not:+isemp");

}
}

-------------------------------------------------
Book
-----------------------
bid->
Bname
Bprice
Bedition
Bauthor
Bcompany
BisJava
BProductionyear

Scanner ->
sublime installing
----------------------------
operators
----------------



























