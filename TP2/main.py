from src.utils import destructure_data
from src.genetic.genetic_algorithm import genetic_algorithm
import json

def main(): 

    with open('./config.json', 'r') as f:
        data = json.load(f)

    palette, N, target_color, selection_type, crossing_type, mutation_type, mutation_pm, select_new_generation_type, K, max_generations, d_error, time = destructure_data(data)

    print("-------------TP2-------------\n"
          "Paleta de colores\n"
          f"{palette}\n"
          f"Color deseado: {target_color}"
          )

    time_passed, finish_condition, best_subject, best_of_each_generation, generation = genetic_algorithm(palette, N, target_color, selection_type,
                      crossing_type, mutation_type, mutation_pm,
                      select_new_generation_type, K, max_generations, d_error, time)
    
    print(f"TIEMPO: {time_passed}")
    
    print("------------GANADOR------------\n"
          f"{finish_condition}\n"
          f"{best_subject}\n")

if __name__ == "__main__":
    main()