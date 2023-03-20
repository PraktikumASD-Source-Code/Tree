class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child (self,child):
        child.parent = self
        self.children.append(child)

    def remove_child (self,child):
        if child in self.children:
            self.children.remove(child)
        else:
            print("Data tidak ditemukan")

    # PRINT TREE
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level
    
    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode("Elektronik")

    laptop = TreeNode("Laptop")
    hp = TreeNode("HP")
    tv = TreeNode ("TV")

    laptop.add_child(TreeNode("ASUS"))
    laptop.add_child(TreeNode("AXIO"))
    laptop.add_child(TreeNode("DELL"))

    hp.add_child(TreeNode("Samsung"))
    hp.add_child(TreeNode("Vivo"))
    # hp.add_child(TreeNode("Xiaomi"))

    xiaomi = TreeNode("Xiaomi")
    hp.add_child(xiaomi)
    xiaomi.add_child(TreeNode("Poco F4"))

    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Sharp"))

    root.add_child(laptop)
    root.add_child(hp)
    root.add_child(tv)

    return root

root = build_product_tree()
root.print_tree()

# print("="* 20)
# laptop = root.children[0]
# laptop.remove_child(laptop.children[0])
# root.print_tree()

# print("="*20)
# root.remove_child(root.children[2])
# root.print_tree()