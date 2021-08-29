package demopack;

public class ChildEmirates extends ParentAirCraft {
	
	public void bodycolour()
	{
		
		System.out.println("Body colour is red");
	}

	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		ChildEmirates obj= new ChildEmirates();
		obj.Engine();
		obj.SafetyGuidelines();
		obj.bodycolour();

	}

}
