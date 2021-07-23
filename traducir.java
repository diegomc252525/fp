import java.util.Scanner;


public class traducir{

Scanner sc=new Scanner(System.in);
public static void main(String []args){
	Scanner sc=new Scanner(System.in);
	System.out.println("numero de problema");
  	tarea13 d= new tarea13();
	switch(sc.nextInt()){
		case 1:d.fun1();break;
		case 2:d.fun2();break;
		case 3:d.fun3();break;
		case 4:d.fun4();break;
	}
}



void fun1(){
	int[][] matriz=new int[20][20];
	int dim,i,j,db,item;

	System.out.print("\nINGRESAR DIMENSION DE LA MATRIZ : ");
	dim = sc.nextInt();
	System.out.print("\nIngresar Direccionamiento Base: "); 
	db  = sc.nextInt();
	for(i=0;i<dim;i++)
	{
		for(j=0;j<dim;j++)
		{
			item=db+(i+j)*(i+j+1)/2 + i; 
			matriz[i][j]=item;
		}
	}

	System.out.print("\nLECTURA DE ASIGNACION DE MATRIZ\n");
	for(i=0;i<dim;i++)
		{
			for(j=0;j<dim;j++)
			{
				if(j<dim-i)
					System.out.print("\t"+matriz[i][j]);
				else
					System.out.print("\t ");
			}
		System.out.print("\n");
		}

	System.out.print("\nQue posición desea saber de matriz[i][j]\n"); 
	System.out.print("\nIngresar i: ");
	i = sc.nextInt();
	System.out.print("\nIngresar j: ");
	j = sc.nextInt();
	System.out.print("\nEl valor es: "+matriz[i][j]);
}







public void fun2()
{
int[][] matriz=new int[20][20];
int dim,i,j,db,item;
//int matriz[20][20], dim,i,j,db,item; 
System.out.print("\nINGRESAR DIMENSION DE LA MATRIZ : ");
dim = sc.nextInt();
System.out.print("\nIngresar Direccionamiento Base: "); 
db = sc.nextInt();
for(i=0;i<dim;i++)
{
for(j=0;j<dim;j++)
{
item=db+(i+j)*(i+j+1)/2 + j; 
matriz[i][j]=item;
}
}

System.out.print("\nLECTURA DE ASIGNACION DE MATRIZ\n");
for(i=0;i<dim;i++)
{
for(j=0;j<dim;j++)
{
if(j<dim-i)


System.out.print("\t"+matriz[i][j]);
else
System.out.print("\t ");
}
System.out.print("\n");
}

System.out.print("\nQue posicion desea saber de matriz[i][j]\n"); 
System.out.print("\nIngresar i: ");
i = sc.nextInt();
System.out.print("\nIngresar j: ");

j = sc.nextInt();
System.out.print("\nEl valor es: "+matriz[i][j]);
}




void fun3()
{
int[][] matriz=new int[20][20];
int dim,i,j,db,item;
System.out.print("\nINGRESAR DIMENSION DE LA MATRIZ : ");
dim = sc.nextInt();
System.out.print("\nIngresar Direccionamiento Base: "); 
db = sc.nextInt();
for(i=0;i<dim;i++)
{
for(j=0;j<dim;j++)
{
if((i+j)%2==0)
{
item=db+(i+j)*(i+j+1)/2 + j; 
matriz[i][j]=item;
}
else
{
item=db+(i+j)*(i+j+1)/2 + i; 
matriz[i][j]=item;
}
}
}

System.out.print("\nLECTURA DE ASIGNACION DE MATRIZ\n");
for(i=0;i<dim;i++)
{
for(j=0;j<dim;j++)
{
if(j<dim-i)
System.out.print("\t"+matriz[i][j]);
else
System.out.print("\t ");
}
System.out.print("\n");
}

System.out.print("\nQue posicion desea saber de matriz[i][j]\n"); 
System.out.print("\nIngresar i: ");
i = sc.nextInt();
System.out.print("\nIngresar j: ");
j = sc.nextInt();

System.out.print("\nEl valor es: "+matriz[i][j]);
}




void fun4(){
int[][] matriz=new int[20][20];
int dim,i,j,db,item;
	System.out.print("\nINGRESAR DIMENSION DE LA MATRIZ : ");
	dim = sc.nextInt();
	System.out.print("\nIngresar Direccionamiento Base: "); 
	db = sc.nextInt();
	for(i=0;i<dim;i++){
		for(j=0;j<dim;j++){
			if((i+j)%2==0)
	{
	item=db+(i+j)*(i+j+1)/2 + i; 
	matriz[i][j]=item;
	}
	else
	{
	item=db+(i+j)*(i+j+1)/2 + j; 
	matriz[i][j]=item;
	}
	}
	}

	System.out.print("\nLECTURA DE ASIGNACION DE MATRIZ\n");
	for(i=0;i<dim;i++)
	{
	for(j=0;j<dim;j++)
	{
	if(j<dim-i)
	System.out.print("\t"+matriz[i][j]);
	else
	System.out.print("\t ");
	}
	System.out.print("\n");
	}

	System.out.print("\nQue posicion desea saber de matriz[i][j]\n"); 
	System.out.print("\nIngresar i: ");
	i = sc.nextInt();
	System.out.print("\nIngresar j: ");
	j = sc.nextInt();

	System.out.print("\nEl valor es: " + matriz[i][j]);
}


}