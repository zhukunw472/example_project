# Kmeans algorithm frmo scratch
#Define a function for assigning each point in the dataset to a centroid (dataset of points where each point has x and y coordinate)
def renew_assignments(data, centroids):
    assignment_list = []
    for point in data:
        #closest_centroid = centroids[0]
        closest_dist = (centroids[0][0]-point[0])**2 + (centroids[0][1]-point[1])**2
        #print(closest_dist)
        centroid_index = 0
        for centroid in centroids:
            if ((centroid[0]-point[0])**2 + (centroid[1]-point[1])**2) <= closest_dist:
                closest_dist = ((centroid[0]-point[0])**2 + (centroid[1]-point[1])**2)
                centroid_id = centroid_index
                #print(centroid_id)
            centroid_index += 1
        assignment_list.append(centroid_id)
        #print(assignment_list)
    return assignment_list 

#Define a function for updating the centroids (return a list of centroids and the list will be renewed)
def renew_centroids(data, num_clusters, assignments): #assignments here is the assignment_list that is returned by last fcn
    centroid_list = []
    #print(len(num_clusters))
    for i in range(len(num_clusters)): #say 3 clusters, i could be in range(0, 3)
        x_tot = 0
        y_tot = 0
        num_pts_cluster = 0
        for index in range(len(data)):
            if assignments[index] == i:
                num_pts_cluster += 1
                x_tot += data[index][0]
                y_tot += data[index][1]
        x_mean = x_tot / (num_pts_cluster)
        y_mean = y_tot / (num_pts_cluster)
        vec = [x_mean, y_mean]
        #print(num_pts_cluster)
        centroid_list.append(vec)
    #print(centroid_list)
    return centroid_list

#Define the K-means function 
def Kmeans(data, centroids): #centroids is a list of K-points as initial centroids
    list_centroidslist = []
    for i in range(0, 100): 
        if i > 0:
            Assignments = renew_assignments(data, list_centroidslist[i-1])
            #print(list_centroidslist[i-1])
            Centroids = renew_centroids(data, list_centroidslist[i-1], Assignments)
            Centroids = np.array(Centroids)
            list_centroidslist.append(Centroids)
            #print(list_centroidslist)
            #Get the round where the list of centroid_lists starts to have same centroid_list, the centroids starts to be fixed ones 
            if (list_centroidslist[i-2] != list_centroidslist[i-1]).any and (Centroids == list_centroidslist[i-1]).any:
                critical_index = i
                #print(critical_index)
        else:
            #Do the same thing but this is for the very beginning round
            Assignments = renew_assignments(data, centroids)
            Centroids = renew_centroids(data, centroids, Assignments)
            Centroids = np.array(Centroids)
            list_centroidslist.append(Centroids)
            #print(Centroids)
    
    #find unique elements in Assignments of all dots
    list_unique_group = np.unique(Assignments)
    #print(list_unique_group)
    #print(len(Assignments))
    
    #Get index of each group
    list_groups = []
    for j in list_unique_group:
        current_group = []
        for i in range(len(Assignments)):
            if Assignments[i] == j:
                current_group.append(i)
        list_groups.append(current_group)
    
    #Plot out each group of points
    for group in list_groups:
        m = group
        plt.scatter(data[m, 0], data[m, 1])
    
    #Plot the final fixed centroids
    plt.scatter(list_centroidslist[critical_index][:, 0], list_centroidslist[critical_index][:, 1])
    plt.show()


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    #Initialize three bivariate Gaussians as shown in the question
    np.random.seed(1)
    mean = np.array([3.0,1.0])
    cov = np.array([[0.9,0.3],[0.3,0.9]])
    X0 = np.random.multivariate_normal(mean,cov,1000)
    mean = np.array([-1.0,3.0])
    cov = np.array([[0.9,0.3],[0.3,0.9]])
    X1 = np.random.multivariate_normal(mean,cov,1000)
    mean = np.array([-5.0,2.0])
    cov = np.array([[0.9,0.3],[0.3,0.9]])
    X2 = np.random.multivariate_normal(mean,cov,1000) 
    X = np.concatenate((X0,X1,X2),axis=0)  #X is the data
    print(X.shape)

    #Set up the centroids
    CENTROIDS = np.array([[0.4, 0.3], [0.1, 0.4], [-2.0, 2.0]]).reshape(3, 2)
    #print(CENTROIDS[0][0])

    #Test the Kmeans algorithm by calling the function
    Kmeans(X, CENTROIDS)
