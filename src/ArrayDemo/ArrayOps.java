package ArrayDemo;

import java.util.Scanner;

public class ArrayOps {
static Scanner scan= new Scanner(System.in);
	public static void main(String[] args) {
		// TODO Auto-generated method stub
int[] array= takeInput();
output(array);
	}

	public static int[] takeInput() {
		System.out.println("Size ?");
		int n=scan.nextInt();
		int[] arr= new int[n];
		for (int i=0;i<arr.length;i++)
		{
			System.out.println("Please enter the value for "+i+" index");
			arr[i]= scan.nextInt();
		}
		return arr;
	}
	
	public static void output(int[] arr) {
		for (int i=0;i<arr.length;i++)
		{
			System.out.println(arr[i]);
		}
	}
}
