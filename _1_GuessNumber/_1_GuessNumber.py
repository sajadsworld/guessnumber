import random

class GuessNumber(object):
    def __init__(self):
        self.user_guess_number = None
        self.cpu_guess_number = None

    def get_cpu_guess(self):
        self.cpu_guess_number = random.randint(1, 10)
        return self.cpu_guess_number

    def get_user_input(self):
        self.user_guess_number = int(input("Enter your guess number: "))
        print(f"your guess number is {self.user_guess_number}")
        return self.user_guess_number

    def guess_number(self):
        if self.user_guess_number > self.cpu_guess_number:
            print(f"User Guess Number {self.user_guess_number} is bigger than cpu guess number")
            return f"User Guess Number {self.user_guess_number} is bigger than cpu guess number"
        elif self.user_guess_number < self.cpu_guess_number:
            print(f"User Guess Number {self.user_guess_number} is smaller than cpu guess number")
            return f"User Guess Number {self.user_guess_number} is smaller than cpu guess number"
        else:
            print(f"User Guess Number {self.user_guess_number} is equal to cpu guess number")
            return f"User Guess Number {self.user_guess_number} is equal to cpu guess number"

    def run(self):
        getcpuinput = self.get_cpu_guess()

        count = 1
        while count <= 5:
            getuserinput = self.get_user_input()
            self.guess_number()
            if getuserinput == getcpuinput:
                break
            print(f"You have {count} guess")
            count += 1


if __name__ == "__main__":
    guessnumber = GuessNumber()
    guessnumber.run()
    