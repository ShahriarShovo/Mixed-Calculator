# This is a simple and Basic console calculator
# Developed by Shahriar

# While loop for running this program
while(1):

    # User Define Function
    def main_menue():
    # Menue
        print("\n---------- Menue ----------\n\n")
        print("1. Basic Calculator\n")
        print("2. Matrix Calculator\n")
        print("3. Binary Calculator\n")
        print("4.Coffee ! I want Coffee and Coffee ")
        choose = int(input("\nChoose a Operation : "))
        if(choose==1):
            basic_Calculator()
        elif (choose==2):
            matrix_Calculator()
        elif (choose==3):
            binaryMath()
        elif (choose==4):
            getCoffee()

# Basic calculator Function
    def basic_Calculator():
   
        print("1.Addtion\n")
        print("2.Subtraction\n")
        print("3.Divisiion\n")
        print("4.Multiplication\n")
        print("5.Exit\n")
        # Input which operation user want
        select=int(input("Select Option : "))
        print()
        # If user input one than addition will work also addition function will call 
        if select==1:
            # while for ruuning addition operation
            while(1):
                print("Write 'clear' and go back Main Menue\n" )
                # Input first number
                number_1=input("Enter the First Number : ")
                # if user write 'clear' than it will back main menue again
                if number_1=='clear':
                    main_menue()
                    
                # Input Second Number
                number_2=int(input("Enter the First Number : "))
                #Calculation 

                final_result=getAddtion(number_1,number_2)
                print("---------------------------")
                # Show result on display
                print("Result ",int(final_result))
                print()
                
# If user input one than subtraction will work also addition function will call 
        elif select==2:
            # While loop for running subtraction operation
            while(1):
                print("Write 'clear' and go back Main Menue\n" )
                # Input first number
                number_1=input("Enter the First Number : ")
                # if user write ' clear ' than it will move main menue
                if number_1=='clear':
                    main_menue() # main menue function
                #Input second number
                number_2=int(input("Enter the First Number : "))
                #calculation
                final_result=getSubtraction(number_1,number_2)
                print("---------------------------")
                #showing result on display
                print("Result : ",int(final_result))
                print()

        # If user input one than division will work also addition function will call 
        elif select==3:

            # While loop for running division operation

            while(1):
                #Message
                print("Write 'clear' and go back Main Menue\n" )
                # input first number but if user write 'celar' than it will move to main menue
                number_1=input("Enter the First Number : ")
                # checking condition
                if number_1=='clear':
                    main_menue()
                    # input second number
                number_2=int(input("Enter the First Number : "))
                # calculation
                final_result=getDivision(number_1,number_2)
                print("---------------------------")
                # showing result on the display
                print("Result : ",int(final_result))
                print()
        # If user input one than multiplication will work also addition function will call 
        elif select==4:

            # while loop for running multiplication

            while(1):
                # message
                print("Write 'clear' and go back Main Menue\n" )
                # input first number but if user write 'celar' than it will move to main menue
                number_1=input("Enter the First Number : ")
                # checking condition
                if number_1=='clear':
                    main_menue()
                # input second numnber
                number_2=int(input("Enter the First Number : "))
                # calculation 
                final_result=getMultiplication(number_1,number_2)
                print("---------------------------")
                # showing result on the display
                print("Result :",int(final_result))
                print()


        elif select==5:
            main_menue()

# Basic Calculator Functions  

# Addtion Function 
    def getAddtion(number_1,number_2):
        return int(number_1)+number_2
    
# Subtraction Function
    def getSubtraction(number_1,number_2):
        return int(number_1)-number_2
# Division Function
    def getDivision(number_1,number_2):
        return float(number_1) / number_2

# Multiplication Function
    def getMultiplication(number_1,number_2):
        return int(number_1)* number_2

    def getDivision_2(number_1,number_2):
        return int(number_1) // number_2
 
#-------------------------------------------------

