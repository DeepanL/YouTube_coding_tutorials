from tkinter.tix import Tree


class TreeNode:
    def __init__(self, name, designation):
        self.data = name, designation
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

    def print_tree(self, format):
        if format == 'both':
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix+ self.data[0] + " ({})".format(self.data[1]))
        # if len(self.children) > 0:
            if self.children:
                for child in self.children:
            # print(child.data)
                    child.print_tree(format)
        elif format == 'name':
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix+ self.data[0])
        # if len(self.children) > 0:
            if self.children:
                for child in self.children:
            # print(child.data)
                    child.print_tree(format)
        elif format == 'designation':
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix+ self.data[1])
        # if len(self.children) > 0:
            if self.children:
                for child in self.children:
            # print(child.data)
                    child.print_tree(format)

def build_management_tree():
    root = TreeNode("Nilupul", "CEO")

    cto = TreeNode("Chinmay", "CTO")

    infra_head = TreeNode("Vishwa", "Infrastructre Head")
    infra_head.add_child(TreeNode("Dhaval", "Cloud Manger"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))

    appli_head = TreeNode("Aamir", "Application Head")

    hr_head = TreeNode("Gels", "HR Head")
    hr_head.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    root.add_child(cto)
    cto.add_child(infra_head)
    cto.add_child(appli_head)
    root.add_child(hr_head)

    return root



if __name__ == '__main__':
    root_node = build_management_tree()
    # root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    # root_node.print_tree("both") # prints both (name and designation) hierarchy