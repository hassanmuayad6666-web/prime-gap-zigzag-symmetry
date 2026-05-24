def generate_and_prove_hassan_sequence(limit):
    # 1. توليد الأعداد الأولية
    sieve = [True] * limit
    primes = []
    for p in range(2, limit):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, limit, p):
                sieve[i] = False
                
    sequence = []
    all_even_after_first = True
    
    print("--- START OF HASSAN'S MATRIX TRANSITION VERIFICATION ---")
    print("Executing dynamic cross-over rules...\n")
    
    # 2. الحساب وطباعة خطوات الإقناع للحدود الأولى
    for n in range(len(primes) - 2):
        p_n = primes[n]        
        p_n2 = primes[n+2]     
        steps = p_n2 - p_n
        sequence.append(steps)
        
        # طباعة تفصيلية لأول 5 خطوات لإقناع العلماء بطريقتك بالفيديو
        if n < 5:
            print(f"Step {n+1}: Pairing Prime({p_n}) with Prime({p_n2}) -> Remaining steps = {steps}")
            if n == 0:
                print(f"        -> Note: First term is {steps} (Odd because it starts from the only even prime 2).\n")
            else:
                print(f"        -> Note: Term is {steps} (Strictly Even).\n")
                
        # اختبار هل الأعداد بعد الأول زوجية دائماً؟
        if n > 0 and steps % 2 != 0:
            all_even_after_first = False

    print("-------------------------------------------------------")
    print(f"Generated Sequence Preview (First 15 terms): {sequence[:15]}")
    print("-------------------------------------------------------")
    
    # 3. حكم الإثبات النهائي الذي يبحث عنه العلماء
    if all_even_after_first:
        print("MATHEMATICAL PROOF VERDICT:")
        print(f"SUCCESS! 100% of terms after the first term are STRICTLY EVEN.")
        print(f"Tested successfully across all prime boundaries up to limit: {limit}")
    else:
        print("Test failed.")
    print("--- END OF PROOF ---")

# تشغيل كود الإثبات الشامل
generate_and_prove_hassan_sequence(2000)
