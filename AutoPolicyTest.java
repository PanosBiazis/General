public class AutoPolicyTest {//class header
    
    public static void main(String[] args) {//main
    
    AutoPolicy policy1 = new AutoPolicy(11111111, "Toyota Camry", "NJ");//constructor
 
    AutoPolicy policy2 = new AutoPolicy(22222222, "Ford Fusion", "ME");//constructor
    
    policyInNoFaultState(policy1);//method call
    
    policyInNoFaultState(policy2);//method call    
    
}//end main

public static void policyInNoFaultState(AutoPolicy policy) {//method header

    System.out.println("The auto policy:");//output
   
    System.out.printf("Account #: %d; Car: %s; State %s %s a no-fault state%n%n", policy.getAccountNumber(), policy.getMakeAndModel(), policy.getState(), (policy.isNoFaultState() ? "is" : "is not"));//output

}//end method policyInNoFaultState

}//end class AutoPolicyTest