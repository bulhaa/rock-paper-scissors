# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

    
def anti_quincy(prev_play, opponent_history=[], guesses=[], results=[]):
    
    n_losses = 0
    failure_rate = 0

    opponent_history.append(prev_play)
    
    n_count = -10
    opponent_history_l = opponent_history[n_count:]
    guesses_l = guesses[n_count:]
      

    guess = "P"
    if len(opponent_history_l) > 1:
        # # store results
        p1_play = guesses_l[-1]
        p2_play = opponent_history_l[-1]
        if p1_play == p2_play:
            results.append({"result": "tie"})
        elif (p1_play == "P" and p2_play == "R") or (
                p1_play == "R" and p2_play == "S") or (p1_play == "S"
                                                       and p2_play == "P"):
            results.append({"result": "win"})
        elif p2_play == "P" and p1_play == "R" or p2_play == "R" and p1_play == "S" or p2_play == "S" and p1_play == "P":
            results.append({"result": "loss"})
            
        results_l = results[n_count:]
                
        # get number of losses
        for result in results_l:
            if result["result"] == "win":
                pass
            elif result["result"] == "loss":
                n_losses += 1
            elif result["result"] == "tie":
                n_losses += 1
            else:
                print('error')
                
        failure_rate = n_losses / len(results_l) * 100 if len(results_l) else 0
        
        
        last_two = "".join(opponent_history_l[-2:])
        if last_two == "R":
            guess = "S"
        elif last_two == "RR":
            guess = "S"
        elif last_two == "RP":
            guess = "S"
        elif last_two == "PP":
            guess = "R"
        elif last_two == "PS":
            guess = "P"
        elif last_two == "SR":
            guess = "P"
    
    guesses.append(guess)
  
    
    return failure_rate
    
def anti_abbey(prev_play, real_guesses, opponent_history=[], guesses=[], results=[]):
    
    play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]
    
    prev_char = ""
    for i, char in enumerate(real_guesses):
        if i != 0:
            last_two = prev_char + char
            play_order[0][last_two] += 1
        prev_char = char
    
    n_losses = 0
    failure_rate = 0

    opponent_history.append(prev_play)
    
    n_count = -20
    opponent_history_l = opponent_history[n_count:]
    guesses_l = guesses[n_count:]
      

    guess = "S"
    if len(opponent_history_l) > 1:
        # # store results
        p1_play = guesses_l[-1]
        p2_play = opponent_history_l[-1]
        if p1_play == p2_play:
            results.append({"result": "tie"})
        elif (p1_play == "P" and p2_play == "R") or (
                p1_play == "R" and p2_play == "S") or (p1_play == "S"
                                                       and p2_play == "P"):
            results.append({"result": "win"})
        elif p2_play == "P" and p1_play == "R" or p2_play == "R" and p1_play == "S" or p2_play == "S" and p1_play == "P":
            results.append({"result": "loss"})
        
        results_l = results[n_count:]
                
        # get number of losses
        for result in results_l:
            if result["result"] == "win":
                pass
            elif result["result"] == "loss":
                n_losses += 1
            elif result["result"] == "tie":
                n_losses += 1
            else:
                print('error')
                
        failure_rate = n_losses / len(results_l) * 100 if len(results_l) else 0
        
        prev = real_guesses[-1:][0]

        potential_plays = [
            prev + "R",
            prev + "P",
            prev + "S",
        ]

        sub_order = {
            k: play_order[0][k]
            for k in potential_plays if k in play_order[0]
        }

        prediction = max(sub_order, key=sub_order.get)[-1:]

        ideal_response = {'P': 'R', 'R': 'S', 'S': 'P'}
        guess = ideal_response[prediction]
    
    guesses.append(guess)
    
    return failure_rate
    
def anti_kris(prev_play, prev_guess, opponent_history=[], guesses=[], results=[], 
          play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]):
    
    n_losses = 0
    failure_rate = 0

    opponent_history.append(prev_play)
    
    n_count = -10
    opponent_history_l = opponent_history[n_count:]
    guesses_l = guesses[n_count:]
      

    guess = "P"
    if len(opponent_history_l) > 1:
        # # store results
        p1_play = guesses_l[-1]
        p2_play = opponent_history_l[-1]
        if p1_play == p2_play:
            results.append({"result": "tie"})
        elif (p1_play == "P" and p2_play == "R") or (
                p1_play == "R" and p2_play == "S") or (p1_play == "S"
                                                       and p2_play == "P"):
            results.append({"result": "win"})
        elif p2_play == "P" and p1_play == "R" or p2_play == "R" and p1_play == "S" or p2_play == "S" and p1_play == "P":
            results.append({"result": "loss"})
        
        results_l = results[n_count:]
                
        # get number of losses
        for result in results_l:
            if result["result"] == "win":
                pass
            elif result["result"] == "loss":
                n_losses += 1
            elif result["result"] == "tie":
                n_losses += 1
            else:
                print('error')
                
        failure_rate = n_losses / len(results_l) * 100 if len(results_l) else 0
        
        prev = prev_guess
        if prev == '':
            prev = "R"
        ideal_response = {'P': 'R', 'R': 'S', 'S': 'P'}
        guess = ideal_response[prev]
    
  
    guesses.append(guess)
    
    return failure_rate
    
