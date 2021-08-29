package Practice;

public class StaticBlock {
	
//Static block executes before main method

	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
System.out.println("This is main method");
//Calling Test method without creating any object
Test();

//Once the object is created for StaticBlockWithoutMain class static block will be loaded
StaticBlockWithoutMain o=new StaticBlockWithoutMain();
System.out.println(StaticBlockWithoutMain.age); //accessing the static variable of StaticBlockWithoutMain class
	}
	
	
static {
	System.out.println("Static block 1");
	
}

static {
	System.out.println("Static block 2");
	

}
//How you can run java program without making any object
public static void Test()
{
System.out.println("Test method using static keyword");
}
}