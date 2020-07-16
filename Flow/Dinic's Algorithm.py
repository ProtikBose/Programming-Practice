# multiple source,multiple sink


def solution1(entrances,exits,path):
    
    residualGraph = path[:]
    currentFlow = 0    
    prevFlow = -1
    
    while prevFlow != currentFlow:
        
        prevFlow = currentFlow

        for j in entrances:
            
            visited = []
            augmentedPath = []
            node = j                    
            
            while 1:
                
                findUnvisited = False   
                visited.append(node)      
                maximum = 0
                index = 0
                
                for i in range(len(residualGraph[node])):
                    if residualGraph[node][i] > maximum and i not in visited:
                        maximum = residualGraph[node][i]
                        index = i
                        findUnvisited = True
                
                if findUnvisited:
                    augmentedPath.append(node)
                    node = index
                
                elif not augmentedPath:
                    break   
                
                else:
                    node = augmentedPath.pop()
                
                # DFS part
                if node in exits:
                    augmentedPath.append(node)
                    minimum = 2000000
                    for j in range(len(augmentedPath) - 1):
                        if residualGraph[augmentedPath[j]][augmentedPath[j + 1]] < minimum:
                            minimum = residualGraph[augmentedPath[j]][augmentedPath[j + 1]]
                    currentFlow += minimum
                    for j in range(len(augmentedPath) - 2):
                        residualGraph[augmentedPath[j]][augmentedPath[j + 1]] -= minimum
                        residualGraph[augmentedPath[j + 1]][augmentedPath[j]] += minimum
                    residualGraph[augmentedPath[len(augmentedPath) - 2]][augmentedPath[len(augmentedPath) - 1]] -= minimum
                    break

    return currentFlow

####################################################################################################################################

# single source,single sink

def solution2(entrances,exits,path):
    
    residualGraph = path[:]
    currentFlow = 0    
    prevFlow = -1
    
    while prevFlow != currentFlow:
        
        prevFlow = currentFlow

        
            
        visited = []
        augmentedPath = []
        node = entrances                    
            
        while 1:
                
            findUnvisited = False   
            visited.append(node)      
            maximum = 0
            index = 0
                
            for i in range(len(residualGraph[node])):
                if residualGraph[node][i] > maximum and i not in visited:
                    maximum = residualGraph[node][i]
                    index = i
                    findUnvisited = True
                
            if findUnvisited:
                augmentedPath.append(node)
                node = index
                
            elif not augmentedPath:
                break   
                
            else:
                node = augmentedPath.pop()
                
            # DFS part
            if node == exits:
                augmentedPath.append(node)
                minimum = 2000000
                for j in range(len(augmentedPath) - 1):
                    if residualGraph[augmentedPath[j]][augmentedPath[j + 1]] < minimum:
                        minimum = residualGraph[augmentedPath[j]][augmentedPath[j + 1]]
                currentFlow += minimum
                for j in range(len(augmentedPath) - 2):
                    residualGraph[augmentedPath[j]][augmentedPath[j + 1]] -= minimum
                    residualGraph[augmentedPath[j + 1]][augmentedPath[j]] += minimum
                residualGraph[augmentedPath[len(augmentedPath) - 2]][augmentedPath[len(augmentedPath) - 1]] -= minimum
                break

    return currentFlow


print(solution1([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))

C = [[ 0, 3, 3, 0, 0, 0 ],  
     [ 0, 0, 2, 3, 0, 0 ],  
     [ 0, 0, 0, 0, 2, 0 ],  
     [ 0, 0, 0, 0, 4, 2 ],  
     [ 0, 0, 0, 0, 0, 2 ],  
     [ 0, 0, 0, 0, 0, 3 ]]  

source = 0  
sink = 5

print(solution2(source,sink,C))