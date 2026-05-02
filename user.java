import java.util.*;

public class user {
    public static void main(String[] args) {

        Scanner sc = new Scanner (System.in);

        while(true){

            System.out.println("Enter your number 0 for Exit :");
            int x = sc.nextInt();

            if (x==0){
            System.out.println("End program!");
            break;
            }

            else if (x<100){
            System.out.println("Smaller than 100 !");
            }

            else if (x>100){
                System.out.println("Grater than 100 !");
            }
            
            else 
            {
                System.out.println("Invalid Index !");

            }
            
            
            }
            sc.close();
        }
    }



       
   