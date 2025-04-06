public class AccountTest {
    public static void main(String[] args) throws Exception {
        App app = new App();
        App.Account account1 = app.new Account("Jane Green", 50.00);
        App.Account account2 = app.new Account("John Blue", -7.53);
        System.out.println(account1.getName() + " balance: $" + account1.getBalance());
        System.out.println(account2.getName() + " balance: $" + account2.getBalance());

        Account AccountOrg = new Account("John Doe", 1000.9912);

        AccountOrg.setName("John Doe");
        AccountOrg.deposit(1000.9912);
        System.out.println(AccountOrg.getName() + " balance: $" + AccountOrg.getBalance());
    }
}
