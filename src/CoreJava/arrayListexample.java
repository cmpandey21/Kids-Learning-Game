package CoreJava;

import java.util.ArrayList;

public class arrayListexample {
//Can accept duplicate values
// ArrayList, LinkedList, Vector - implementing list interface
//array have fixed size where as arrayList can grow dynamically 
//You can access and insert any value in any index
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		ArrayList<String> obj= new ArrayList<String>();
		obj.add("Mohan");
		System.out.println(obj);
		obj.add(1,"Pandey");
		obj.add(2,"Employee");

		obj.remove("Employee");
		System.out.println(obj);
		System.out.println(obj.get(1));
		System.out.println(obj.contains("Employee"));
		System.out.println(obj.indexOf("Mohan"));
		System.out.println(obj.isEmpty());
		System.out.println(obj.size());
		
	}

}
