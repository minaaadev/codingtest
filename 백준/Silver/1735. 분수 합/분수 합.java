import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);

        int b1=sc.nextInt();
        int a1=sc.nextInt();
        int b2=sc.nextInt();
        int a2=sc.nextInt();
        int max=1;

        int b=a2*b1+a1*b2;
        int a=a1*a2;//분모


        for(int i=1; i<=a && i<=b; i++){
            if (a%i==0 && b%i==0){
                max=i;
            }
        }
        sc.close();
        b=b/max;
        a=a/max;
        
        System.out.print(b+" ");
        System.out.print(a);

    }

}
