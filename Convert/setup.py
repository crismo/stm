import pip

def install(package):

    pip.main(['install', package])

install("os")
install("pillow")
install("getopt")
