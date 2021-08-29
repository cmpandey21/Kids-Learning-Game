package Inheritance;

public class ChildClass extends ParentClass {
String colour = "Red";
	public void ParentVariable()
	{
		System.out.println(colour);
	}
	
	
	public void ParentVariableToTestsuperkeyword()
	{
		System.out.println(super.colour);
		//Use of Super key, if we want to use parent class value and dont want it to override use super keyword
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		ChildClass obj= new ChildClass();
		obj.ParentVariable();
		obj.Parentmethod();
		
		ParentClass obj1= new ChildClass();
		obj1.Parentmethod();
		obj1.ParentVariable();
		
	
		obj.ParentVariableToTestsuperkeyword();
	}

}
//Default: access method anywhere only in package
//public: valirable /method as public then you will have access across all the packages
//private: you can not access method/variable outside the class 
//protected : variable/method as proteced then you can access these in sub class (means the class which is inherting the properties) (this is for other packages)