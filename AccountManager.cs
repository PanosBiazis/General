using System;

namespace BankingSystem
{
    // Base class for all accounts
    abstract class Account
    {
        protected double balance;
        public abstract void Deposit(double amount);
        public abstract void Withdraw(double amount);
        public virtual void DisplayBalance()
        {
            Console.WriteLine("Balance: " + balance);
        }
    }

    // Derived class for savings accounts
    class SavingsAccount : Account
    {
        public override void Deposit(double amount)
        {
            balance += amount;
            Console.WriteLine("Deposited: " + amount);
        }

        public override void Withdraw(double amount)
        {
            if (balance >= amount)
            {
                balance -= amount;
                Console.WriteLine("Withdrawn: " + amount);
            }
            else
            {
                Console.WriteLine("Insufficient funds.");
            }
        }
    }

    // Derived class for checking accounts
    class CheckingAccount : Account
    {
        public override void Deposit(double amount)
        {
            balance += amount;
            Console.WriteLine("Deposited: " + amount);
        }

        public override void Withdraw(double amount)
        {
            if (balance >= amount)
            {
                balance -= amount;
                Console.WriteLine("Withdrawn: " + amount);
            }
            else
            {
                Console.WriteLine("Insufficient funds.");
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            SavingsAccount savings = new SavingsAccount();
            savings.Deposit(1000);
            savings.Withdraw(500);
            savings.DisplayBalance();

            CheckingAccount checking = new CheckingAccount();
            checking.Deposit(2000);
            checking.Withdraw(1500);
            checking.DisplayBalance();
        }
    }
}
