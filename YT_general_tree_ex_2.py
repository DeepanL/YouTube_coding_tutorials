class TreeNode:
    def __init__(self, place):
        self.data = place
        self.children = [] # each element of children will be an instance of the TreeNode class
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p =self.parent
        while p:
            level +=1
            p = p.parent
        return level

    # def print_tree(self):
    #     spaces = ' ' * self.get_level() * 3
    #     prefix = spaces + "|__" if self.parent else ""
    #     print(prefix+ self.data)
    #     if self.children:
    #         for child in self.children:
    #             child.print_tree()

    def print_tree(self, level):
        if self.get_level() > level:
            return
        
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix+ self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

def build_location_tree():
    root = TreeNode("Global")

    India = TreeNode("India")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    usa = TreeNode("USA")

    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    cali = TreeNode("California")
    cali.add_child(TreeNode("San Francisco"))
    cali.add_child(TreeNode("Mountain View"))
    cali.add_child(TreeNode("Palo Alto"))

    root.add_child(India)
    India.add_child(gujarat)
    India.add_child(karnataka)
    root.add_child(usa)
    usa.add_child(nj)
    usa.add_child(cali)

    return root


if __name__ == '__main__':
    root_node = build_location_tree()
    root_node.print_tree(1)








    