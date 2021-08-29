package Practice;

public class ReverseInteger {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
 int n=420;
 
 ReverseInteger in=new ReverseInteger();
 
System.out.println("Input value: "+ n);
System.out.println("Inverted Input value: "+ in.invertedNumber(n));
	}




public int invertedNumber(int n)
{
	int reverse=0;
	while(n!=0)
	{
	reverse=(reverse*10)+(n%10);
	n=n/10;
	}
	
	return reverse;
	}

}