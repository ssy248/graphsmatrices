
def centrality(v, sp_mat):
    row = sp_mat[v]
    mn = np.mean(row)
    recip = 1/(mn)
    return recip

class ShortestPath(Kernel):

    _graph_bins = dict()

    def __init__(self, n_jobs=None,
                 normalize=False,
                 verbose=False,
                 with_labels=True,
                 algorithm_type="auto"):
        """Initialize a `shortest_path` kernel."""
        super(ShortestPath, self).__init__(
            n_jobs=n_jobs, normalize=normalize, verbose=verbose)

        self.with_labels = with_labels
        self.algorithm_type = algorithm_type
        self._initialized.update({"with_labels": False, "algorithm_type": False})
        
        

    def initialize(self):
        """Initialize all transformer arguments, needing initialization."""
        if not self._initialized["n_jobs"]:
            if self.n_jobs is not None:
                warnings.warn('no implemented parallelization for ShortestPath')
            self._initialized["n_jobs"] = True

        if not self._initialized["algorithm_type"]:
            if self.algorithm_type == "auto":
                self._graph_format = "auto"
            elif self.algorithm_type == "floyd_warshall":
                self._graph_format = "adjacency"
            elif self.algorithm_type == "dijkstra":
                self._graph_format = "dictionary"
            else:
                raise ValueError('Unsupported "algorithm_type"')

        if not self._initialized["with_labels"]:
            if self.with_labels:
                self._lt = "vertex"
                self._lhash = lhash_labels
                self._decompose_input = decompose_input_labels
            else:
                self._lt = "none"
                self._lhash = lhash
                self._decompose_input = decompose_input
    
    def parse_input(self, X):
        # returns sp_counts: dictionary for each vertex holds the counts of shortest path tuples
        
        # add: centrality : centrality scores of each vertex 
        i=0
        for (idx, x) in enumerate(iter(X)):
            if type(x) is Graph:
                spm_data = x.build_shortest_path_matrix(self.algorithm_type, labels=self._lt)
                
                centralities = {}
                # calculate centralities 
                for vertex in range(nvert):
                    cent = centrality(vertex, spm_data)
                    centralities[vertex] = cent
                
        S, L = self._decompose_input(spm_data)
                sp_counts[i] = dict()
                for u in range(S.shape[0]):
                    for v in range(S.shape[1]):
                        if u == v or S[u, v] == float("Inf"):
                            continue
                        label = self._lhash(S, u, v, *L)
                        if label not in self._enum:
                            if self._method_calling == 1:
                                idx = len(self._enum)
                                self._enum[label] = idx
                            elif self._method_calling == 3:
                                if label not in self._Y_enum:
                                    idx = len(self._enum) + len(self._Y_enum)
                                    self._Y_enum[label] = idx
                                else:
                                    idx = self._Y_enum[label]
                        else:
                            idx = self._enum[label]
                        if idx in sp_counts[i]:
                            sp_counts[i][idx] += 1
                        else:
                            sp_counts[i][idx] = 1
            

    def fit_transform(self, X, y=None):
        """Fit and transform, on the same dataset.
        Parameters
        ----------
        X : iterable
            Each element must be an iterable with at most three features and at
            least one. The first that is obligatory is a valid graph structure
            (adjacency matrix or edge_dictionary) while the second is
            node_labels and the third edge_labels (that fitting the given graph
            format).
        y : Object, default=None
            Ignored argument, added for the pipeline.
        Returns
        -------
        K : numpy array, shape = [n_targets, n_input_graphs]
            corresponding to the kernel matrix, a calculation between
            all pairs of graphs between target an features
        """
        self._method_calling = 2
        self.fit(X)

        # calculate feature matrices.
        phi_x = np.zeros(shape=(self._nx, len(self._enum)))

        for i in self.X.keys():
            for j in self.X[i].keys():
                phi_x[i, j] = self.X[i][j]

        # Transform - calculate kernel matrix
        self._phi_X = phi_x
        km = np.dot(phi_x, phi_x.T)

        self._X_diag = np.diagonal(km)
        if self.normalize:
            return np.divide(km, np.sqrt(np.outer(self._X_diag, self._X_diag)))
        else:
            return km