# Matrix Calculator Function 

    def matrix_Calculator():

        print("1.Matrix Addtion\n")
        print("2.Matrix Subtraction\n")
        print("3.Matrix Multiplication\n")
        print("4.Exit\n")

        select=int(input("Select Option : "))

        if select==1:
            # while for ruuning addition operation
            while(1):
                print("Write 'clear' and go back Main Menue\n" )
                # Input first number
                input_matrix_row=input("Enter the  Matrix Row : ")
                # if user write 'clear' than it will back main menue again
                if input_matrix_row =='clear':
                    main_menue()
                    
                # Input Second Number
                input_matrix_col=int(input("Enter the Matrix Column  : "))
                #Calculation 
                print()
                
                first_matrix=printingMatrix(input_matrix_row,input_matrix_col)
                second_matrix=printingMatrix(input_matrix_row,input_matrix_col)
                print("---------------------------\n")
                add_result=getMatrixAddtion(first_matrix,second_matrix)
        
        elif select == 2 :

            while(1):
                print("Write 'clear' and go back Main Menue\n" )
                # Input first number
                input_matrix_row=input("Enter the  Matrix Row : ")
                # if user write 'clear' than it will back main menue again
                if input_matrix_row =='clear':
                    main_menue()
                    
                # Input Second Number
                input_matrix_col=int(input("Enter the Matrix Column  : "))
                #Calculation 
                print()

                first_matrix=printingMatrix(input_matrix_row,input_matrix_col)
                second_matrix=printingMatrix(input_matrix_row,input_matrix_col)
                print("---------------------------\n")
                sub_result=getMatrixSubtraction(first_matrix,second_matrix)

        elif select == 3:
            while(1):
                print("Write 'clear' and go back Main Menue\n" )
                # Input first number
                input_f_matrix_row=input("Enter the  First Matrix Row : ")
                # if user write 'clear' than it will back main menue again
                if input_f_matrix_row =='clear':
                    main_menue()
                    
                # Input Second Number
                input_f_matrix_col=int(input("Enter the First Matrix Column  : "))

                input_s_matrix_row=input("Enter the Second  Matrix Row : ")
                input_s_matrix_col=input("Enter the Second  Matrix Column : ")

                while(input_f_matrix_row != input_s_matrix_col):
                    print("Sorry !\n First Matrix Row and Second Matrix Column is not same .\n So Matrix Multiplication cant be done\nPlease try again : ")
                    input_f_matrix_row=input("Enter the  First Matrix Row : ")
                # if user write 'clear' than it will back main menue again
                    if input_matrix_row =='clear':
                        main_menue()
                    
                    input_f_matrix_col=int(input("Enter the First Matrix Column  : "))
                    # Input Second Matrix
                    input_s_matrix_row=int(input("Enter the Second  Matrix Row : "))
                    input_s_matrix_col=int(input("Enter the Second  Matrix Column : "))

                first_matrix=printingMatrix(input_f_matrix_row,input_f_matrix_col)
                second_matrix=printingMatrix(input_s_matrix_row,input_s_matrix_col)
                print("---------------------------\n")
                mul_result=getMatrixMultiplication(first_matrix,second_matrix)
               
    def printingMatrix(input_matrix_row,input_matrix_col):
        matrix=[[int(input("Enter the Matrix Data :")) for j in range(int(input_matrix_col))] for i in range(int(input_matrix_row))]
                
        for i in range(int(input_matrix_row)):       
            for j in range(int(input_matrix_col)):          
                print(matrix[i][j],end='  ')            
            print("\n")
        return matrix

    def getMatrixAddtion(first_matrix,second_matrix):
        result=[]

        for i in range(len(first_matrix)):
            addData=[]
            for j in range(len(first_matrix)):
                addData.append(first_matrix[i][j] + second_matrix[i][j])
            result.append(addData)

        for i in range(len(result)):
            for j in range(len(result)):
                print(result[i][j],end='  ')
            print("\n")
        return result

    def getMatrixSubtraction(first_matrix,second_matrix):
        result=[]

        for i in range(len(first_matrix)):
            subData=[]
            for j in range(len(first_matrix)):
                subData.append(first_matrix[i][j] - second_matrix[i][j])
            result.append(subData)

        for i in range(len(result)):
            for j in range(len(result)):
                print(result[i][j],end='  ')
            print("\n")
        return result

    def getMatrixMultiplication(first_matrix,second_matrix):
        result=[]

        for i in range(len(first_matrix)):
            addData=[]
            for j in range(len(second_matrix[0])):
                store=0
                for k in range(len(first_matrix[i])):
                    store+=first_matrix[i][k] * second_matrix[k][j]
                addData.append(store)
            
            result.append(addData)
         
        for i in range(len(result)):
            for j in range(len(result)):
                print(result[i][j],end='  ')
            print("\n")
       
        return result

    def binaryMath():
        print("1.Convert Decimal to Binary\n")
        print("2.Binary Addtion\n")
        print("3.Binary Subtraction\n")
        print("4.Binary Divisiion\n")
        print("5.Binary Multiplication\n")
        print("6.Exit\n")

        select=int(input("Select Option : "))
        print()
        # If user input one than addition will work also addition function will call 
        if select==1:
            # while for ruuning addition operation
            while(1):
                print("\n\nWrite '0 (Zero)' and go back Main Menue\n" )
                # Input first number
                number=int(input("Enter the Decimal Number : "))
                # if user write 'clear' than it will back main menue again
                if number==0:
                    main_menue()

                print("---------------------------")
                #showing result on display
                
                Binary=convertDecimalToBinary(number)
        elif select == 2:
            while(1):
                print("\n\n Write 0(Zero) and go back Main Menue\n")
                binary_number_1=int(input("Enter the First Binary Number :"))
                if binary_number_1==0:
                    main_menue()
                binary_number_2=int(input("Enter the Second Binary Number :"))

                binary_1=convertBinaryToDecimal(binary_number_1)
                binary_2=convertBinaryToDecimal(binary_number_2)
                

                binaryAddtion=getAddtion(binary_1,binary_2)
                print("\n--------------------\n")
                final_Result=convertDecimalToBinary(binaryAddtion)
                
        elif select == 3:
            while(1):
                print("\n\n Write 0(Zero) and go back Main Menue\n")
                binary_number_1=int(input("Enter the First Binary Number :"))
                if binary_number_1==0:
                    main_menue()
                binary_number_2=int(input("Enter the Second Binary Number :"))

                binary_1=convertBinaryToDecimal(binary_number_1)
                binary_2=convertBinaryToDecimal(binary_number_2)
                

                binarySubtraction=getSubtraction(binary_1,binary_2)
                print("\n--------------------\n")
                final_Result=convertDecimalToBinary(binarySubtraction)

        elif select == 4:
            while(1):
                print("\n\n Write 0(Zero) and go back Main Menue\n")
                binary_number_1=int(input("Enter the First Binary Number :"))
                if binary_number_1==0:
                    main_menue()
                binary_number_2=int(input("Enter the Second Binary Number :"))

                binary_1=convertBinaryToDecimal(binary_number_1)
                binary_2=convertBinaryToDecimal(binary_number_2)
                

                binaryDivision=getDivision_2(binary_1,binary_2)
                print("\n--------------------\n")
                final_Result=convertDecimalToBinary(binaryDivision)

        elif select == 5:
            while(1):
                print("\n\n Write 0(Zero) and go back Main Menue\n")
                binary_number_1=int(input("Enter the First Binary Number :"))
                if binary_number_1==0:
                    main_menue()
                binary_number_2=int(input("Enter the Second Binary Number :"))

                binary_1=convertBinaryToDecimal(binary_number_1)
                binary_2=convertBinaryToDecimal(binary_number_2)
                

                binaryMultiplication=getMultiplication(binary_1,binary_2)
                print("\n--------------------\n")
                final_Result=convertDecimalToBinary(binaryMultiplication)
                
    def convertDecimalToBinary(number):
        binary=[]
        i=0
        while(number != 0):
            binary.append(number%2)
            number=number//2
            i+=1
        
        
        for i in range(len(binary)-1,-1,-1):
            print(binary[i],end=' ')
        return number
        
    def getCoffee():
        for i in range(11):
            print("I love Coffee ")
    

    def convertBinaryToDecimal(convertToDecimal):
        sum=0
        i=0
        while convertToDecimal !=0:
            remainder=convertToDecimal % 10
            sum=sum+remainder*pow(2,i)
            convertToDecimal=convertToDecimal//10
            i+=1
        
        return sum
#Main Function

    main_menue()

    
    
    


    
    
        
    


