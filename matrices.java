import static java.lang.System.out;

public class matrices{

public static void main(String []arg){
int[][] t=m2();int c=21;

out.println("Ejercicio numero "+c++);imprimirT(m1());
out.println("Ejercicio numero "+c++);imprimir(rotar(rotar(rotar(m1()))));
out.println("Ejercicio numero "+c++);imprimir(rotar(m1()));
out.println("Ejercicio numero "+c++);imprimirT(rotar(rotar(m1())));
out.println("Ejercicio numero "+c++);imprimir(m1());
out.println("Ejercicio numero "+c++);imprimirT(rotar(rotar(rotar(m1()))));
out.println("Ejercicio numero "+c++);imprimir(rotar(rotar(m1())));
out.println("Ejercicio numero "+c++);imprimirT(rotar(m1()));

out.println("Ejercicio numero "+c++);imprimir(rotar(rotar(t)));
out.println("Ejercicio numero "+c++);imprimir(rotar(rotar(rotar(t))));
out.println("Ejercicio numero "+c++);imprimir(t);
out.println("Ejercicio numero "+c++);imprimir(rotar(t));
out.println("Ejercicio numero "+c++);imprimirT(rotar(t));
out.println("Ejercicio numero "+c++);imprimirT(rotar(rotar(t)));
out.println("Ejercicio numero "+c++);imprimirT(rotar(rotar(rotar(t))));
out.println("Ejercicio numero "+c++);imprimirT(t);
	
}


//imprime matrices tal y como estas
public static void imprimir(int[][] mat){
for(int i=0;i<5;i++){for(int j=0;j<5;j++){
	out.print(mat[i][j]+" ");if(mat[i][j]<=9){out.print(" ");}}out.println("");}
	out.println("\n");
}

//imprime matrices transpuestas
public static void imprimirT(int[][] mat){
for(int i=0;i<5;i++){for(int j=0;j<5;j++){
	out.print(mat[j][i]+" ");if(mat[j][i]<=9){out.print(" ");}}out.println("");}
	out.println("\n");
}

//gira la matriz en una direccion
public static int[][] rotar(int[][] matriz){
int tam=matriz.length;
int[][] rotado=new int[tam][tam];
for(int i=0,a=4;i<5;i++,a--){for(int j=0,b=4;j<5;j++,b--){
rotado[j][a]=matriz[i][j];
}}
return rotado;
}

//matriz del 21-28
public static int[][] m1(){
int v=4;boolean direccion=true;int count=0;
int[][] num=new int[5][5];
for(int i=0;i<5;i++){for(int j=0;j<5;j++){
if(direccion==true){num[i][j]=count++;}else{num[i][v-j]=count++;}
}
direccion=direccion==true?false:true;
}
return num;
}

//matriz del 29-36
public static int[][] m2(){
int p=3,o=4,y=3,u=3,e=5,r=4,l=1;
int count=0;
int[][] num=new int[5][5];
for(int j=0,w=4;j<5;j++,w--){
num[4][w]=count;
count++;}

for(int i=0;i<2;i++){
for(int j=0,w=p-i;j<o-(2*i);j++,w--){
num[w][i]=count;
count++;}
for(int j=l+i;j<e-i;j++){
num[i][j]=count;
count++;}
for(int j=l+i;j<o-i;j++){
num[j][o-i]=count;
count++;}
for(int j=0,w=y-i;j<3-(i*2);j++,w--){
num[u-i][w]=count;
count++;}}
return num;
}}
