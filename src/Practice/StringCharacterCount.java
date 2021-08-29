package Practice;

public class StringCharacterCount {  
	
	
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
String S1="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrtuvwxyz";
String S2="Pandey";
int[] result = new int[26];
for(int i=0;i<S1.length() || i < S2.length();i++)
{         
	
	     if(i<S1.length()) {
	  if(S1.charAt(i)>='a' && S1.charAt(i)<='z')
       result[S1.charAt(i)-'a']++;   
	  
	  else if(S1.charAt(i)>='A' && S1.charAt(i)<='Z') {
		  result[S1.charAt(i)-'A']++;
	  }   
	  }    
	     
	     if(i<S2.length()) {
	   	  if(S2.charAt(i)>='a' && S2.charAt(i)<='z')
	          result[S2.charAt(i)-'a']++;   
	   	  
	   	  else if(S2.charAt(i)>='A' && S2.charAt(i)<='Z') {
	   		  result[S2.charAt(i)-'A']++;
	   	  } 
	   	  }  
	    
	    
    
}
		
for(int i=0;i<26;i++)
{
	if(result[i]!=0)
	{   
		char c = (char)('a'+i);
		 
		System.out.println(c + " "+ result[i]);
	}
}
	}

}
