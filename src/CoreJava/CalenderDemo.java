package CoreJava;

import java.text.SimpleDateFormat;
import java.util.Calendar;

public class CalenderDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Calendar cal=Calendar.getInstance();
		SimpleDateFormat ob= new SimpleDateFormat("M/d/yyyy");
		System.out.println(ob.format(cal.getTime()));
		System.out.println(cal.get(Calendar.DAY_OF_MONTH));

	}

}
