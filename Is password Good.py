def is_password_good(password):
    pass
    count = 0
    #его длина не менее 8 символов
    if len(password) >= 8:
        count += 1
    
    #он содержит хотя бы одну цифру
    if password.isalpha() is False and password.isalnum():
        count += 1
    
    #он содержит как минимум одну заглавную букву (верхний регистр); 
    if password.islower() is False and password.isdigit() == False:
        count += 1
        
    #он содержит как минимум одну строчную букву (нижний регистр);
    if password.isupper() is False:
        count += 1
    
    # все 4 условия соблюдены
    if count == 4: 
        return True
    else:
        return False
        
# считываем данные
txt = input()


# вызываем функцию
print(is_password_good(txt))