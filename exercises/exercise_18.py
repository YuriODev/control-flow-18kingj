# Your solution to Exercise 18

remember_name = input("Do you remember the person's name: ").lower()
if remember_name == 'yes':
    is_ex = input("Is it an ex: ").lower()
    if is_ex == 'yes':
        are_you_drunk = input("Are you drunk: ").lower()
        if are_you_drunk == 'yes':
            rekindle = input("Do you want to rekindle and/or give 'em what for: ").lower()
            output = "Say hi." if rekindle == 'yes' else "Don't say hi."
        else:
            in_convertible = input("Are you in a convertible with Brad Pitt and/or Rihanna: ").lower()
            output = "Say hi." if in_convertible == 'yes' else "Don't say hi."
    else:
        friend_ex = input("A friend's ex: ").lower()
        if friend_ex == 'yes':
            output = "Don't say hi."
        else:
            enemy_or_frenemy = input("An enemy or frenemy: ").lower()
            if enemy_or_frenemy == 'yes':
                in_convertible = input("Are you in a convertible with Brad Pitt and/or Rihanna: ").lower()
                output = "Say hi." if in_convertible == 'yes' else "Don't say hi."
            else:
                robbing_bank = input("Are you robbing a bank: ").lower()
                if robbing_bank == 'yes':
                    output = "Don't say hi."
                else:
                    in_bathrobe = input("Are you in a bathrobe: ").lower()
                    output = "Don't say hi." if in_bathrobe == 'yes' else "Say hi."

else:  # Don't remember the person's name
    time_to_flee = input("Is there time to flee: ").lower()
    if time_to_flee == 'yes':
        output = "Run for it."
    else:
        pretend_call = input("Could you pretend to get a call on your cell: ").lower()
        if pretend_call == 'yes':
            output = "Hello, doctor. What are my test results?"
        else:
            wearing_sunglasses = input("Are you wearing sunglasses: ").lower()
            if wearing_sunglasses == 'yes':
                output = "Keep walking."
            else:
                output = "Address the person using an amusing nickname such as 'Sarge', 'Slugger', or 'Master Blaster.'"
print(output)