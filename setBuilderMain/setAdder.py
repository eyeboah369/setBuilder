import sys
import io
import shutil

#global variables passed throughout program
global userFile

#Super cool graphic I made!!!
print("""   
                                 *       *                          *       *                      
                                *         *                        *         *                            
                               *           *                      *           * 
                              *             *                    *             *
                             *               *                  *               *
                            *                 *                *                 *
                           *      welcome      *              *       Glad        *
                          *         to          *            *         to          *
                         *          the          *          *         have          *  
                         *          set          *          *         you           *
                          *       Builder!      *            *        here!        *
                           *                   *              *                   *
                            *                 *                *                 *
                             *               *                  *               *
                              *             *                    *             *  
                               *           *                      *           * 
                                *        *                         *         *  
                                 *      *                           *       *
                                  *   *                              *     * 
                                                                        """)

#initial CLI function that starts of user input
def start():
    answer = str(input("(Enter 'set' to build a set or 'learn' to learn more about sets): "))
    if answer == 'learn':
        print("Head over to https://matthewpalmer.net/blog/2015/01/20/discrete-maths-math1081-unsw-notes-sets-functions-sequences/index.html")
        print("Happy learning!")
        sys.exit(1)
    if answer == 'set':
        newFile = setBuild()
    else:
        answer = str(input("Invalid input. Please enter 'set or 'learn' to continue"))
        start()
    return newFile

#function to build file for set building 
def setBuild():
    filename = str(input("Are you confirming you want to make a new set file? Enter 'y' to continue: "))
    if filename == 'y':
        file = open('newSet.html', "w+")
        shutil.move("./newSet.html", "./app/templates/newSet.html")
        return file
    else:
        print("Invalid input, try again")
        setBuild()


#function to populate the newly created set file with the data needed to run inside of the flask app seamlessly
def populateSet():
    print("adding numbers to your set...")
    userFile.write("""
    {% extends "login.html" %}
    {% block content %}
    <head>
        <link rel= "stylesheet" type= "text/css" href= "{{ url_for('static',filename='level.css') }}">
    </head>
    <body style="background-color: bisque;">
    <h1 style="font-family: system-ui;">Level 1</h1>

    <div style="display: inline;">
    <div style="float: right; width: 10%; border-radius: 12px; border-style: solid; border-width: 2px; border-color:cadetblue; align-content: center;">
        <p style="font-size: 35px; margin-top: 0">{1,2,3,4}</p>
    </div>

    <div style="float: right; margin-bottom: 3%; margin-right: 5%; width: 10%; border-radius: 12px; border-style: solid; border-width: 2px; border-color:cadetblue; align-content: center;">
        <p style="font-size: 35px; margin-top: 0">{5,6,7,8}</p>
    </div>

    <div style="float: right; margin-bottom: 3%; margin-right: 5%; width: 14%; border-radius: 12px; border-style: solid; border-width: 2px; border-color:cadetblue; align-content: center;">
        <p style="font-size: 35px; margin-top: 0">{9,10,11,12}</p>
    </div>

    <div style="float: right; margin-bottom: 3%; margin-right: 5%; width: 10%; border-radius: 12px; border-style: solid; border-width: 2px; border-color:cadetblue; align-content: center;">
        <p style="font-size: 35px; margin-top: 0%;">{4,5,6,7}</p>
    </div>

    <div style="float: right; margin-bottom: 3%; margin-right: 5%; width: 13%; border-radius: 12px; border-style: solid; border-width: 2px; border-color:cadetblue; align-content: center;">
        <p style="font-size: 35px; margin-top: 0">{0,-1,-2,-3}</p>
    </div>

    <div style="float: right; margin-bottom: 3%; margin-right: 5%; width: 14%; border-radius: 12px; border-style: solid; border-width: 2px; border-color:cadetblue; align-content: center;">
        <p style="font-size: 35px; margin-top: 0">{-4,-5,-6,-7}</p>
    </div>

    <div style="float: right; margin-bottom: 3%; margin-right: 18%; width: 16%; border-radius: 12px; border-style: solid; border-width: 2px; border-color:cadetblue; align-content: center;">
        <p style="font-size: 35px; margin-top: 0">{-8,-9,-10,-11}</p>
    </div>

    <div style="float: right; margin-bottom: 3%; margin-right: 5%; width: 18%; border-radius: 12px; border-style: solid; border-width: 2px; border-color:cadetblue; align-content: center;">
        <p style="font-size: 35px; margin-top: 0">{-20,-10,10,20}</p>
    </div>

    <div style="float: right; margin-bottom: 3%; margin-right: 5%; width: 16%; border-radius: 12px; border-style: solid; border-width: 2px; border-color:cadetblue; align-content: center;">
        <p style="font-size: 35px; margin-top: 0">{12,13,14,15}</p>
    </div>
    </div>

    <h2 style="clear: right">
        Let the N be the set of all numbers; let the following sets be given based on the numbers above: </br>
        - Set of all negative numbers (A)</br>
        - Set of all positive numbers (B)</br>
        - Set of all numbers with two digits (C)</br>
        Using only the symbols (VALUES IN PARENTHESES CORRESPOND TO SPECIAL SYMBOLS) A, B, C, N, {}(| |), ∈(E), ⊆(CC), =, ≠(!=), ∩(^), ∪(U), ×(*),′, ∅(%), >, (, and ) write the following statement: </br>
    </br>""")

    question = str(input("What would you like your question to be? \n"))
    userFile.write(question)
    userFile.write("""
    </h2>

    <form action="" method="post" novalidate style="float: left; clear: right;">
        {{ answerForm.hidden_tag() }}
        <p>
            {{ answerForm.userAnswer.label}} </br>
            {{ answerForm.userAnswer(size=52)}}
        </p>
        <a href="{{ url_for('level1', user_answer=answer) }}"><p> {{ answerForm.submitAnswer() }} </p></a>

    </form>
    </body>
    {% endblock %}""")

    #userFile.close()
    return userFile





#main user interactions including function calls from above
username = str(input("Enter your name: "))
print("What would you like to do", username, "? \n")
userFile = start()
print("Your file has been created! \n")
print("Now lets add content to your new file...")
populateSet()
f = open("./app/templates/newSet.html", "r")
print("Your set is ready ot go!: \n")
#print(f.read())
#f.close()
print("Thank you for building your very own set! Later!")
sys.exit(1)


