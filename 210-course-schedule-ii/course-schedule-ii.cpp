class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> result;
        vector<int> in_degree(numCourses,0);
        vector<int> *adj_list;
        adj_list = new vector<int> [numCourses];

        for(auto node: prerequisites)
        {
            adj_list[node[1]].push_back(node[0]);
        }

        // add courses with no dep to queue
        std::queue<int> queue;

        // add in degree for nodes with prereqs
        for(int i {}; i <numCourses; i++)
        {
            for(auto neighb : adj_list[i])
            {
                in_degree[neighb]++;
            }
        }

        for(int i {}; i<numCourses; i++)
        {
            if(in_degree[i] == 0)
            {
                queue.push(i);
            }
        }

        // BFS topological sort
        while(!(queue.empty()))
        {
            auto curr_course = queue.front();
            queue.pop();
            result.push_back(curr_course);

            for(auto neighb : adj_list[curr_course])
            {
                in_degree[neighb]--;

                if(in_degree[neighb] == 0)
                {
                    queue.push(neighb);
                }
            }
        }

        if(result.size() == numCourses)
        {
            return result;
        }

        return {};
    }
};