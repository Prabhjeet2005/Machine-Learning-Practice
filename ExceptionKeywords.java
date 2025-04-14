import java.util.*;
public class ExceptionKeywords{
  public static void AgeException(int age) throws Exception{
    if(age<18){
      throw new Exception("Age Invalid");
    }
    System.out.println("Age Valid");
  }
  public static void main(String[] args ){
    try{
      int age = 16;
      AgeException(age);
      System.out.println("Age is: "+age);
    }catch(Exception e){
      System.out.println(e);
    }
    finally{
      System.out.println("Finaaly Block");
    }
  }
}