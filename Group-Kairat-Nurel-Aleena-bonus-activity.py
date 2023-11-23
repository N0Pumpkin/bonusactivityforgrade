#Nurel, Kairat, Aleena

#made Nurel
task_dep_sc = {                                                                                     #dictionary
    'T3': ['T2', 'T1'],
    'T2': ['T1'],
    'T1': []
    # 'T3': ['T2'],
    # 'T2': ['T1', 'T3'],
    # 'T1': []
    #
    # 'T3': ['T2'],
    # 'T2': ['T1'],
    # 'T1': [],
    # 'T0': []
    #
    # 'T4': ['T3'],
    # 'T3': ['T2', 'T1'],
    # 'T2': ['T1'],
    # 'T1': []
}

                                                                                                    #function to make mirror of dictionary
def mirror(task_dep_sc):
    dependency_tasks = dict()                                                                       #add empty dict
    for key, values in task_dep_sc.items():                                                         # Iteration by key-value pairs in the sent task_dep_sc dictionary.
        for value in values:                                                                        #For each value in the task dependency list.
            if value not in dependency_tasks.keys():                                                # Check if the value in the backlink dictionary exists.
                dependency_tasks[value] = []                                                        # If no value is present, create a new key with an empty list.
            dependency_tasks[value].append(key)                                                     # Adds the current task to the list of inverse dependencies for the value.
    return dependency_tasks                                                                         # Returns the backlink dictionary.
                                                                                                    #function to remove values from dictionary

# Made Kairat
def remove_value(list_tasks, Tx, task_dep_sc):
    empty = []                                                                                      # Initializes the list to store tasks without dependencies.
    for task in list_tasks:                                                                         # Iterate by task in list_tasks list.
        if Tx in task_dep_sc[task]:                                                                 # Check if Tx is present in the dependencies of the current task.
            task_dep_sc[task] = [value for value in task_dep_sc[task] if value != Tx]               # Removes Tx from the list of dependencies of the current task.
            if task_dep_sc[task] == []:                                                             # Check if the dependency list is empty after deletion.
                empty.append(task)                                                                  # If empty, add the task to the empty list.
    return task_dep_sc, empty                                                                       # Returns the updated task dictionary and task list without dependencies.

#Made Aleena
def schedule_fixed(task_dep_sc):
    dependency_tasks = mirror(task_dep_sc)                                                          #creating mirror of dictionary
    tasks_sequence = []                                                                             #the order of tasks
    while True:
        ready_to_execute = [key for key, values in task_dep_sc.items() if not values]               # Create a list of tasks ready to perform (without dependencies).
        if len(ready_to_execute) == 0:                                                              # Validation, if all tasks depend on others, it is not possible to generate a schedule.
            break                                                                                   #if all tasks depend on others then will be impossible to schedule
        ready_to_execute = sorted(ready_to_execute)                                                 #sorting the tasks in order
        tasks_sequence += ready_to_execute                                                          # Add finished tasks to the execution order list.
        for task in ready_to_execute:                                                               # Remove completed tasks from the source dictionary.
            del task_dep_sc[task]                                                                   #deleting the executed task


                                                                                                    # Update dependencies for other tasks.
        for task in ready_to_execute:                                                               #deleting the executed task from previous
            if task in dependency_tasks.keys():                                                     #checks if task is a previous
                removed_executed = remove_value(dependency_tasks[task], task, task_dep_sc)[1]
                for elem in removed_executed:
                    if elem in dependency_tasks:
                        dependency_tasks[elem] = [value for value in dependency_tasks[elem] if value != task]


    if task_dep_sc:                                                                                 # Check if the failed tasks are still in the original dictionary.
        print([])                                                                                   # If there are outstanding tasks, you cannot create a schedule.
    else:
        print(tasks_sequence)                                                                       #return the ordered tasks
schedule_fixed(task_dep_sc)