package Practice;
//Pass null argument with method overloading of String and Object types
public class NullArguement {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Test(null);
	}
	
	public static void Test(Object O)
	{
		System.out.println("Object Arguement");
	}
	
	public static void Test(String S)
	{
		System.out.println("String Arguement");
	}

}
