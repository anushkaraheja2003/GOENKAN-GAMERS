print("---------------------------------------------------------------------------------------------------------------------------------------------------")
print("****************************************************GOENKAN GAMERS *********************************************************************************")
print("---------------------------------------------------------------------------------------------------------------------------------------------------")
print("                          WELCOME PLAYERS,GET READY TO ENTER INTO A WORLD FULL OF FUN AND GAMES                                             ")

print("                                           MAY THE ODDS BE EVER IN YOUR FAVOUR (;                                                          ")
print("----------------------------------------------------------------------------------------------------------------------------------------------------")


X="Y"
while X=="Y":
   print("        **************************************************GAMES**************************************************************                                                                     ")
   print("----------------------------------------------------------------------------------------------------------------------------------------------------")
   print("1. MAGIC 8 BALL")
   print("2. HANGMAN")
   print("3. TIC-TAC-TOE")
   print("4. ROCK PAPER SCISSORS")
   print("5. ARCHERY MATCH ARCADE GAME- DELHI VS SIKKIM ")
   print("6. SNAKE GAME")
   print("----------------------------------------------------------------------------------------------------------------------------------------------------")

   print("HEY GAMER , WHICH GAME WOULD YOU LIKE TO ROLL ?????")
   print()
   print("ENTER YOUR CHOICE (1,2,3,4,OR 5 OUR SPECIAL ARCHERY GAME DESIGNED ESPECIALLY FOR YOU) ")
   print("---------------------------------------------------------------------------------------------------------------------------------------------------")
   print()
   CHOICE_OF_GAME=int(input("enter your choice of game"))
   print("-"*148)
   if CHOICE_OF_GAME==1:
      print('''THE INTRUCTIONS ARE AS FOLLOWS:
         MAGIC BALL IS A FUN FORTUNE TELLING GAME. YOU CAN TYPE IN ANY QUESTION AND THE MAGIC BALL WOULD PROVIDE YOU AN ADVICE OR PREDICT FUTURE''')
      print("-"*148)
      import random as r
      print("Hello! My name is Magic 8 Ball and I'm here to answer all your queries ")
      print("-"*148)
      ANS="YES"
      while ANS=="YES":
         q=input("Ask me any yes/no questions :D  ")
         with open("magic 8 ball.txt") as f:
            d = f.readlines()
            ans = r.randint(0, 16)
            word = d[ans]
            print(word)
            ANS=input("Would you like to continue? YES/NO  ")
      
      print("Thank you for playing! Hope you have a great day!")
      print("-"*148)

   elif CHOICE_OF_GAME==2:
      print('''HANGMAN IS A POPULAR GUESSING GAME. PLAYER ATTEMPTS TO BUILD A MISSING WORD BY
               GUESSING ONE LETTER AT A TIME.AFTER CERTAIN NUMBER OF INCORRECT GUESSES, THE GAME ENDS
               OR THE GAME ALSO ENDS IF PLAYER CORRECTLY IDENTIFIES ALL LETTERS OF THE MISSING WORD''')
      import random as r
      # steps to select a random word from HANGMAN.txt file
      with open("HANGMAN.txt") as f:
                           d = f.read().split()
                           number = r.randint(0, len(d))
                           word = d[number]

      # create a list of underscores 
      # it contains exactly same number of underscore as the length of our random word
      lines = []
      for i in word:
         lines.append('_')

      #   wrong variable is used to track number of wrong letters.
      #   a user can make If it is 6 then terminate the program and print message

      wrong = 0
      while True:
         letter = input('\nGuess your letter :')
         if letter in word:
            for i in range(0, len(word)):
               if word[i] == letter:
                  lines[i] = letter
         else:
            # letter is not in the word
            wrong += 1
            # print the word with inserted letters
            for i in lines:
                print(i, end="")

            # check letters remained in the list

            x=lines.count('_')

            if x == 0 or wrong == 4:
               break
                           


      if wrong>=4:
         print("\n\n\n Sorry :(...You have lost this round.")
         print("-"*148)
                           
      else:
         print("\n\n\n VICTORY! Congratulations!:D ")
         print("-"*148)
                      
   elif CHOICE_OF_GAME==3:
      print("-"*148)
      print("******************************************************* TIC TAC TOE *********************************************************** *****")
      print("-"*148)
      print('''THE INSTRUCTIONS TO PLAY ARE AS FOLLOWS:
               ITS A DUAL PLAYER GAME , WHICH CAN BE PLAYEED BY TWO PLAYERS X AND Y. ITS PLAYED ON A 3X3 GRID.
               THE FIRST PLAYER TO GET 3 OF HIS/HER MARKS IN A ROW(UP,DOWN<ACROSS OR DIGONALLY) IS THW WINNER.
               WHEN ALL 9 SQUARES ARE FULL,THE GAME IS OVER!!!''')
      print("-"*148)
      theboard={'1': ' ' , '2': ' ' , '3': ' ' ,
          '4': ' ' , '5': ' ' , '6': ' ' ,
          '7': ' ' , '8': ' ' , '9' : ' ' }

      board_keys=[]
      for key in theboard:
         board_keys.append(key)
    
      def printboard(board):
         print(board['1'] + '|' + board['2'] + '|' + board['3'])
         print("-+-+-")
         print(board['4'] + '|' + board['5'] + '|' + board['6'])
         print("-+-+-")
         print(board['7'] + '|' + board['8'] + '|' + board['9'])
    
      def game():
         turn = 'X'
         count = 0
    
         for i in range (10):
            printboard(theboard)
            print("It's", turn, "'s turn, move to where?")
        
            move = input()
         
            if theboard[move] == ' ':
               theboard[move] = turn
               count+=1
            else:
               print("Place filled, Please move elsewhere..")
               print("-"*148)
               continue
            if count>=5:
               if theboard['7'] == theboard['8'] == theboard['9']!=' ':
                  printboard(theboard)
                  print("Game Over.")
                  print("--------------------------------------------------")
                  print("_X_X_X_", turn, "Won the match. _X_X_X_")
                  print("-"*148)
                  break
               elif theboard['4'] == theboard['5'] == theboard['6']!=' ':
                  printboard(theboard)
                  print("Game over. ")
                  print("--------------------------------------------------")
                  print("_X_X_X_", turn, "Won the match. _X_X_X_")
                  print("-"*148)
                  break
               elif theboard['1'] == theboard['2'] == theboard['3']!=' ':
                  printboard(theboard)
                  print("Game Over. ")
                  print("--------------------------------------------------")
                  print("_X_X_X_", turn, "Won the match. _X_X_X_")
                  print("-"*148)
                  break
               elif theboard['1'] == theboard['4'] == theboard['7']!=' ':
                  printboard(theboard)
                  print("Game Over. ")
                  print("--------------------------------------------------")
                  print("_X_X_X_", turn, "Won the match. _X_X_X_")
                  print("-"*148)
                  break
               elif theboard['2'] == theboard['5'] == theboard['8']!=' ':
                  printboard(theboard)
                  print("Game Over. ")
                  print("--------------------------------------------------")
                  print("_X_X_X_", turn, "Won the match. _X_X_X_")
                  print("-"*148)
                  break
               elif theboard['3'] == theboard['6'] == theboard['9']!=' ':
                  printboard(theboard)
                  print("Game Over. ")
                  print("--------------------------------------------------")
                  print("_X_X_X_", turn, "Won the match. _X_X_X_")
                  print("-"*148)
                  break
               elif theboard['1'] == theboard['5'] == theboard['9']!=' ':
                  printboard(theboard)
                  print("Game Over. ")
                  print("--------------------------------------------------")
                  print("_X_X_X_", turn, "Won the match. _X_X_X_")
                  print("-"*148)
                  break
               elif theboard['3'] == theboard['5'] == theboard['7']!=' ':
                  printboard(theboard)
                  print("Game Over. ")
                  print("--------------------------------------------------")
                  print("_X_X_X_", turn, "Won the match. _X_X_X_")
                  print("-"*148)
                  break
            if count == 9:
               print("Game Over. ")
               print("--------------------------------------------------")
               print("_X_X_X_ It's a Tie _X_X_X_")
               print("-"*148)
                
            if turn == 'X':
               turn = 'O'
            else:
               turn = 'X'
            
         restart=input("Do You Want To Start Again? (YES/N0) :")
         if restart=="YES" or restart=="yes":
            for key in board_keys:
             
               theboard[key] = ' '
            
            game()
      if __name__ == "__main__":
         game()


   elif CHOICE_OF_GAME==4:
      print("-"*148)
      print("*************************************************** ROCK PAPER SCISSORS **************************************************************")
      print("-"*148)
      print(''' THE INSTRUCTIONS FOR PLAYING THE GAME ARE AS FOLLOWS:
                1)THE GAME IS GOING TO BE PLAYED BY THE PLAYER AND YOUR OPPONENT IS GOING TO BE THE COMPUTER
                2)IF YOU CHOOSE Rock, YOU WILL WIN AGAINST Scissors BUT LOSE AGAINST Paper.
                3)IF YOU CHOOSE Scissors, YOU WILL WIN AGAINST Paper BUT LOSE AGAINST Rock.
                4)IF YOU CHOOSE Paper, YOU WILL WIN AGAINST Rock BUT LOSE AGAINST Scissors.''')
      print("-"*148)
      ANS="YES"
      while ANS=="YES":
         from random import randint

         #create a list of play options
         t = ["Rock", "Paper", "Scissors"]

         #assign a random play to the computer
         computer = t[randint(0,2)]

         #set player to False
         player = False

         while player == False:
            #set player to True
            print("-"*148)
            player = input(''' WHAT IS IT GOING TO BE !!!
                                  Rock, Paper OR  Scissors?????''')
            print("-"*148)
            if player == computer:
               print("-"*148)
               print("Tie! BETTER LUCK NEXT TIME (:")
               print("-"*148)
            elif player == "Rock":
               if computer == "Paper":
                  print("-"*148)
                  print("You lose!", computer, "covers", player,"BETTER LUCK NEXT TIME (:")
                  print("-"*148)
               else:
                  print("-"*148)
                  print("You win!", player, "smashes", computer,"BRAVO!!")
                  print("-"*148)
            elif player == "Paper":
               if computer == "Scissors":
                  print("-"*148)
                  print("You lose!", computer, "cut", player,"BETTER LUCK NEXT TIME (:")
                  print("-"*148)
               else:
                  print("-"*148)
                  print("You win!", player, "covers", computer,"BRAVO!!")
                  print("-"*148)
            elif player == "Scissors":
               
               if computer == "Rock":
                  print("-"*148)
                  print("You lose...", computer, "smashes", player,"BETTER LUCK NEXT TIME (:")
                  print("-"*148)
               else:
                  print("-"*148)
                  print("You win!", player, "cut", computer,"BRAVO!!")
                  print("-"*148)
            else:
               print("-"*148)
               print("That's not a valid play. Check your spelling!")
               print("-"*148)
               #player was set to True, but we want it to be False so the loop continues
            player = False
            computer = t[randint(0,2)]
            ANS=input("DO YPU WANT TO REPLAY ??? OUR INSTINCTS TELL US THAT ITS GOING TO BE FUN!!!! (YES/NO)")

   elif CHOICE_OF_GAME==5:
      print("----------------------------------------------------------------------------------------------------------------------------------------------------")
      print("********************************************ARCHERY MATCH ARCADE GAME- DELHI VS SIKKIM************************************************************")
      print("\t                                         ~EK BHARAT SHRESTH BHARAT~                                                 \t")
      print("----------------------------------------------------------------------------------------------------------------------------------------------------")
      print(''' "ARCHERY MATCH ARCADE GAME- DELHI VS SIKKIM" HAS BEEN DESIGNED ESPECIALLY IN ORDER TO PAY HOMAGE TO SIKKIM'S INDEGENIOUS SPORT,
             ARCHERY. Our inspired by FitIndia’s contribution to Prime Minister Narendra Modi’s Ek Bharat Shreshtha Bharat Initiative. ''')
      print("----------------------------------------------------------------------------------------------------------------------------------------- ----------")
      print("----------------------------------------------------------------------------------------------------------------------------------------------------")
      print(''' THE INSTRUCTIONS FOR PLAYING THE GAME ARE AS FOLLOWS:
                 1)The game will be played from the perspective of a player from Delhi against a player from Sikkim
                 or vice versa, depending upon user entry.

                 2)Number of shoots rely upon the player’s will.
                 The performance of the computerized opponent was controlled by difficulty levels: Novice, Intermediate, and Advanced.

                 3)Novice opponent could only shoot the five outermost rings, intermediate was limited from 6 to 8 points,
                  and advanced’s score varied between the three innermost rings, including the notorious Bull’s Eye.''')
      print("----------------------------------------------------------------------------------------------------------------------------------------------------")
      print("----------------------------------------------------------------------------------------------------------------------------------------------------")
      import random
      
     
      print()
      ch=input("Player from? d/s")
      print()
      print("Difficulty levels")
      print("-"*60)
      print("1. Novice")
      print("2. Intermediate")
      print("3. Advanced")
      print("-"*60)
      lev=int(input("Enter your choice:"))

      ans="y"

      if ch=="d":
         print("Welcome player from Delhi!")
         print("-"*60)
         while ans=="y":
            sumd=0
            x=input("Release arrow? y/n")
            print()
            if x=="y":
               num1=random.randrange(1,11)
               print("Game set match! You have scored", num1, "points")
               sumd+=num1
               print("Total score for Delhi:", sumd)
               print("-"*60)
             
            sumsik=0
            print("Your opponent from Sikkim is now playing")
            if lev==1:
               num2=random.randrange(1,5)
               print("Brava! They have scored", num2, "points")
               sumsik+=num2
               print("Total score for Sikkim:", sumsik)
            elif lev==2:
               num2=random.randrange(5,8)
               print("Brava! They have scored", num2, "points")
               sumsik+=num2
               print("Total score for Sikkim:", sumsik)
            elif lev==3:
               num2=random.randrange(8,11)
               print("Bravo!!!! They have scored", num2, "points")
               sumsik+=num2
               print("Total score for Sikkim:", sumsik)
            print("-"*60)
            ans=input("Do yoy want a Rematch? y/n")
            print()

         if sumd>sumsik:
            print("Congratulations player from Delhi! You have won")
            print("-"*60)
         else:
            print("Sadly, you have lost ): , BETTER LUCK NEXT TIME!!!")
            print("-"*60)
        
                
            
      if ch=="s":
        print("Welcome player from Sikkim!")
        print("-"*60)
        while ans=="y":
           sumsik=0
           x=input("Release arrow? y/n")
           print()
           if x=="y":
              num1=random.randrange(1,11)
              print("Game set match! You have scored", num1, "points")
              sumsik+=num1
              print("Total score for Sikkim:", sumsik)
              print("-"*60)
             
           sumd=0
           print("Your opponent from Delhi is now playing")
           if lev==1:
              num2=random.randrange(1,5)
              print("Brava! They have scored", num2, "points")
              sumd+=num2
              print("Total score for Delhi:", sumd)
           elif lev==2:
              num2=random.randrange(5,8)
              print("Brava! They have scored", num2, "points")
              sumd+=num2
              print("Total score for Delhi:", sumd)
           elif lev==3:
              num2=random.randrange(8,11)
              print("Brava! They have scored", num2, "points")
              sumd+=num2
              print("Total score for Delhi:", sumd)
           print("-"*60)
           ans=input("Do you want a Rematch? y/n")
           print()

        if sumsik>sumd:
          print("Congratulations player from Sikkim! You have won")
          print("-"*60)
        else:
          print("Sadly, you have lost player")
          print("-"*60)
      print()
      print("-"*60)
      print("THANK YOU FOR PLAYING")
      print("-"*60)
   elif CHOICE_OF_GAME==6:
      """
      Snake Eater
      Made with PyGame
"""

      import pygame, sys, time, random


      # Difficulty settings
      # Easy      ->  10
      # Medium    ->  25
      # Hard      ->  40
      # Harder    ->  60
      # Impossible->  120
      difficulty = 10

      # Window size
      frame_size_x = 720
      frame_size_y = 480

      # Checks for errors encountered
      check_errors = pygame.init()
      # pygame.init() example output -> (6, 0)
      # second number in tuple gives number of errors
      if check_errors[1] > 0:
          print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
          sys.exit(-1)
      else:
          print('[+] Game successfully initialised')


      # Initialise game window
      pygame.display.set_caption('Snake Eater')
      game_window = pygame.display.set_mode((frame_size_x, frame_size_y))


      # Colors (R, G, B)
      black = pygame.Color(0, 0, 0)
      white = pygame.Color(255, 255, 255)
      red = pygame.Color(255, 0, 0)
      green = pygame.Color(0, 255, 0)
      blue = pygame.Color(0, 0, 255)


      # FPS (frames per second) controller
      fps_controller = pygame.time.Clock()


      # Game variables
      snake_pos = [100, 50]
      snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

      food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
      food_spawn = True

      direction = 'RIGHT'
      change_to = direction

      score = 0


      # Game Over
      def game_over():
          my_font = pygame.font.SysFont('arial', 90)
          game_over_surface = my_font.render('YOU DIED', True, white)
          game_over_rect = game_over_surface.get_rect()
          game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
          game_window.fill(black)
          game_window.blit(game_over_surface, game_over_rect)
          show_score(0, white, 'times', 20)
          pygame.display.flip()
          time.sleep(3)
          pygame.quit()
          sys.exit()


      # Score
      def show_score(choice, color, font, size):
          score_font = pygame.font.SysFont(font, size)
          score_surface = score_font.render('Score : ' + str(score), True, color)
          score_rect = score_surface.get_rect()
          if choice == 1:
              score_rect.midtop = (frame_size_x/10, 15)
          else:
              score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
          game_window.blit(score_surface, score_rect)
          # pygame.display.flip()


      # Main logic
      while True:
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
              # Whenever a key is pressed down
              elif event.type == pygame.KEYDOWN:
                  # W -> Up; S -> Down; A -> Left; D -> Right
                  if event.key == pygame.K_UP or event.key == ord('w'):
                      change_to = 'UP'
                  if event.key == pygame.K_DOWN or event.key == ord('s'):
                      change_to = 'DOWN'
                  if event.key == pygame.K_LEFT or event.key == ord('a'):
                      change_to = 'LEFT'
                  if event.key == pygame.K_RIGHT or event.key == ord('d'):
                      change_to = 'RIGHT'
                  # Esc -> Create event to quit the game
                  if event.key == pygame.K_ESCAPE:
                      pygame.event.post(pygame.event.Event(pygame.QUIT))

          # Making sure the snake cannot move in the opposite direction instantaneously
          if change_to == 'UP' and direction != 'DOWN':
              direction = 'UP'
          if change_to == 'DOWN' and direction != 'UP':
              direction = 'DOWN'
          if change_to == 'LEFT' and direction != 'RIGHT':
              direction = 'LEFT'
          if change_to == 'RIGHT' and direction != 'LEFT':
              direction = 'RIGHT'

          # Moving the snake
          if direction == 'UP':
              snake_pos[1] -= 10
          if direction == 'DOWN':
              snake_pos[1] += 10
          if direction == 'LEFT':
              snake_pos[0] -= 10
          if direction == 'RIGHT':
              snake_pos[0] += 10

          # Snake body growing mechanism
          snake_body.insert(0, list(snake_pos))
          if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
              score += 1
              food_spawn = False
          else:
              snake_body.pop()

          # Spawning food on the screen
          if not food_spawn:
              food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
          food_spawn = True

          # GFX
          game_window.fill(black)
          for pos in snake_body:
              # Snake body
              # .draw.rect(play_surface, color, xy-coordinate)
              # xy-coordinate -> .Rect(x, y, size_x, size_y)
              pygame.draw.rect(game_window, red, pygame.Rect(pos[0], pos[1], 10, 10))

          # Snake food
          pygame.draw.rect(game_window, green, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

          # Game Over conditions
          # Getting out of bounds
          if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
              game_over()
          if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
              game_over()
          # Touching the snake body
          for block in snake_body[1:]:
              if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                  game_over()

          show_score(1, white, 'consolas', 20)
          # Refresh game screen
          pygame.display.update()
          # Refresh rate
          fps_controller.tick(difficulty)


   else:
      print("-"*148)
      print('''SORRY ): NO SUCH GAME EXISTS .........
      PLEASE CHECK YOUR GAME NUMBER AND TRY AGAIN''')
      print("-"*148)
      print()

print("THANK YOU FOR PLAYING !!!!! HOPE YOU JOIN US SOON ")
      

      
      
