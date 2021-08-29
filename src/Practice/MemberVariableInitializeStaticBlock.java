package Practice;
//Can we initialize member variables within static block
public class MemberVariableInitializeStaticBlock {

	 String name;
	static int age;
	
	static{
		MemberVariableInitializeStaticBlock e1=new MemberVariableInitializeStaticBlock();
	e1.name ="Mohan Pandey";	
		age=24;
		System.out.println("Name "+ e1.name+" and Age "+age);
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
