package Inheritance;

public class Methodoverloading extends ParentClass{



//function overloading
//either argument count should be different or
//argument data type should be different


public void getData(int a)
{
System.out.println(a);
}
public void getData(String a)
{
System.out.println(a);
}
public void getData(int a,int b)
{
System.out.println(a + b);
}
public static void main(String[] args) {
//TODO Auto-generated method stub

Methodoverloading cl=new Methodoverloading();
cl.getData(2);
cl.getData("hello");
cl.getData(2,5);

}



}