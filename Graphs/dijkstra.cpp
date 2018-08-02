#include <iostream>
#include <vector>
using namespace std;

const int INFINITY = 1000000;
const int NUM_VERTICES = 6;


class Graph
{
    public:
        int adjMatrix[6][6] = {{0, 120, 150, INFINITY, INFINITY, 500},
                               {120, 0, INFINITY, 75, INFINITY, 350},
                               {150, INFINITY, 0, INFINITY, 250, INFINITY},
                               {INFINITY, 75, INFINITY, 0, 150, INFINITY},
                               {INFINITY, INFINITY, 250, 150, 0, INFINITY},
                               {500, 350, INFINITY, INFINITY, INFINITY, 0}
                               };

        int numVertices = NUM_VERTICES;

        int edgeWeight(int a, int b)
        {
            return adjMatrix[a][b];
        }

        /**
        Get neighbors of vertex v.
        A neighbor is a vertex that has an edge to v and is not v itself and is not inifinity.
        */
        vector<int> neighborsOf(int v)
        {
            vector<int> neighbors;
            for (int i = 0; i < numVertices; i++)
            {
                if (i != v && edgeWeight(v, i) != INFINITY)
                {
            //      cout << "Neighor of " << v << " is " << i << endl;
                    neighbors.push_back(i);
                }
            }
            return neighbors;
        }

        void displayMatrix()
        {
            for (int v = 0; v < 6; v++)
            {
                for (int u = 0; u < 6; u++)
                {
                    cout << adjMatrix[v][u] << " | ";
                }
                cout << endl;
            }
        }

        int * dijkstra(int source) // source to destination
        {
            bool visited[NUM_VERTICES];    // keep track of visited nodes, in the vertexSet

            int * distance;
            distance = new int[NUM_VERTICES];    // cost of path, the weight

            // initialize
            for (int v = 0; v < NUM_VERTICES; v++)
            {
                distance[v] = INFINITY;
                visited[v] = false;
            }
            distance[source] = 0;         // initially, source is SFO (0)

            // keep track of current node
            int currentVertex = source;

            while (true)
            {
                visited[currentVertex] = true;

                // Iterate over all neighbors of currentVertex
                vector<int> neighbors = neighborsOf(currentVertex);
                for (unsigned int i = 0; i < neighbors.size(); i++)
                {
                    int u = neighbors[i];

                    if (visited[u])
                    {
                        continue;
                    }
                    // relax the distances
                    /* same as:
                    Check weight[u] for all u not in vertexSet
                    for (all vertices u not in vertexSet)
                    if (weight[u] > weight[v] + matrix[v][u])
                        weight[u] = weight[v] + matrix[v][u]
                    */
                    int newDistance = distance[currentVertex] + edgeWeight(currentVertex, u);
                    distance[u] = min(distance[u], newDistance);
                //  cout << "NEIGHBOR OF " << currentVertex << " is " << u << " with distance " << distance[u] << endl;
                }

                // Find the next vertex to visit. It should be unvisited and have minimum entry in distance.

                int minWeight = INFINITY;
                int minUnVisitedVertex = -1;        // cannot be -1

                for (int v = 0; v < numVertices; v++)
                {
                    if ((!visited[v]) && (distance[v] <= minWeight))
                    {
                        minWeight = distance[v];
                        minUnVisitedVertex = v;
                    }
                }
                // cout << "cheapest unvisited airport: " << minUnVisitedVertex << endl;

                if (minWeight == INFINITY)
                {
                    // There are no more unvisited nodes.
                    break;
                }

                currentVertex = minUnVisitedVertex;
            }

            return distance;
        }

};

int main()
{
    Graph matrix;

    // matrix.displayMatrix();
    // matrix.neighborsOf(0);

    /*
    for (int i = 0; i < matrix.numVertices; i++)
    {
        for (int j = i + 1; j < matrix.numVertices; j++)
        {
            cout << "Lowest cost fares from " << i << " to " << j << " is ";
            cout << matrix.dijkstra(i, j) << endl;
        }
    }
    */

    int * shorttestDistances = matrix.dijkstra(0);

    for (int i =  1; i < matrix.numVertices; i++)
    {
        cout << "Lowest cost fares from SFO" << " to " << i << " is $";
        cout << shorttestDistances[i] << endl;
    }

    return 0;
}

/* SAMPLE OUTPUT
hoeunsim2@Hoeuns-MBP ~/Dropbox/ccsf/courses/cs110c/assignments/Graphs
 % ./a.out
Lowest cost fares from SFO to 1 is $120
Lowest cost fares from SFO to 2 is $150
Lowest cost fares from SFO to 3 is $195
Lowest cost fares from SFO to 4 is $345
Lowest cost fares from SFO to 5 is $470
*/
