# Enter your code here. Read input from STDIN. Print output to STDOUT
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self):
        self.val = "."
        self.left = None
        self.right = None

def parse(st):
    stack = []
    root = TreeNode()
    node = root
    for ch in st:
        if ch == "(":
            stack.append(node)
            tmp = TreeNode()
            if node.left:
                node.right = tmp
            else:
                node.left = tmp
            node = tmp
        elif ch not in ['*', '|', ')']:
            tmp = TreeNode()
            tmp.val = ch
            if node.left:
                node.right = tmp
            else:
                node.left = tmp
        elif ch == '|':
            node.val = "|"
        elif ch == '*':
            node.val = '*'
        elif ch == ")":
            node = stack.pop()
    return root.left


class NfaTrans:
    def __init__(self, initial, final, ch):
        self.initial = initial
        self.final = final
        self.label = ch


class NFA:
    def __init__(self):
        self.vertices = []
        self.start = None
        self.final = self.create_vertex()

    def add_transition(self, initial, final, label):
        self.vertices[initial].append(NfaTrans(initial, final, label))

    def create_vertex(self):
        self.vertices.append([])
        return len(self.vertices) - 1

    def get_edges(self, vertex):
        return self.vertices[vertex]

    def move(self, states, label):
        res = []
        for state in states:
            for edge in self.get_edges(state):
                if edge.label == label:
                    res.append(edge.final)

        return res

    def eclose(self, states):
        eclosure = set()
        stack = []

        for s in states:
            eclosure.add(s)
            stack.append(s)

        while stack:
            cur = stack.pop()
            for edge in self.get_edges(cur):
                if edge.label == 'e' and edge.final not in eclosure:
                    stack.append(edge.final)
                    eclosure.add(edge.final)

        return tuple(eclosure)


class NfaParser:
    def __init__(self, nfa):
        self.nfa = nfa

    def parse(self, root):
        self.nfa.start = self.create_state(root, self.nfa.final)

    def add_transition(self, initial, final, label):
        self.nfa.add_transition(initial, final, label)

    def create_vertex(self):
        return self.nfa.create_vertex()

    def create_state(self, node, o):
        if node.val == "|":
            return self.create_or(node, o)

        if node.val == ".":
            return self.create_con(node, o)

        if node.val == '*':
            return self.create_star(node, o)

        return self.create_basic(node, o)

    def create_basic(self, node, o):
        # print "Creating basic", node.val
        s = self.create_vertex()
        self.add_transition(s, o, node.val)
        return s

    def create_or(self, node, o):
        # print "Creating or"
        start = self.create_vertex()
        left = self.create_state(node.left, o)
        right = self.create_state(node.right, o)
        self.add_transition(start, left, 'e')
        self.add_transition(start, right, 'e')

        return start

    def create_con(self, node, o):
        # print "Creating connection"
        end = self.create_state(node.right, o)
        start = self.create_state(node.left, end)
        return start

    def create_star(self, node, o):
        # print "Creating star"
        start = self.create_vertex()
        finish = self.create_vertex()
        inner = self.create_state(node.left, finish)
        self.add_transition(start, inner, 'e')
        self.add_transition(start, o, 'e')
        self.add_transition(finish, o, 'e')
        self.add_transition(finish, inner, 'e')
        return start


class DFA:
    def __init__(self):
        self.states = []
        self.start_state = None
        self.final_states = []

    def connect(self, start, final, label):
        trans = self.states[start]
        edge = trans.get(label, set())
        edge.add(final)
        trans[label] = edge

    def new_state(self):
        self.states.append({})
        return len(self.states) - 1

    def nfaToDfa(self, nfa):
        dfa_states = {}
        start_closure = nfa.eclose([nfa.start])
        self.start_state = self.new_state()
        dfa_states[start_closure] = self.start_state
        unmarked = [(start_closure, self.start_state)]

        while unmarked:
            t, index = unmarked.pop()

            for al in ['a', 'b']:
                s_closure = nfa.eclose(nfa.move(t, al))
                if s_closure not in dfa_states:
                    dfa_states[s_closure] = self.new_state()
                    unmarked.append((s_closure, dfa_states[s_closure]))
                self.connect(index, dfa_states[s_closure], al)

        for s in dfa_states:
            if nfa.final in s:
                self.final_states.append(dfa_states[s])

    def to_matrix(self):
        matrix = [[0 for i in range(len(self.states))] for i in range(len(self.states))]

        for i in range(len(self.states)):
            for labels, edges in self.states[i].items():
                for edge in edges:
                    matrix[i][edge] += 1

        return matrix

def matrixMultMod(A, B, m):
    N = [[0 for y in xrange(len(B[0]))] for x in xrange(len(A))]
    for i in xrange(len(A)):
        for j in xrange(len(B[0])):
            for k in xrange(len(B)):
                N[i][j] = (N[i][j] + A[i][k] * B[k][j]) % m
    return N

def matrixPowMod(M, k, m):
    if k == 1:
        return M
    if k % 2 == 0:
        A = matrixPowMod(M, k / 2, m)
        return matrixMultMod(A, A, m)
    if k % 2 == 1:
        return matrixMultMod(M, matrixPowMod(M, k - 1, m), m)

for _ in range(input()):
    st,n = raw_input().split()
    n = int(n)
    root = parse(st)
    nfa = NFA()
    parser = NfaParser(nfa)
    parser.parse(root)
    dfa = DFA()
    dfa.nfaToDfa(nfa)
    matrix = dfa.to_matrix()
    matrix = matrixPowMod(matrix, n, 1000000007)
    ans = 0
    for e in dfa.final_states:
        final = matrix[dfa.start_state][e]
        ans = (ans + final) % 1000000007
    print ans
