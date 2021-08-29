package Practice;

import java.util.Scanner;

public class SwapInteger {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a;
		int b;
		
		@SuppressWarnings("resource")
		Scanner in=new Scanner(System.in);
        System.out.println("Enter Value for First Number");
		a=in.nextInt();
		System.out.println("Enter Value for Second Number");
		b=in.nextInt();
		a=a+b;
	    b=a-b;
	    a=a-b;
	    System.out.println("Value of First Number after Swap"+" "+a+" "+"Value of Second Number after Swap "+b);
				
	}

}
