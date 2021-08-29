package Practice;

public class PrintNumberWithoutUsingLoop {
//Print 1 to 100 Without Using for/while/do-while Loop in Code
	public static void main(String[] args) {
		// TODO Auto-generated method stub
PrintNumber(1,100);
	}
	
	public static void PrintNumber(int StartNum,int EndNum)
	{
		if(StartNum<=EndNum)
		{
			System.out.println(StartNum);
			StartNum++;
			PrintNumber(StartNum,EndNum);
		}
		
	}

}
