import java.util.Scanner;
public class tarea{
	public static void main(String[] arg){
		Scanner sc=new Scanner(System.in);
		System.out.print("numero de ejercicio:");
		switch(sc.nextInt()){
			case 1:
				System.out.print("el numero n es: ");
				System.out.print(sumar(sc.nextInt()));
				break;
			case 2:
				System.out.print("el radio del circulo es: ");
				System.out.print(area(sc.nextFloat()));
				break;
			case 3:
				System.out.print("precio del objeto es: ");
				float[] sal=new float[2];
                                sal=pagar(sc.nextInt());
				System.out.print("descuento es: "+sal[0]+"\nprecio final: "+sal[1]);
				break;

		}

	}
	public static int sumar(int n){
		int v=(n*(n+1))/2;
		return v;
	}
	public static float area(float n){
		float v=(float)Math.PI*(n*n);
		return v;
	}
	public static float[] pagar(int n){
		float des=n-(n*0.2f);
		float n2=des+(des*0.15f);
		float[] re={des,n2};
		return re;
	}

}