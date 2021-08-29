package Practice;

import java.util.Scanner;

public class ReverseString {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		@SuppressWarnings("resource")
		Scanner in=new Scanner(System.in);
		String a=in.nextLine();
		for (int i=a.length()-1;i>=0;i--)
		{
			System.out.print(a.charAt(i));
		}
		
	}

}
