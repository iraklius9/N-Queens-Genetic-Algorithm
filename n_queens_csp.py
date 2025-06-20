def print_board(solution, N):
    for row in range(N):
        line = ['Q' if solution[row] == col else '.' for col in range(N)]
        print(' '.join(line))
    print()

def is_safe(row, col, queens):
    for r in range(row):
        c = queens[r]
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True

def solve_n_queens(N):
    queens = [-1] * N
    solution = []
    def backtrack(row):
        if row == N:
            solution.extend(queens)
            return True
        for col in range(N):
            if is_safe(row, col, queens):
                queens[row] = col
                if backtrack(row + 1):
                    return True
                queens[row] = -1  
        return False
    found = backtrack(0)
    return solution if found else None

def main():
    print("N-Queens Problem as CSP (Backtracking)")
    N = 8
    solution = solve_n_queens(N)
    if solution:
        print(f"\nSolution for N={N}:")
        print_board(solution, N)
    else:
        print(f"No solution exists for N={N} (unsolvable).")
    print("\nAlgorithm explanation:")
    print("- Place queens row by row, trying all columns.")
    print("- If a row has no valid columns, backtrack to previous row.")
    print("- If all rows are filled, a solution is found.")
    print("- If all options are exhausted, the problem is unsolvable for this N.")

if __name__ == "__main__":
    main()

"""
N Queens ამოცანის ახსნა (ქართული)
==================================

ამოცანის არსი:
--------------
N Queens არის კლასიკური თავსატეხი, სადაც მიზანია N დედოფლის ისე განთავსება NxN ჭადრაკის დაფაზე, 
რომ არცერთი მათგანი არ ემუქრებოდეს ერთმანეთს (არც ერთ სვეტში, მწკრივში ან დიაგონალზე).

მიდგომა და ალგორითმი:
---------------------
- თითოეული დედოფალი განთავსებულია ცალკე მწკრივში (ცვლადი = მწკრივის ინდექსი).
- თითოეული ცვლადის მნიშვნელობაა სვეტის ინდექსი (0-დან N-1-მდე).
- შეზღუდვები: არცერთი ორი დედოფალი არ უნდა იყოს ერთ სვეტში, მთავარ ან მეორეულ დიაგონალზე.
- გამოიყენება ბექტრეკინგი: დედოფლები განთავსდება მწკრივების მიხედვით, ყოველი ახალი დადებისას მოწმდება შეზღუდვები. 
თუ რომელიმე მწკრივში ვეღარ ვპოულობთ სწორ სვეტს, ვბრუნდებით უკან (backtrack).

ბლოკირების (dead end) და ამოუხსნელობის შემოწმება:
-----------------------------------------------
- თუ რომელიმე მწკრივში ყველა სვეტი დაკავებულია ან კონფლიქტურია, ხდება ბექტრეკინგი წინა მწკრივზე.
- თუ ყველა ვარიანტი ამოიწურა და პირველი მწკრივიდანაც ვეღარ ვაგრძელებთ, ამოცანა ამოუხსნელია მოცემული N-სთვის (N < 4-ის გარდა).

ეს პროგრამა პოულობს პირველივე სწორ განლაგებას ნებისმიერი N-სთვის (N ≥ 1).
""" 