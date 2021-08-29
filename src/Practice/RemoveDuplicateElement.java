package Practice;

import java.util.Arrays;

public class RemoveDuplicateElement {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
int arr[] = {10,10,100,100,412,411,20,40,53,54};
Arrays.sort(arr);
int length=arr.length;
length= removeDuplicateElement(arr,length);
for(int i=0;i<length;i++)
{
	System.out.print(arr[i]+" ");
}
	}
	
	public static int removeDuplicateElement(int arr[],int n)
	{
		if(n==0 || n==1)
		{
		
	   return n;
		}
		
		int j=0;
		for(int i=0;i<n-1;i++)
		{
		
		if(arr[i]!=arr[i+1])
		{
	       arr[j++]=arr[i];
	     }
		}
		arr[j++]=arr[n-1];
		return j;
}
}