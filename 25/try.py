"""
=============================================================
Trial Program for PE 25

Goal: Find the index of the first Fibonacci number
      to contain 1000 digits

=============================================================
"""
_DIGITS = 1000
    
def main():
    print("Trial Program PE 25")
    num1 = 1
    num2 = 1
    count = 2
    
    while ( len ( str(num2) ) < _DIGITS):
        placeholder = num1
        num1 = num2
        num2 = num2 + placeholder
        count += 1
    print(count)
            
main()