import java.util.Scanner;

class ejer2
{
  public static void main (String[] a){
    
    Scanner sc = new Scanner(System.in);

    System.out.println("base:");
    int b = sc.nextInt();
    System.out.println("altura:");
    int d = sc.nextInt();
    int c = d*b/2;
    System.out.println("area:" + c);
  }
}