package CoreJava;

import java.text.SimpleDateFormat;
import java.util.Date;

public class DateDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Date obj= new Date();
		SimpleDateFormat ob= new SimpleDateFormat("M/d/yyyy");
		System.out.println(obj.toString());
		System.out.println(ob.format(obj));
	}

}