def anti_mrugesh(prev_play, real_guesses, opponent_history=[], guesses=[], results=[], 
          play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]):
    
    n_losses = 0
    failure_rate = 0

    opponent_history.append(prev_play)
    
    n_count = -10
    opponent_history_l = opponent_history[n_count:]
    guesses_l = guesses[n_count:]
      

    guess = "P"
    if len(opponent_history_l) > 1:
        # # store results
        p1_play = guesses_l[-1]
        p2_play = opponent_history_l[-1]
        if p1_play == p2_play:
            results.append({"result": "tie"})
        elif (p1_play == "P" and p2_play == "R") or (
                p1_play == "R" and p2_play == "S") or (p1_play == "S"
                                                       and p2_play == "P"):
            results.append({"result": "win"})
        elif p2_play == "P" and p1_play == "R" or p2_play == "R" and p1_play == "S" or p2_play == "S" and p1_play == "P":
            results.append({"result": "loss"})
        
        results_l = results[n_count:]
                
        # get number of losses
        for result in results_l:
            if result["result"] == "win":
                pass
            elif result["result"] == "loss":
                n_losses += 1
            elif result["result"] == "tie":
                n_losses += 1
            else:
                print('error')
                
        failure_rate = n_losses / len(results_l) * 100 if len(results_l) else 0
        
        
        last_ten = real_guesses[-10:]
        most_frequent = max(set(last_ten), key=last_ten.count)
        if most_frequent == '':
            most_frequent = "S"

        ideal_response = {'P': 'R', 'R': 'S', 'S': 'P'}
        guess = ideal_response[most_frequent]
    
  
    guesses.append(guess)
    
    return failure_rate

def player(prev_play, opponent_history=[], guesses=[], results=[], storage=[{"algorithm": 0}], 
          play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]):

    n_count = -100
    
    opponent_history.append(prev_play)
    opponent_history_l = opponent_history[n_count:]
    guesses_l = guesses[n_count:]
    
    
    guess = "S"
    if len(opponent_history_l) > 1:
        
        anti_quincy_failure_rate = anti_quincy(prev_play)
        anti_abbey_failure_rate = anti_abbey(prev_play, guesses_l)
        anti_kris_failure_rate = anti_kris(prev_play, guesses_l[-1:][0])
        anti_mrugesh_failure_rate = anti_mrugesh(prev_play, guesses_l)
        
        # store results
        p1_play = guesses_l[-1]
        p2_play = opponent_history_l[-1]
        if p1_play == p2_play:
            results.append({"result": "tie", "algorithm": storage[0]["algorithm"]})
        elif (p1_play == "P" and p2_play == "R") or (
                p1_play == "R" and p2_play == "S") or (p1_play == "S"
                                                       and p2_play == "P"):
            results.append({"result": "win", "algorithm": storage[0]["algorithm"]})
        elif p2_play == "P" and p1_play == "R" or p2_play == "R" and p1_play == "S" or p2_play == "S" and p1_play == "P":
            results.append({"result": "loss", "algorithm": storage[0]["algorithm"]})

        results_l = results[n_count:]
        
        # # get number of tries
        # n_tries = [0, 0, 0, 0]
        # for result in results_l:
        #     n_tries[result["algorithm"]] += 1
                
        # # get number of losses
        # n_losses = [0, 0, 0, 0]
        # for result in results_l:
        #     if result["result"] == "win":
        #         pass
        #     elif result["result"] == "loss":
        #         n_losses[result["algorithm"]] += 1
        #     elif result["result"] == "tie":
        #         n_losses[result["algorithm"]] += 1
        #     else:
        #         print('error')
                
        # failure_rate = [n_losses[i] / (n_tries[i]+ 0) if n_tries[i] else 0 for i, tries in enumerate(n_tries)  ]
        
        failure_rate = [anti_abbey_failure_rate, anti_quincy_failure_rate, anti_kris_failure_rate, anti_mrugesh_failure_rate]
   
        
        if failure_rate[0] == min(failure_rate) or min(failure_rate) > 10:
            storage[0]["algorithm"] = 0
            prev = guesses_l[-1:][0]

            last_two = "".join(guesses_l[-2:])
            if len(last_two) == 2:
                play_order[0][last_two] += 1

            potential_plays = [
                prev + "R",
                prev + "P",
                prev + "S",
            ]

            sub_order = {
                k: play_order[0][k]
                for k in potential_plays if k in play_order[0]
            }

            prediction = max(sub_order, key=sub_order.get)[-1:]

            ideal_response = {'P': 'R', 'R': 'S', 'S': 'P'}
            guess = ideal_response[prediction]
        elif failure_rate[1] == min(failure_rate):
            storage[0]["algorithm"] = 1
            last_two = "".join(opponent_history_l[-2:])
            if last_two == "R":
                guess = "S"
            elif last_two == "RR":
                guess = "S"
            elif last_two == "RP":
                guess = "S"
            elif last_two == "PP":
                guess = "R"
            elif last_two == "PS":
                guess = "P"
            elif last_two == "SR":
                guess = "P"
        elif failure_rate[2] == min(failure_rate):
            storage[0]["algorithm"] = 2
            prev = guesses_l[-1:][0]
            if prev == '':
                prev = "R"
            ideal_response = {'P': 'R', 'R': 'S', 'S': 'P'}
            guess = ideal_response[prev]
        else:
            storage[0]["algorithm"] = 3
            last_ten = guesses_l[-10:]
            most_frequent = max(set(last_ten), key=last_ten.count)
            if most_frequent == '':
                most_frequent = "S"

            ideal_response = {'P': 'R', 'R': 'S', 'S': 'P'}
            guess = ideal_response[most_frequent]
            
    guesses.append(guess)
  
    return guess

