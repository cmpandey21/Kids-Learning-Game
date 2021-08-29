package CoreJava;

public class JavaClass {
static int a = 21;

public void getdata()
{
	System.out.println("I am inside the getdata method");
}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.print("hi");
		System.out.println(", my name is Mohan");
		System.out.println(a);
//objects are instances/references of a class
		JavaClass fn=new JavaClass();
		fn.getdata();
		SecondClass Sn=new SecondClass();
		Sn.setData();
	}

}
