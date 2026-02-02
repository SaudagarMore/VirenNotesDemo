/*
vowels ->
*/
import java.util.Scanner;
class vowels{
	public static void main(String[] args) {
		Scanner sa=new Scanner(System.in);	
		System.out.println("Enter Any Character");
		String vowel=sa.next();
		switch(vowel){
		case "A":
			System.out.println("This is Vowel");
			break;
		case "E":
			System.out.println("This is Vowel");
			break;
		case "I":
			System.out.println("This is Vowel");
			break;
		case "o":
			System.out.println("This is Vowel");
			break;
		case "U":
			System.out.println("This is Vowel");
			break;
		default:
			System.out.println("This is Constant");
		}
	}
}