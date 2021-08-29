package CoreJava;

import java.util.Scanner;

public class ReverseString {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
@SuppressWarnings("resource")
Scanner input=new Scanner(System.in);
System.out.println("Enter the string you want to reverse");
String s=input.nextLine();
String t="";
System.out.println(s.length());
for(int i=s.length()-1;i>=0;i--)
{
t=t+s.charAt(i);
	}
System.out.println(t);
System.out.println(s);


}
}
