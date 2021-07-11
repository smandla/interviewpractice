def awardBudgetCuts(grants, budget):
    n = len(grants)
    grants.sort()
    grantsLeft = budget
    for i, currentSalary in enumerate(grants):
        employeesLeft = n - i
        #print(employeesLeft)
        candidateSpend = employeesLeft * currentSalary
        if candidateSpend > grantsLeft:
            return grantsLeft/employeesLeft
        grantsLeft -= currentSalary
    return 0

grants = [2, 100, 50, 120, 1000]
budget = 190
grants1 = [100, 300, 200, 400]
budget1 = 800
print(awardBudgetCuts(grants1, budget1))